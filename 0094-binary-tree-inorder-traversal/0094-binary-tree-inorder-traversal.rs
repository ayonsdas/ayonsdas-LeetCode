// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        
        let mut returnable = vec![];
        fn traverse(node: Option<Rc<RefCell<TreeNode>>>, r: &mut Vec<i32>)
        {
            if let Some(n) = node
            {
                traverse(n.borrow().left.clone(), r);
                r.push(n.borrow().val);
                traverse(n.borrow().right.clone(), r);
            }
        }
        traverse(root, &mut returnable);
        return returnable;
    }
}