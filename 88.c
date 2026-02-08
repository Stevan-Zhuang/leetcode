void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int* result = malloc((m + n) * sizeof(int));
    int i = 0;
    int j = 0;
    while (i + j <  m + n) {
        if (j >= n || (i < m && nums1[i] < nums2[j])) {
            result[i+j] = nums1[i];
            i++;
        } else {
            result[i+j] = nums2[j];
            j++;
        }
    }
    for (int k = 0; k < m + n; k++) {
        nums1[k] = result[k];
    }
}
