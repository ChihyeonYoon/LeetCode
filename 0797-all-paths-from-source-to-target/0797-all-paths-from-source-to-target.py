class Solution(object):
    def __init__(self):
        self.end_idx = 0
        self.answer_list=[]

    def dfs(self, graph, idx, depth, rlist):
        cur_idx = idx
        cur_depth = depth
        cur_rlist = list(rlist) # 리스트 복사
        cur_rlist.append(cur_idx)

        if cur_rlist[-1] == self.end_idx:
            # print(cur_rlist)
            self.answer_list.append(cur_rlist)
            return

        for next_idx in graph[cur_idx]:
            # for next_idx in next_idxs:
            self.dfs(graph, next_idx, depth+1, cur_rlist)
        
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.end_idx = len(graph)-1
        self.dfs(graph, 0, 0, [])

        return self.answer_list
