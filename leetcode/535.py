# 535. Encode and Decode TinyURL
import random
import string


class Codec:
    def __init__(self):
        self.db = {}
        self.alphabet = string.ascii_letters + "0123456789"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        suffix = ''.join(random.choices(self.alphabet, k=6))
        while suffix in self.db.keys():
            suffix = ''.join(random.choices(self.alphabet, k=6))
        self.db[suffix] = longUrl
        return "http://tinyurl.com/" + suffix

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.db[shortUrl.split('/')[-1]]


# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.decode(codec.encode("www.google.com")))
