#include <iostream>
#include <vector>

const int IDS_MAX_DEPTH = 10;

//variables globales
//current_s la position courante
//H la table de hashage des profondeurs des états évaluées
//solved un booléen à vrai si une solution est trouvée
//▶ applyMove(m) joue/ajoute m sur current_s
//▶ undoMove(m) déjoue/retire m sur current_s
//▶ applyMove(m) et undoMove(m) modifient current_s

/*
void DLS(int d) {
    if (solved) return;
    
    H[current_s] = d;

    if (h(current_s) < h(best_s))
        best_s = current_s;

    if (current_s == WIN) {
        solved = true;
        return;
    }

    if (current_s == LOST || d == DLS_MAX_DEPTH)
        return;

    std::vector<Move> M = nextMoves(); // Assuming Move is the type of your move

    for (const auto& m : M) {
        applyMove(m);

        if (H.find(current_s) == H.end() || H[current_s] > d)
            DLS(d + 1);

        undoMove(m);

        if (solved) return;
    }
}

void IDS(int p) {
    int solution_size = 0;

    for (int depth = 1; depth <= IDS_MAX_DEPTH; ++depth) {
        DLS(p, 0);
        if (solution_size != 0) {
            break;
        }
    }
}

int main() {
    return 0;
}
*/
