class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        t = []
        for a in asteroids:
            if a > 0:
                t.append(a)
            else:
                while t and t[-1] > 0 and -a > t[-1]:
                    t.pop(-1)
                if t and t[-1] > 0:
                    if -a == t[-1]:
                        t.pop(-1)
                else:
                    t.append(a)
        return t