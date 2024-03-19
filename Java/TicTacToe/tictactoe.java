import java.util.*;

public class TicTacToe {

    private static final int SIZE = 3;
    private static final char EMPTY = '-';
    private static final char PLAYER_X = 'X';
    private static final char PLAYER_O = 'O';

    private char currentPlayer;
    private char[][] board;

    public TicTacToe() {
        board = new char[SIZE][SIZE];
        currentPlayer = PLAYER_X;
        initializeBoard();
    }

    private void initializeBoard() {
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                board[i][j] = EMPTY;
            }
        }
    }

    public void printBoard() {
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }

    public boolean isMoveValid(int row, int col) {
        return row >= 0 && row < SIZE && col >= 0 && col < SIZE && board[row][col] == EMPTY;
    }

    public void makeMove(int row, int col) {
        board[row][col] = currentPlayer;
        currentPlayer = (currentPlayer == PLAYER_X) ? PLAYER_O : PLAYER_X;
    }

    public boolean isGameOver() {
        return hasPlayerWon(PLAYER_X) || hasPlayerWon(PLAYER_O) || isBoardFull();
    }

    private boolean hasPlayerWon(char player) {
        // Check rows and columns
        for (int i = 0; i < SIZE; i++) {
            if ((board[i][0] == player && board[i][1] == player && board[i][2] == player) ||
                (board[0][i] == player && board[1][i] == player && board[2][i] == player)) {
                return true;
            }
        }
        // Check diagonals
        return (board[0][0] == player && board[1][1] == player && board[2][2] == player) ||
               (board[0][2] == player && board[1][1] == player && board[2][0] == player);
    }

    private boolean isBoardFull() {
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                if (board[i][j] == EMPTY) {
                    return false;
                }
            }
        }
        return true;
    }

    public int evaluate() {
        if (hasPlayerWon(PLAYER_X)) {
            return 10;
        } else if (hasPlayerWon(PLAYER_O)) {
            return -10;
        }
        return 0;
    }

    public List<int[]> getPossibleMoves() {
        List<int[]> moves = new ArrayList<>();
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                if (board[i][j] == EMPTY) {
                    moves.add(new int[]{i, j});
                }
            }
        }
        return moves;
    }

    public int[] minimax(int depth, boolean maximizingPlayer) {
        if (isGameOver() || depth == 0) {
            return new int[]{evaluate()};
        }

        if (maximizingPlayer) {
            int bestScore = Integer.MIN_VALUE;
            int[] bestMove = new int[2];
            for (int[] move : getPossibleMoves()) {
                makeMove(move[0], move[1]);
                int score = minimax(depth - 1, false)[0];
                if (score > bestScore) {
                    bestScore = score;
                    bestMove = move;
                }
                board[move[0]][move[1]] = EMPTY;
            }
            return new int[]{bestScore, bestMove[0], bestMove[1]};
        } else {
            int bestScore = Integer.MAX_VALUE;
            int[] bestMove = new int[2];
            for (int[] move : getPossibleMoves()) {
                makeMove(move[0], move[1]);
                int score = minimax(depth - 1, true)[0];
                if (score < bestScore) {
                    bestScore = score;
                    bestMove = move;
                }
                board[move[0]][move[1]] = EMPTY;
            }
            return new int[]{bestScore, bestMove[0], bestMove[1]};
        }
    }

    public static void main(String[] args) {
        TicTacToe game = new TicTacToe();
        Scanner scanner = new Scanner(System.in);

        while (!game.isGameOver()) {
            game.printBoard();
            System.out.println("Player " + game.currentPlayer + "'s turn:");
            System.out.print("Enter row and column (0-2) separated by space: ");
            int row = scanner.nextInt();
            int col = scanner.nextInt();

            if (game.isMoveValid(row, col)) {
                game.makeMove(row, col);
            } else {
                System.out.println("Invalid move! Try again.");
            }
        }

        game.printBoard();
        if (game.evaluate() == 10) {
            System.out.println("Player X wins!");
        } else if (game.evaluate() == -10) {
            System.out.println("Player O wins!");
        } else {
            System.out.println("It's a draw!");
        }

        scanner.close();
    }
}
