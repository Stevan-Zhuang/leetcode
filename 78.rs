impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut combinations: u16 = 0;
        for _ in 0..nums.len() {
            combinations <<= 1;
            combinations |= 1;
        }
        for bitmask in 0..=combinations {
            let mut subset: Vec<i32> = Vec::new();
            for (i, &num) in nums.iter().enumerate() {
                if bitmask & (1 << i) > 0 {
                    subset.push(num);
                }
            }
            result.push(subset);
        }
        result
    }
}
