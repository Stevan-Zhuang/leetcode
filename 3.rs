use std::collections::HashMap;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut best: i32 = 0;
        let mut start: usize = 0;
        let mut prev_chars: HashMap<char, usize> = HashMap::new();
        for (idx, c) in s.chars().enumerate() {
            if prev_chars.contains_key(&c) {
                start = std::cmp::max(start, prev_chars[&c] + 1);
            }
            best = std::cmp::max(best, (idx - start + 1) as i32);
            prev_chars.insert(c, idx);
        }
        return best;
    }
}
