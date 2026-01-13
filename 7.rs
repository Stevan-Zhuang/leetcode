impl Solution {
    pub fn reverse(x: i32) -> i32 {
        checked_reverse(x).unwrap_or_default()
    }
}

pub fn checked_reverse(x: i32) -> Option<i32> {
    if x.is_negative() {
        return Some(-Solution::reverse(0_i32.checked_sub(x)?));
    }
    let mut digits: Vec<i32> = vec![];
    let mut x_calc = x;
    while x_calc > 0 {
        digits.push(x_calc % 10);
        x_calc /= 10;
    }
    let mut result: i32 = 0;
    let mut multiplier = 10_i32.pow((digits.len() - 1) as u32);
    for digit in digits {
        let new_digit = digit.checked_mul(multiplier)?;
        result = result.checked_add(new_digit)?;
        multiplier /= 10;
    }
    return Some(result);
}
