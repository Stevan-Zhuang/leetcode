use std::str;

impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        let mut result: &[u8] = &vec![];
        // s is guaranteed to be only alphanumeric characters, so each byte
        // represents a single character.
        let s_bytes = s.as_bytes();
        assert_eq!(s.len(), s_bytes.len());
        for base in 0..s.len() {
            let mut idx = 0;
            while idx <= base && idx < s.len() - base {
                if s_bytes[base - idx] != s_bytes[base + idx] {
                    break;
                }
                let substr = &s_bytes[(base - idx)..(base + idx + 1)];
                if substr.len() > result.len() {
                    result = substr;
                }
                idx += 1;
            }
        }
        for base in 0..s.len() {
            let mut idx = 0;
            while idx <= base && idx + 1 < s.len() - base {
                if s_bytes[base - idx] != s_bytes[base + idx + 1] {
                    break;
                }
                let substr = &s_bytes[(base - idx)..(base + idx + 2)];
                if substr.len() > result.len() {
                    result = substr;
                }
                idx += 1;
            }
        }
        return str::from_utf8(result).unwrap().to_string();
    }
}
