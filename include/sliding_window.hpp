// Standard Sliding Window Template
void sliding_window(string s) {
    int l = 0, r = 0;
    while (r < s.size()) {
        // Expand window
        r++;
        // Contract window
        while (/* condition */ l < r) {
            l++;
        }
    }
}
