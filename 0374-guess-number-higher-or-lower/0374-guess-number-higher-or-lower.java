// The guess API is defined in the parent class GuessGame.
// int guess(int num);

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int left = 1, right = n;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            int res = guess(mid);

            if (res == 0) return mid;        // Correct guess
            else if (res < 0) right = mid - 1; // Your guess is higher
            else left = mid + 1;             // Your guess is lower
        }

        return -1; // fallback, although per constraints this won't happen
    }
}