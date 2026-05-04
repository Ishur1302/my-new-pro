#ifndef GAME_UTILS_HPP
#define GAME_UTILS_HPP

namespace GameTheory {
    // Returns true if the first player wins a standard subtraction game
    inline bool can_first_player_win(long long total_moves) {
        return total_moves % 2 != 0;
    }
}

#endif
