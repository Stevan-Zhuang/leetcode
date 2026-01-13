impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        let mut mem = vec![0; (n + 1) as usize];
        for i in 1..=n {
            mem[i as usize] = mem[(i >> 1) as usize] + (i & 1);
        }
        mem
    }
}
