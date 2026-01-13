#include <math.h>
#define M 100000
int divCount[M+1];
int divSum[M+1];

int sumFourDivisors(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; i++) {
        divCount[nums[i]] = 0;
        divSum[nums[i]] = 0;
    }
    for (int i = 0; i < numsSize; i++) {
        if (divCount[nums[i]] != 0) {
            continue;
        }
        for (int div = 1; div <= (int)sqrt((float)nums[i] + 1); div++) {
            if (nums[i] % div == 0) {
                divCount[nums[i]] += 2;
                divSum[nums[i]] += div;
                divSum[nums[i]] += nums[i] / div;
                if (div * div == nums[i]) {
                    divCount[nums[i]]--;
                    divSum[nums[i]] -= div;
                }
            }
        }
    }
    int res = 0;
    for (int i = 0; i < numsSize; i++) {
        if (divCount[nums[i]] == 4) {
            res += divSum[nums[i]];
        }
    }
    return res;
}
