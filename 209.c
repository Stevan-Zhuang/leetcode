#define MAX 100000

int min(int a, int b) {
    return a < b ? a : b;
}

int minSubArrayLen(int target, int* nums, int numsSize) {
    int minLen = MAX+1;
    int front = 0;
    int back = 0;
    int cumSum = 0;
    while (back <= front) {
        while (front < numsSize && cumSum < target) {
            cumSum += nums[front++];
        }
        if (cumSum < target) {
            return minLen == MAX+1 ? 0 : minLen;
        }
        minLen = min(minLen, front - back);
        cumSum -= nums[back++];
    }
    return minLen;
}
