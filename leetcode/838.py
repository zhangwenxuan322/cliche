# 838. Push Dominoes

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        lst = list(dominoes)
        dist = [0] * len(dominoes)
        rDist = None
        for i, val in enumerate(lst):
            if val == 'R':
                rDist = 0
            elif val == 'L':
                rDist = None
            elif rDist != None:
                rDist += 1
                dist[i] = rDist
                lst[i] = 'R'
        lDist = None
        for i in range(len(lst) - 1, -1, -1):
            if dominoes[i] == 'L':
                lDist = 0
            elif dominoes[i] == 'R':
                lDist = None
            elif lDist != None:
                lDist += 1
                if lDist < dist[i] or lst[i] == '.':
                    lst[i] = 'L'
                elif lDist == dist[i]:
                    lst[i] = '.'
        return ''.join(lst)
