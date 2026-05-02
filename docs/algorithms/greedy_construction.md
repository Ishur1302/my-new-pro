# Greedy Construction: Maximizing Medians
To maximize the sum of medians in blocks of size K:
1. Identify the position of the median (e.g., in size 3, it's the 2nd largest).
2. Allocate the largest possible values to the median and "larger-than-median" slots.
3. Use the smallest values to fill the "smaller-than-median" slots.
