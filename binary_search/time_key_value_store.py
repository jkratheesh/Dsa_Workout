class TimeMap:

    def __init__(self):
        
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        pairs = self.store[key]

        for i in range(len(pairs) - 1,-1,-1):
            if pairs[i][1] <= timestamp:
                return pairs[i][0]
     
        return ""
