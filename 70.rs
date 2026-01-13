impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let n = n as usize;
        let mut tab = vec![0; n + 2];
        tab[0] = 1;
        for i in 0..n {
            tab[i + 1] += tab[i];
            tab[i + 2] += tab[i];
        }
        tab[n]
    }
}
