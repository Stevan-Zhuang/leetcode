impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let n = cost.len() as usize;
        let mut tab: Vec<i32> = vec![i32::MAX; n + 2];
        tab[0] = 0;
        tab[1] = 0;
        for i in 0..n {
            tab[i + 1] = tab[i + 1].min(tab[i] + cost[i]);
            tab[i + 2] = tab[i + 2].min(tab[i] + cost[i]);
        }
        tab[n]
    }
}
