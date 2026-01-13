impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        return (0..num_rows).fold(
            String::from(""),
            |mut res, row| {
                res.push_str(&zigzag_row(&s, row, num_rows));
                return res;
            }
        );
    }
}

pub fn zigzag_row(s: &str, row: i32, num_rows: i32) -> String {
    if num_rows == 1 {
        return s.to_string();
    }
    let mut result = String::from("");
    let mut cycle = 0;
    let n = 2 * (num_rows - 1);
    let mut result_add = |idx: usize| -> Option<()> {
        Some(result.push_str(s.get(idx..=idx)?))
    };
    loop {
        let idx_1st: usize = (cycle * n + row) as usize;
        let idx_2nd: usize = (cycle * n + (n - row)) as usize;
        cycle += 1;
        match result_add(idx_1st) {None => break, Some(_) => ()};
        if row == 0 || row == num_rows - 1 {
            continue;
        }
        match result_add(idx_2nd) {None => break, Some(_) => ()};
    }
    return result;
}
