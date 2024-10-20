#include <vector>   
#include <iostream> 
using namespace std;

/* 
    I have solved this a while ago on Leetcode
    but main reference link i used was this: 
    https://leetcode.com/problems/sudoku-solver/solutions/5513231/easy-clean-code-backtracking-c/
*/ 
/*
    If I were to solve this again, I would utilize 3 sets, one for columns, one for rows, and 
    one for the sub-boxes to check validity over calling an expensive function like isValid.
*/

class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        fillBoard(board);
    }
    // helper function to fill in valid Sudoku values (backtracking approach)
    bool fillBoard(vector<vector<char>>& board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    // iterate through all values 1-9, then place value if valid
                    for (char ch = '1'; ch <= '9'; ch++) {
                        if (isValid(board, i, j, ch)) {
                            board[i][j] = ch;
                            if (fillBoard(board) == true) {
                                return true;
                            }
                            else {
                                board[i][j] = '.';
                            }
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
    bool isValid(vector<vector<char>>& board, int row, int col, char ch) {
        for (int i = 0; i < 9; i++) {
            // checks rows and columns for validity
            if ((board[i][col] == ch) || (board[row][i] == ch)) {
                return false;
            }
            // checks sub-box for validity
            if (board[3 * (row / 3)  +  i / 3][3 * (col / 3)  +  i % 3] == ch) {
                return false;
            }
        }
        return true;
    }
};

// Example usage
int main() {
    Solution sol;
    vector<vector<char>> board = {
        {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
    };
    
    sol.solveSudoku(board);
    
    // Prints the solved board
    for (const auto& row : board) {
        for (char num : row) {
            cout << num << ' ';
        }
        cout << endl;
    }

    return 0;
}
