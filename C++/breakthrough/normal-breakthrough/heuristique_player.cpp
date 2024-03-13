#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <iostream>
#include <string>
#include "mybt.h"

bt_t B;
int boardwidth = 0;
int boardheight = 0;
bool white_turn = true;

#ifndef VERBOSE_RAND_PLAYER
#define VERBOSE_RAND_PLAYER
bool verbose = true;
bool showboard_at_each_move = false;
#endif

void help() {
  fprintf(stderr, "  quit\n");
  fprintf(stderr, "  echo ON | OFF\n");
  fprintf(stderr, "  help\n");
  fprintf(stderr, "  name <PLAYER_NAME>\n");
  fprintf(stderr, "  newgame <NBCOL> <NBLINE>\n");
  fprintf(stderr, "  genmove\n");
  fprintf(stderr, "  play <L0C0L1C1>\n");
  fprintf(stderr, "  showboard\n");
}
void name() {
  printf("= heuristique_player\n\n");
}
void newgame() {
  if((boardheight < 1 || boardheight > 10) && (boardwidth < 1 || boardwidth > 10)) {
    fprintf(stderr, "boardsize is %d %d ???\n", boardheight, boardwidth);
    printf("= \n\n");
    return;
  }
  B.init(boardheight, boardwidth);
  white_turn = true;
  if(verbose) fprintf(stderr, "ready to play on %dx%d board\n", boardheight, boardwidth);
  printf("= \n\n");
}
void showboard() {
  B.print_board(stderr);
  printf("= \n\n");
}

void play(char a, char b, char c, char d) {
  bt_move_t m;
  m.line_i = boardheight-(a-'0');
  m.col_i = b-'a';
  m.line_f = boardheight-(c-'0');
  m.col_f = d-'a';
  if(B.can_play(m)) {
    B.play(m);
    if(verbose) {
      m.print(stderr, white_turn, B.nbl);
      fprintf(stderr, "\n");
    }
    white_turn = !white_turn;
  } else {
    fprintf(stderr, "CANT play %d %d %d %d ?\n", m.line_i, m.col_i, m.line_f, m.col_f);
  }
  if(showboard_at_each_move) showboard();
  printf("= \n\n");
}

int heuristique(const bt_t& tab)
{
  int blanc = 0;
  int noir = 0;

  for (int i = 0; i < tab.nbl; i++)
  {
    for (int j = 0; j < tab.nbc; j++)
    {
      if (tab.board[i][j] == WHITE)
      {
        blanc += (tab.nbl - 1 - i);
      }
      else if (tab.board[i][j] == BLACK)
      {
        noir += i;
      }
    }
  }

  return blanc - noir;
}

bt_move_t minimax(bt_t& a, int depth, bool maximizing_player)
{
    if (depth == 0 || a.endgame() != EMPTY)
    {
        return bt_move_t(); //heuristique ici non ?
    }

    if (maximizing_player)
    {
        // Joueur max
        double max_eval_h = -INFINITY;
        bt_move_t best_move;

        a.update_moves();
        for (int i = 0; i < a.nb_moves; i++)
        {
            bt_move_t move = a.moves[i];
            if (a.can_play(move))
            {
                a.play(move);
                double eval_h = heuristique(a);
                a.play(move);

                if (eval_h > max_eval_h)
                {
                    max_eval_h = eval_h;
                    best_move = move;
                }
            }
        }
        return best_move;
    } 
    else
    {
        // Joueur min
        double min_eval_h = INFINITY;
        bt_move_t best_move;

        a.update_moves();
        for (int i = 0; i < a.nb_moves; ++i)
        {
            bt_move_t move = a.moves[i];
            if (a.can_play(move))
            {
                a.play(move);
                double eval_h = heuristique(a);
                a.play(move);

                if (eval_h < min_eval_h)
                {
                    min_eval_h = eval_h;
                    best_move = move;
                }
            }
        }
        return best_move;
    }
}

int main(int _ac, char** _av) {
  bool echo_on = false;
  setbuf(stdout, 0);
  setbuf(stderr, 0);
  if(verbose) fprintf(stderr, "heuristique_player started\n");
  char a,b,c,d; // for play cmd
  for (std::string line; std::getline(std::cin, line);) {
    if(verbose) fprintf(stderr, "heuristique_player receive %s\n", line.c_str());
    if(echo_on) if(verbose) fprintf(stderr, "%s\n", line.c_str());
    if(line.compare("quit") == 0) { printf("= \n\n"); break; }
    else if(line.compare("echo ON") == 0) echo_on = true;
    else if(line.compare("echo OFF") == 0) echo_on = false;
    else if(line.compare("help") == 0) help();
    else if(line.compare("name") == 0) name();
    else if(sscanf(line.c_str(), "newgame %d %d\n", &boardheight, &boardwidth) == 2) newgame();
    else if(line.compare("heuristique") == 0)
    {
    	bt_move_t best_move = minimax(B, 4, white_turn);
    	play('0' + boardheight - best_move.line_i, 'a' + best_move.col_i, '0' + boardheight - best_move.line_f, 'a' + best_move.col_f);
    }
    else if(sscanf(line.c_str(), "play %c%c%c%c\n", &a,&b,&c,&d) == 4) play(a,b,c,d);
    else if(line.compare("showboard") == 0) showboard();
    else if(line.compare(0,2,"//") == 0) ; // just comments
    else fprintf(stderr, "???\n");
    if(echo_on) printf(">");
  }
  if(verbose) fprintf(stderr, "bye.\n");

  return 0;
}
