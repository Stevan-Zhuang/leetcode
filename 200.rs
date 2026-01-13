impl Solution {
    pub fn num_islands(grid: Vec<Vec<char>>) -> i32 {
        let mut count = 0;
        let mut grid = grid;
        let grid_height = grid.len();
        let grid_width = grid[0].len();
        for i in 0..grid_height {
            for j in 0..grid_width {
                if grid[i][j] == '1' {
                    Self::dfs(&mut grid, i as i32, j as i32);
                    count += 1;
                }
            }
        }
        count
    }

    fn dfs(grid: &mut Vec<Vec<char>>, i: i32, j: i32) {
        if i < 0 || j < 0 || i as usize >= grid.len() || j as usize >= grid[0].len() || grid[i as usize][j as usize] != '1' {
            return;
        }
        grid[i as usize][j as usize] = '0';
        Self::dfs(grid, i+1, j);
        Self::dfs(grid, i-1, j);
        Self::dfs(grid, i, j+1);
        Self::dfs(grid, i, j-1);
    }
}
