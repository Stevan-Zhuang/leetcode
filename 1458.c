#define MAXLEN 500
int memo[MAXLEN+1][MAXLEN+1][2];
int ans[MAXLEN+1][MAXLEN+1][2];

int max(int a, int b) {
    return a > b ? a : b;
}

int MDPMemo(int* n1, int* n2, int n1s, int n2s, int used) {
    if (n1s <= 0 || n2s <= 0) return 0;
    if (ans[n1s][n2s][used]) return memo[n1s][n2s][used];
    int res = n1[n1s-1] * n2[n2s-1] + MDPMemo(n1, n2, n1s - 1, n2s - 1, 1);
    if (n1s != 1 || used) res = max(res, MDPMemo(n1, n2, n1s - 1, n2s, used));
    if (n2s != 1 || used) res = max(res, MDPMemo(n1, n2, n1s, n2s - 1, used));
    ans[n1s][n2s][used] = 1;
    memo[n1s][n2s][used] = res;
    return res;
}

int maxDotProduct(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    for (int i = 0; i < MAXLEN + 1; i++) {
        for (int j = 0; j < MAXLEN + 1; j++) {
            ans[i][j][0] = 0;
            ans[i][j][1] = 0;
        }
    }
    return MDPMemo(nums1, nums2, nums1Size, nums2Size, 0);
}
