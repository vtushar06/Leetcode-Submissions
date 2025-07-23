class Solution {
public:
    int removePattern(string& s, char first, char second, int score) {
        stack<char> st;
        int points = 0;
        
        for (char c : s) {
            if (!st.empty() && st.top() == first && c == second) {
                st.pop();
                points += score;
            } else {
                st.push(c);
            }
        }
        
        // Rebuild remaining string after first removal pass
        s = "";
        while (!st.empty()) {
            s += st.top();
            st.pop();
        }
        reverse(s.begin(), s.end());
        
        return points;
    }

    int maximumGain(string s, int x, int y) {
        int total = 0;
        
        if (x > y) {
            total += removePattern(s, 'a', 'b', x); // Remove "ab" first
            total += removePattern(s, 'b', 'a', y); // Then remove "ba"
        } else {
            total += removePattern(s, 'b', 'a', y); // Remove "ba" first
            total += removePattern(s, 'a', 'b', x); // Then remove "ab"
        }
        
        return total;
    }
};