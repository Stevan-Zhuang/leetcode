/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minBitwiseArray(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int *r = malloc(sizeof(int)*numsSize);
    int j;
    int flip;
    for (int i = 0; i < numsSize; i++) {
        r[i] = -1;
        j = 1;
        while (j < nums[i]) {
            if ((nums[i] & j) > 0) {
                flip = nums[i] ^ j;
                if ((flip | (flip + 1)) == nums[i]) {
                    r[i] = flip;
                }
            }
            j <<= 1;
        }
    }
    return r;
}
