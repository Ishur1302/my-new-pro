# Greedy Reordering Strategies
When minimizing subarray properties (like product divisibility), the goal is often to separate "trigger" elements.
- **Example:** To minimize products divisible by 6, keep factors of 2 and 3 at opposite ends of the array.
- **Pattern:** [Multiples of 6] -> [Multiples of 2] -> [Neutrals] -> [Multiples of 3]
