# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_integet_dict = dict()
        roman_integet_dict['I'] = 1
        roman_integet_dict['V'] = 5
        roman_integet_dict['X'] = 10
        roman_integet_dict['L'] = 50
        roman_integet_dict['C'] = 100
        roman_integet_dict['D'] = 500
        roman_integet_dict['M'] = 1000

        res = 0
        s_len = len(s)
        subtract_index_list = list()
        for i in range(s_len-1):
            if roman_integet_dict[s[i]] < roman_integet_dict[s[i+1]]:
                subtract_index_list.append(i)
        i = 0
        while i < s_len:
            if i not in subtract_index_list:
                res += roman_integet_dict[s[i]]
                i += 1
            elif i in subtract_index_list:
                res += roman_integet_dict[s[i+1]
                                          ] - roman_integet_dict[s[i]]
                i += 2
        return res
