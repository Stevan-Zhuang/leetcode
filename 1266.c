int max(int a, int b) {
    return a > b ? a : b;
}
int abs(int a) {
    return a < 0 ? -a : a;
}

int minTimeToVisitAllPoints(int** points, int pointsSize, int* pointsColSize) {
    int total = 0;
    int pastX = points[0][0];
    int pastY = points[0][1];
    for (int i = 1; i < pointsSize; i++) {
        total += max(abs(points[i][0] - pastX), abs(points[i][1] - pastY));
        pastX = points[i][0];
        pastY = points[i][1];
    }
    return total;
}
