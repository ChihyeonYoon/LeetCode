class Solution(object):
    

    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        vowels = ['a','e','i','o','u']
        # answers = []
        global answer
        answer = 0

        def dfs(idx, w, depth):
            global answer
            cur_idx = idx
            cur_w = w
            cur_depth = depth
            if cur_depth == n:
                # answers.append(cur_w)
                
                answer+=1
                return
            
            if cur_depth <= n:
                for i, w in enumerate(vowels[cur_idx:]):
                    dfs(cur_idx+i, cur_w+w, cur_depth+1)

        dfs(0, '', 0)
        # print(answers)
        return answer