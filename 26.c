int removeDuplicates(int* nums, int numsSize) {
    int i = 0;
    int j = 0;
    int k = numsSize;
    int p = 100+1;
    int* result = malloc(numsSize * sizeof(int));
    while (j < k) {
        if (nums[i] == p) {
            i++;
            k--;
            continue;
        }
        result[j] = nums[i];
        p = nums[i];
        i++;
        j++;
    }
    for (int jj = 0; jj < k; jj++) {
        nums[jj] = result[jj];
    }
    free(result);
    return k;
}
