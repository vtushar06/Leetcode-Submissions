/**
 * Definition for a binary tree node.
 * struct TreeNode {
 * int val;
 * TreeNode *left;
 * TreeNode *right;
 * TreeNode() : val(0), left(nullptr), right(nullptr) {}
 * TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 * TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        // We use LONG_MIN and LONG_MAX to safely handle edge cases 
        // where node values are INT_MIN or INT_MAX.
        return validate(root, LONG_MIN, LONG_MAX);
    }

private:
    bool validate(TreeNode* node, long long minVal, long long maxVal) {
        // An empty node is technically a valid BST
        if (node == nullptr) {
            return true;
        }

        // The current node's value must be strictly inside the valid range
        if (node->val <= minVal || node->val >= maxVal) {
            return false;
        }

        // Recursively validate subtrees:
        // 1. Go Left: Update max limit to current node's value
        // 2. Go Right: Update min limit to current node's value
        return validate(node->left, minVal, node->val) &&
               validate(node->right, node->val, maxVal);
    }
};