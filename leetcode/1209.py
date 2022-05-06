# 1209. Remove All Adjacent Duplicates in String II

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * k for c, k in stack)

    def test(self):
        assert self.removeDuplicates(s="abcd", k=2) == "abcd"
        assert self.removeDuplicates(s="deeedbbcccbdaa", k=3) == "aa"
        assert self.removeDuplicates(s="pbbcggttciiippooaais", k=2) == "ps"
        print("all tests passed")


Solution().test()
