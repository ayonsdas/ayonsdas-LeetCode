#include <math.h>

class Solution {
public:
    
    double r;
    double x;
    double y;
    
    Solution(double radius, double x_center, double y_center) {
        r = radius;
        x = x_center;
        y = y_center;
    }
    
    vector<double> randPoint() {
        double rR = sqrt(((double) rand() / (double) RAND_MAX)) * this->r;
        double tR = ((double) rand() / (double) RAND_MAX) * 2 * M_PI;
        return vector<double>{x + rR * cos(tR), y + rR * sin(tR)};
    }
};