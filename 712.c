#include <string.h>

#define MAX 1000
int memo[MAX][MAX];

int min(int a, int b) {
    return a < b ? a : b;
}

int lcsRecursive(char* text1, char* text2, int n, int m) {
    if (n < 0 && m < 0) {
        return 0;
    }
    if (n < 0) {
        int rest = 0;
        for (int j = 0; j <= m; j++)
            rest += (int)text2[j];
        return rest;
    }
    if (m < 0) {
        int rest = 0;
        for (int i = 0; i <= n; i++)
            rest += (int)text1[i];
        return rest;
    }

    if (memo[n][m] != -1) {
        return memo[n][m];
    }
    int res;
    if (text1[n] == text2[m]) {
        res = lcsRecursive(text1, text2, n-1, m-1);
    } else {
        res = min(
            lcsRecursive(text1, text2, n-1, m) + (int)text1[n],
            lcsRecursive(text1, text2, n, m-1) + (int)text2[m]
        );
    }
    memo[n][m] = res;
    return res;
}

int minimumDeleteSum(char* s1, char* s2) {
    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX; j++) {
            memo[i][j] = -1;
        }
    }
    return lcsRecursive(s1, s2,
    strlen(s1)-1, strlen(s2)-1); 
}
