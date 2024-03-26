#include <stdio.h>
#include <stdbool.h>

#define SIZE 8

char board[SIZE][SIZE];

// Initialise le tableau de jeu avec les pièces aux positions initiales
void initBoard() {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if ((i + j) % 2 == 1 && i < 3)
                board[i][j] = 'o'; // Pion du joueur 1
            else if ((i + j) % 2 == 1 && i > 4)
                board[i][j] = 'x'; // Pion du joueur 2
            else
                board[i][j] = ' ';
        }
    }
}

// Affiche le tableau de jeu
void printBoard() {
    printf("  0 1 2 3 4 5 6 7\n");
    for (int i = 0; i < SIZE; i++) {
        printf("%d ", i);
        for (int j = 0; j < SIZE; j++) {
            printf("%c ", board[i][j]);
        }
        printf("\n");
    }
}

// Vérifie si une position est valide sur le plateau
bool isValidPosition(int row, int col) {
    return row >= 0 && row < SIZE && col >= 0 && col < SIZE;
}

// Vérifie si une case contient une pièce du joueur donné
bool isPlayerPiece(char player, int row, int col) {
    return isValidPosition(row, col) && (board[row][col] == player || board[row][col] == player - ('o' - 'x'));
}

// Vérifie si une case contient une pièce adverse
bool isOpponentPiece(char player, int row, int col) {
    return isValidPosition(row, col) && (board[row][col] == (player - ('o' - 'x')));
}

// Déplace une pièce d'une position à une autre
void movePiece(int fromRow, int fromCol, int toRow, int toCol) {
    board[toRow][toCol] = board[fromRow][fromCol];
    board[fromRow][fromCol] = ' ';
}

// Vérifie si une pièce peut effectuer une prise
bool canCapture(char player, int row, int col) {
    if (board[row][col] == ' ')
        return false;

    char opponent = (player == 'o') ? 'x' : 'o';
    int dir = (player == 'o') ? 1 : -1;

    // Vérification pour une prise vers la gauche
    if (isValidPosition(row + dir, col - 1) && isOpponentPiece(player, row + dir, col - 1) &&
        isValidPosition(row + 2 * dir, col - 2) && board[row + 2 * dir][col - 2] == ' ')
        return true;

    // Vérification pour une prise vers la droite
    if (isValidPosition(row + dir, col + 1) && isOpponentPiece(player, row + dir, col + 1) &&
        isValidPosition(row + 2 * dir, col + 2) && board[row + 2 * dir][col + 2] == ' ')
        return true;

    return false;
}

// Vérifie si un joueur peut effectuer une prise avec n'importe quelle pièce
bool canPlayerCapture(char player) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j] == player && canCapture(player, i, j))
                return true;
        }
    }
    return false;
}

// Vérifie si un joueur peut encore bouger
bool canPlayerMove(char player) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j] == player) {
                if (isValidPosition(i + 1, j - 1) && board[i + 1][j - 1] == ' ')
                    return true;
                if (isValidPosition(i + 1, j + 1) && board[i + 1][j + 1] == ' ')
                    return true;
                if (canCapture(player, i, j))
                    return true;
            }
        }
    }
    return false;
}

// Vérifie si le jeu est terminé
bool gameOver() {
    return !canPlayerMove('o') || !canPlayerMove('x');
}

// Évalue le plateau
int evaluateBoard() {
    int score = 0;
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j] == 'o')
                score += 1;
            else if (board[i][j] == 'x')
                score -= 1;
            else if (board[i][j] == 'O')
                score += 3;
            else if (board[i][j] == 'X')
                score -= 3;
        }
    }
    return score;
}

// Implémente l'algorithme Minimax pour les dames
int minimax(char player, int depth, bool isMaximizing) {
    if (depth == 0 || gameOver()) {
        return evaluateBoard();
    }

    if (isMaximizing) {
        int bestScore = -1000;
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                if (board[i][j] == player || board[i][j] == player - ('o' - 'x')) {
                    if (isValidPosition(i + 1, j - 1) && board[i + 1][j - 1] == ' ') {
                        movePiece(i, j, i + 1, j - 1);
                        bestScore = max(bestScore, minimax(player, depth - 1, false));
                        movePiece(i + 1, j - 1, i, j);
                    }
                    if (isValidPosition(i + 1, j + 1) && board[i + 1][j + 1] == ' ') {
                        movePiece(i, j, i + 1, j + 1);
                        bestScore = max(bestScore, minimax(player, depth - 1, false));
                        movePiece(i + 1, j + 1, i, j);
                    }
                    if (canCapture(player, i, j)) {
                        if (isValidPosition(i + 2, j - 2) && board[i + 2][j - 2] == ' ') {
                            movePiece(i, j, i + 2, j - 2);
                            bestScore = max(bestScore, minimax(player, depth - 1, false));
                            movePiece(i + 2, j - 2, i, j);
                        }
                        if (isValidPosition(i + 2, j + 2) && board[i + 2][j + 2] == ' ') {
                            movePiece(i, j, i + 2, j + 2);
                            bestScore = max(bestScore, minimax(player, depth - 1, false));
                            movePiece(i + 2, j + 2, i, j);
                        }
                    }
                }
            }
        }
        return bestScore;
    } else {
        int bestScore = 1000;
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                if (board[i][j] == player || board[i][j] == player - ('o' - 'x')) {
                    if (isValidPosition(i + 1, j - 1) && board[i + 1][j - 1] == ' ') {
                        movePiece(i, j, i + 1, j - 1);
                        bestScore = min(bestScore, minimax(player, depth - 1, true));
                        movePiece(i + 1, j - 1, i, j);
                    }
                    if (isValidPosition(i + 1, j + 1) && board[i + 1][j + 1] == ' ') {
                        movePiece(i, j, i + 1, j + 1);
                        bestScore = min(bestScore, minimax(player, depth - 1, true));
                        movePiece(i + 1, j + 1, i, j);
                    }
                    if (canCapture(player, i, j)) {
                        if (isValidPosition(i + 2, j - 2) && board[i + 2][j - 2] == ' ') {
                            movePiece(i, j, i + 2, j - 2);
                            bestScore = min(bestScore, minimax(player, depth - 1, true));
                            movePiece(i + 2, j - 2, i, j);
                        }
                        if (isValidPosition(i + 2, j + 2) && board[i + 2][j + 2] == ' ') {
                            movePiece(i, j, i + 2, j + 2);
                            bestScore = min(bestScore, minimax(player, depth - 1, true));
                            movePiece(i + 2, j + 2, i, j);
                        }
                    }
                }
            }
        }
        return bestScore;
    }
}

