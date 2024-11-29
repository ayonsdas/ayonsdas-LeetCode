class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set()
        for order in orders:
            foods.add(order[2])
        keys = {}
        for order in orders:
            order[1] = int(order[1])
            if not order[1] in keys:
                keys[order[1]] = {}
                for food in foods:
                    keys[order[1]][food] = 0
            keys[order[1]][order[2]] += 1
        t = []
        l = ["Table"]
        for x in sorted(foods):
            l.append(x)
        t.append(l)
        for x in sorted(keys.keys()):
            z = [str(x)]
            for tx in sorted(keys[x].keys()):
                z.append(str(keys[x][tx]))
            t.append(z)
        return t