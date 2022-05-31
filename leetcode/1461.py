# 1461. Check If a String Contains All Binary Codes of Size K

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        st = set()
        for i in range(k, len(s) + 1):
            st.add(s[i - k: i])
            if len(st) == 1 << k:
                break
        return len(st) == 1 << k

    def test(self):
        assert self.hasAllCodes(s="00110110", k=2) is True
        assert self.hasAllCodes(s="0110", k=1) is True
        assert self.hasAllCodes(s="0110", k=2) is False
        print("all tests passed!")


Solution().test()
