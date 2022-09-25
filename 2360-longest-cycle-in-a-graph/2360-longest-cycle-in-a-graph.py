class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        length = len(edges) 
        candidates = {node for node in range(length)}
        dq = collections.deque([]) 
        indegree = [0 for _ in range(length)]
        marked = [False for _ in range(length)]
        
        # Following is a typical code for the topological sort
        for idx, node in enumerate(edges):
            if node != -1:
                indegree[node] += 1
    
        for i in range(length):
            if not indegree[i]: dq.append(i)
                
        while dq:
            node = dq.popleft()
            # we remove the nodes we come across from the 
            # candidates since any nodes in the cycle have other
            # nodes pointing to them and thus have no chance of
            # having an indegree of 0
            candidates.remove(node)
            if edges[node] != -1:
                indegree[edges[node]] -= 1
            if edges[node] != -1 and not indegree[edges[node]]:
                dq.append(edges[node])
        # if the candidates are empty, it means that there is no
        # cycle in the graph 
        if not candidates: return -1
        max_cycle = 0
        # Iterate over the nodes in the cycle only and skip 
        # the ones that we have already examined
        # use Floyd's algorithm to find the cycle length
        for node in candidates:
            if marked[node]: continue
            
            start = edges[node]
            end = edges[edges[node]]
            length = 1
            marked[node] = marked[start] = marked[end] = True
            while start != end:
                start = edges[start]
                end = edges[edges[end]]
                marked[start] = marked[end] = True
            start = node
            while start != end:
                start = edges[start]
                end = edges[end]
            first = start
            
            end = edges[first]
            while end != first:
                end = edges[end]
                length += 1
            max_cycle = max(max_cycle, length)
        return max_cycle