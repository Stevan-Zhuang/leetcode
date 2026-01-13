// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        add_digits(l1, l2, 0)
    }
}

fn add_digits(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>, carry: i32
) -> Option<Box<ListNode>> {
    let options = (l1, l2);
    match options {
        (None, None) => {
            if carry != 0 {Some(Box::from(ListNode::new(carry)))} else {None}
        },
        (Some(x), None) | (None, Some(x)) => {
            let sum: i32 = x.val + carry;
            let mut cur = Box::from(ListNode::new(sum % 10));
            cur.next = add_digits(x.next, None, sum / 10);
            Some(cur)
        }
        (Some(x), Some(y)) => {
            let sum: i32 = x.val + y.val + carry;
            let mut cur: Box<ListNode> = Box::from(ListNode::new(sum % 10));
            cur.next = add_digits(x.next, y.next, sum / 10);
            Some(cur)
        }
    }
}
