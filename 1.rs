use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut val2idx: HashMap<i32, i32> = HashMap::new();
        for idx in 0..nums.len() {
            let idx_i32: i32 = idx as i32;
            if val2idx.contains_key(&nums[idx]) {
                return vec![val2idx[&nums[idx]], idx_i32];
            }
            val2idx.entry(target - nums[idx]).or_insert(idx_i32);
        }
        return vec![];
    }
}
