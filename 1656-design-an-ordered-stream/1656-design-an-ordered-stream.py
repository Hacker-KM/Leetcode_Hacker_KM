class OrderedStream:

    def __init__(self, n: int):
        self.l = [[] for i in range(n)]
        self.ptr = 0
        self.ans= [None]

    def insert(self, idKey: int, value: str) -> List[str]:
        if self.ptr!=idKey-1:
            self.l[idKey-1].append(value)
            self.ans.append([])
        else:
            self.l[idKey-1].append(value)
            res = [value]
            self.ptr+=1
            while self.ptr<len(self.l) and self.l[self.ptr]!=[]:
                res.append(self.l[self.ptr][0])
                self.ptr+=1
            self.ans.append(res)
        return self.ans[-1]

        
            
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)