class Solution {
    fun generate(numRows: Int): List<List<Int>> {
        var b = ArrayList<List<Int>>();
        b.add(listOf(1));
        while(b.size < numRows)
        {
            var x = ArrayList<Int>();
            x.add(1);
            for(t in 1..b.size - 1)
            {
                x.add(b[b.size - 1][t - 1] + b[b.size - 1][t]);
            }
            x.add(1);
            b.add(x);
        }
        return b;
    }
}



/**


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        b = [[1]]
        while len(b) < numRows:
            x = [1]
            for t in range(1, len(b)):
                x.append(b[-1][t - 1] + b[-1][t])
            x.append(1)
            b.append(x)
        return b
        
*/