#include <stdlib.h>

int largestRectangleArea(int* heights, int heightsSize) {
    int* stack = malloc((heightsSize + 1) * sizeof(int));
    int top = -1;
    int maxArea = 0;
    for (int i = 0; i <= heightsSize; i++) {
        int height = (i == heightsSize) ? 0 : heights[i];
        while (top >= 0 && height < heights[stack[top]]) {
            int h = heights[stack[top--]];
            int right = i;
            int left = (top >= 0) ? stack[top] : -1;
            int area = h * (right - left - 1);
            if (area > maxArea) maxArea = area;
        }
        stack[++top] = i;
    }
    free(stack);
    return maxArea;
}
