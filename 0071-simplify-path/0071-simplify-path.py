class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        s = []
        for i in path:
            if i == "..":
                if s:
                    s.pop(-1)
            elif i == "." or i == "":
                continue
            else:
                s.append(i)
        return "/" + "/".join(s)