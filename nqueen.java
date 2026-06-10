/*
N-Queen Problem using Backtracking

Approach:
1. Place one queen in each row.
2. Check if the position is safe.
3. Recursively place queens in the next row.
4. Backtrack if no valid position is found.

Time Complexity: O(N!)
Space Complexity: O(N)
*/
import java.util.*;
public class nqueen {
    

    public static boolean isSafe(char board[][], int row, int col)
    {
        // vertical up
        for(int i = row - 1; i >= 0; i--)
        {
            if(board[i][col] == 'Q')
            {
                return false;
            }
        }

        // diagonal left up
        for(int i = row - 1, j = col - 1;
            i >= 0 && j >= 0;
            i--, j--)
        {
            if(board[i][j] == 'Q')
            {
                return false;
            }
        }

        // diagonal right up
        for(int i = row - 1, j = col + 1;
            i >= 0 && j < board.length;
            i--, j++)
        {
            if(board[i][j] == 'Q')
            {
                return false;
            }
        }

        return true;
    }

    public static void nqueen(char board[][], int row)
    {
        if(row == board.length)
        {
            printboard(board);
            return;
        }

        for(int j = 0; j < board.length; j++)
        {
            if(isSafe(board, row, j))
            {
                board[row][j] = 'Q';

                nqueen(board, row + 1);

                board[row][j] = 'X'; // backtracking
            }
        }
    }

    public static void printboard(char board[][])
    {
        System.out.println("-----chessboard-----");

        for(int i = 0; i < board.length; i++)
        {
            for(int j = 0; j < board.length; j++)
            {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void main(String[] args)
    {
        int n = 4;

        char board[][] = new char[n][n];

        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
            {
                board[i][j] = 'X';
            }
        }

        nqueen(board, 0);
    }
}

