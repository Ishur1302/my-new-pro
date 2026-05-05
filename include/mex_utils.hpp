#ifndef MEX_UTILS_HPP
#define MEX_UTILS_HPP
#include <vector>
#include <set>
#include <algorithm>

namespace GameTheory {
    inline int calculate_mex(const std::vector<int>& values) {
        std::set<int> s(values.begin(), values.end());
        int mex = 0;
        while (s.count(mex)) mex++;
        return mex;
    }
}
#endif
