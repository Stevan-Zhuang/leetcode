/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minBitwiseArray(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int *r = malloc(sizeof(int)*numsSize);
    for (int i = 0; i < numsSize; i++) {
        r[i] = -1;
        for (int j = 1; j < nums[i]; j++) {
            if ((j | (j+1)) == nums[i]) {
                r[i] = j;
                break;
            }
        }
    }
    return r;
}
