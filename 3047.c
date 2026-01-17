int abs(int x) {
    return x < 0 ? -x : x;
}
long long min(long long x, long long y) {
    return x < y ? x : y;
}
long long max(long long x, long long y) {
    return x > y ? x : y;
}

long long largestSquareArea(int** bottomLeft, int bottomLeftSize, int* bottomLeftColSize, int** topRight, int topRightSize, int* topRightColSize) {
    long long aX, aY, aW, aH, bX, bY, bW, bH;
    long long x_overlap, y_overlap;
    long long max_area = 0;
    for (int i = 0; i < bottomLeftSize; i++) {
        for (int j = i + 1; j < bottomLeftSize; j++) {
            aX = bottomLeft[i][0] + topRight[i][0];
            aY = bottomLeft[i][1] + topRight[i][1];
            aW = abs(bottomLeft[i][0] - topRight[i][0]);
            aH = abs(bottomLeft[i][1] - topRight[i][1]);
            bX = bottomLeft[j][0] + topRight[j][0];
            bY = bottomLeft[j][1] + topRight[j][1];
            bW = abs(bottomLeft[j][0] - topRight[j][0]);
            bH = abs(bottomLeft[j][1] - topRight[j][1]);
            x_overlap = (aW + bW) - abs(aX - bX);
            y_overlap = (aH + bH) - abs(aY - bY);
            if (x_overlap > 0 && y_overlap > 0) {
                x_overlap = min(min(aW, bW), x_overlap/2);
                y_overlap = min(min(aH, bH), y_overlap/2);
                max_area = max(min(x_overlap, y_overlap) * min(x_overlap, y_overlap), max_area);
            } 
        }
    }
    return max_area;
}
