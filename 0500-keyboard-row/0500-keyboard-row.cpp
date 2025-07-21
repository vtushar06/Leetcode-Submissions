class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        vector<string> result;

        // Define keyboard rows as sets for fast lookup
        string row1 = "qwertyuiop";
        string row2 = "asdfghjkl";
        string row3 = "zxcvbnm";

        for (string word : words) {
            string lowerWord = word;
            for (char& c : lowerWord) c = tolower(c);  // convert to lowercase

            // Determine which row the first character is in
            string* row;
            if (row1.find(lowerWord[0]) != string::npos) row = &row1;
            else if (row2.find(lowerWord[0]) != string::npos) row = &row2;
            else row = &row3;

            // Check if all characters are in the same row
            bool isValid = true;
            for (char c : lowerWord) {
                if (row->find(c) == string::npos) {
                    isValid = false;
                    break;
                }
            }

            if (isValid) result.push_back(word);  // Add the original word
        }

        return result;
    }
};