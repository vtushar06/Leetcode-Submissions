class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> rows(9), cols(9), boxes(9);

        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                char current = board[i][j];
                if (current == '.') continue;

                // Check row
                if (rows[i].count(current)) return false;
                rows[i].insert(current);

                // Check column
                if (cols[j].count(current)) return false;
                cols[j].insert(current);

                // Check 3x3 sub-box
                int boxIndex = (i / 3) * 3 + (j / 3);
                if (boxes[boxIndex].count(current)) return false;
                boxes[boxIndex].insert(current);
            }
        }
        return true;
    }
};