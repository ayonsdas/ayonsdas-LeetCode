/* The isBadVersion API is defined in the parent class VersionControl.
      fun isBadVersion(version: Int) : Boolean {} */

class Solution: VersionControl() {
    override fun firstBadVersion(n: Int) : Int {
        var l : Int = 0;
        var r : Int = n;
        while(l <= r)
        {
            var m : Int = l + (r - l) / 2;
            if(isBadVersion(m))
                r = m - 1;
            else
                l = m + 1;
        }
        return l;
	}
}


/**


/* The isBadVersion API is defined in the parent class VersionControl.
      bool IsBadVersion(int version); */

public class Solution : VersionControl {
    public int FirstBadVersion(int n) {
        int l = 1, r = n;
        while(l <= r) 
        {
            int m = l + (r - l) / 2;
            if(IsBadVersion(m))
            {
                r = m - 1;
            }
            else
            {
                l = m + 1;
            }
        }
        return l;
    }
}

*/