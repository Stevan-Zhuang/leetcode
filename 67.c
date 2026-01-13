#include <string.h>
#include <stdlib.h>

char* addBinary(char* a, char* b) {
    int len_a = strlen(a);
    int len_b = strlen(b);
    int maxLen = (len_a > len_b ? len_a : len_b) + 1;
    char* res = malloc(maxLen + 1);
    res[maxLen] = '\0';
    int i = strlen(a) - 1;
    int j = strlen(b) - 1;
    int carry = 0;
    int sum = 0;
    int k = maxLen - 1;
    while (i >= 0 || j >= 0 || carry > 0) {
        sum = carry;
        if (i >= 0) sum += a[i--] == '1';
        if (j >= 0) sum += b[j--] == '1';
        res[k--] = (sum & 1) + '0';
        carry = (sum & 2) >> 1;
    }
    for (int i = 0; i < maxLen - k; i++) {
        res[i] = res[i + k + 1];
    }
    return res;
}
