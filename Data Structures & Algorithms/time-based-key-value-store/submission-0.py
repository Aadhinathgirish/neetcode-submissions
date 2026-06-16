class TimeMap:

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key]=[]
        self.hashmap[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res=''
        value = self.hashmap.get(key,[])
        l=0
        r=len(value)-1
        while l<=r:
            m =(l+r)//2
            if value[m][1]<=timestamp:
                res=value[m][0]
                l=m+1
            else:
                r=m-1
        return res
        
