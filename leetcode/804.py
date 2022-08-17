# 804. Unique Morse Code Words

from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".",
                 "..-.","--.","....","..",".---",
                 "-.-",".-..","--","-.","---",".--.",
                 "--.-",".-.","...","-","..-","...-",
                 ".--","-..-","-.--","--.."]
        
        seen = set()
        
        for word in words:
            representation = ""
            for letter in word:
                index = ord(letter) - ord('a')
                representation += codes[index]
            seen.add(representation)
        
        return len(seen)