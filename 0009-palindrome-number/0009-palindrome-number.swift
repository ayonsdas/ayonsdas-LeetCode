class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        if(x < 0 || x > 0 && x % 10 == 0) {
            return false;
        }
        var reversedNum = 0;
        var xP = x;
        while(xP > reversedNum) {
            reversedNum = reversedNum * 10 + xP % 10;
            xP /= 10;
        }
        return reversedNum == xP || xP == reversedNum / 10;
    }
}