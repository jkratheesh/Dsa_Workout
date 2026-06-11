class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for ch in strs:
            s += ch + ":;"
        return s
    def decode(self, s: str) -> List[str]:
        return s.split(':;')[:-1]