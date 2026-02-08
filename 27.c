int removeElement(int* nums, int numsSize, int val) {
    int i = 0;
    int k = numsSize;
    while (i < k) {
        if (nums[i] == val) {
            for (int j = i; j < k - 1; j++) {
                nums[j] = nums[j+1];
            }
            k--;
            continue;
        }
        i++;
    }
    return k;
}