// Fonction utilitaire pour trouver le maximum de deux nombres
int max(int a, int b) {
    return (a > b) ? a : b;
}

// Fonction utilitaire pour trouver le minimum de deux nombres
int min(int a, int b) {
    return (a < b) ? a : b;
}

// Joue le meilleur coup pour l'IA en utilisant l'algorithme Minimax
void playAIMove(char player) {
    int bestScore = -1000;
    int bestMoveRow, bestMoveCol;

    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j] == player || board[i][j] == player - ('o' - 'x')) {
                if (isValidPosition(i + 1, j - 1) && board[i + 1][j - 1] == ' ') {
                    movePiece(i, j, i + 1, j - 1);
                    int moveScore = minimax(player, 3, false);
                    movePiece(i + 1, j - 1, i, j);
                    if (moveScore > bestScore) {
                        bestScore = moveScore;
                        bestMoveRow = i;
                        bestMoveCol = j;
                    }
                }
                if (isValidPosition(i + 1, j + 1) && board[i + 1][j + 1] == ' ') {
                    movePiece(i, j, i + 1, j + 1);
                    int moveScore = minimax(player, 3, false);
                    movePiece(i + 1, j + 1, i, j);
                    if (moveScore > bestScore) {
                        bestScore = moveScore;
                        bestMoveRow = i;
                        bestMoveCol = j;
                    }
                }
                if (canCapture(player, i, j)) {
                    if (isValidPosition(i + 2, j - 2) && board[i + 2][j - 2] == ' ') {
                        movePiece(i, j, i + 2, j - 2);
                        int moveScore = minimax(player, 3, false);
                        movePiece(i + 2, j - 2, i, j);
                        if (moveScore > bestScore) {
                            bestScore = moveScore;
                            bestMoveRow = i;
                            bestMoveCol = j;
                        }
                    }
                    if (isValidPosition(i + 2, j + 2) && board[i + 2][j + 2] == ' ') {
                        movePiece(i, j, i + 2, j + 2);
                        int moveScore = minimax(player, 3, false);
                        movePiece(i + 2, j + 2, i, j);
                        if (moveScore > bestScore) {
                            bestScore = moveScore;
                            bestMoveRow = i;
                            bestMoveCol = j;
                        }
                    }
                }
            }
        }
    }

    // Effectue le meilleur coup trouvé
    if (bestScore != -1000) {
        if (canCapture(player, bestMoveRow, bestMoveCol)) {
            if (isValidPosition(bestMoveRow + 2, bestMoveCol - 2) && board[bestMoveRow + 2][bestMoveCol - 2] == ' ') {
                movePiece(bestMoveRow, bestMoveCol, bestMoveRow + 2, bestMoveCol - 2);
            }
            if (isValidPosition(bestMoveRow + 2, bestMoveCol + 2) && board[bestMoveRow + 2][bestMoveCol + 2] == ' ') {
                movePiece(bestMoveRow, bestMoveCol, bestMoveRow + 2, bestMoveCol + 2);
            }
        } else {
            if (isValidPosition(bestMoveRow + 1, bestMoveCol - 1) && board[bestMoveRow + 1][bestMoveCol - 1] == ' ') {
                movePiece(bestMoveRow, bestMoveCol, bestMoveRow + 1, bestMoveCol - 1);
            }
            if (isValidPosition(bestMoveRow + 1, bestMoveCol + 1) && board[bestMoveRow + 1][bestMoveCol + 1] == ' ') {
                movePiece(bestMoveRow, bestMoveCol, bestMoveRow + 1, bestMoveCol + 1);
            }
        }
    }
}

int main() {
    initBoard();
    char currentPlayer = 'o';

    // Tant que le jeu n'est pas terminé
    while (!gameOver()) {
        printBoard();

        if (currentPlayer == 'o') {
            printf("Tour du joueur o :\n");
            // Logique de mouvement du joueur o
        } else {
            printf("Tour de l'IA :\n");
            playAIMove('x');
        }

        currentPlayer = (currentPlayer == 'o') ? 'x' : 'o';
    }

    // Affiche le résultat final
    printBoard();
    printf("Le jeu est terminé.\n");
    // Affiche le gagnant ou s'il y a match nul

    return 0;
}
