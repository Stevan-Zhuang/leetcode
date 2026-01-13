impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let mut result: i32 = 0;
        for (i, n) in nums.into_iter().enumerate() {
            result ^= i as i32 + 1;
            result ^= n;
        }
        result
    }
}
