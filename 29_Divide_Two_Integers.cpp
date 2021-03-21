class Solution {
public:
    typedef numeric_limits<int> lim;

int divide(int A, int B) {
    if (B == 0) return lim::max();
    // Check A and B for lim::min() before applying abs() to avoid overflow.
    if (B == lim::min()) return A == lim::min() ? 1 : 0;
    int quotient = 0;
    if (A == lim::min()) {
        // quotient is int thus cannot carry -lim::min() 1s,
        // so take special care when abs(B) == 1.
        if (B == -1) return lim::max();
        if (B == 1) return lim::min();
        // Add one B to A to avoid overflow.
        A += abs(B);
        quotient = 1;
    }
    bool positive = (A >= 0) == (B > 0);
    A = abs(A);
    B = abs(B);
    while (A >= B) {
        int quotient_ = 1;
        int B_ = B;
        while (A >= (B_ << 1) && (B_ << 1) > 0) {
            quotient_ <<= 1;
            B_ <<= 1;
        }
        A -= B_;
        quotient += quotient_;
    }
    return positive ? quotient : -quotient;
}
};