class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") return "0";

        int n = num1.size(), m = num2.size();
        vector<int> result(n + m, 0);

        // Multiply each digit of num1 and num2
        for (int i = n - 1; i >= 0; --i) {
            for (int j = m - 1; j >= 0; --j) {
                int mul = (num1[i] - '0') * (num2[j] - '0');
                int pos1 = i + j, pos2 = i + j + 1;

                int sum = mul + result[pos2];
                result[pos2] = sum % 10;
                result[pos1] += sum / 10;
            }
        }

        // Convert result vector to string
        string res = "";
        for (int num : result) {
            if (!(res.empty() && num == 0)) res += to_string(num);
        }

        return res.empty() ? "0" : res;
    }
};