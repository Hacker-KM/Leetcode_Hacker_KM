class TextEditor:

    def __init__(self):
        self.ans = "|"

    def addText(self, text: str) -> None:
        index = self.ans.index('|')
        self.ans = self.ans[:index]+text+"|"+self.ans[index+1:]
        

    def deleteText(self, k: int) -> int:
        temp = self.ans
        index = self.ans.index("|")
        if len(self.ans[:index])>=k:        
            self.ans = self.ans[:index-k]+self.ans[index:]
        else:
            self.ans = self.ans[index:]
        return len(temp) - len(self.ans)
        

    def cursorLeft(self, k: int) -> str:
        index = self.ans.index('|')
        if index<k:
            self.ans = self.ans.replace("|","")
            self.ans = "|"+self.ans
        else:
            self.ans = self.ans.replace("|","")
            self.ans = self.ans[:index-k]+"|"+self.ans[index-k:]
        
        index = self.ans.index('|')
        if self.ans.index("|")>10:
            return self.ans[index-10:index]
        return self.ans[:self.ans.index("|")]
        

    def cursorRight(self, k: int) -> str:
        index = self.ans.index('|')
        if len(self.ans)-index<k:
            self.ans = self.ans.replace("|","")
            self.ans = self.ans+"|"
        else:
            self.ans = self.ans.replace("|","")
            self.ans = self.ans[:index+k]+"|"+self.ans[index+k:]
        
        index = self.ans.index('|')
        if self.ans.index("|")>10:
            return self.ans[index-10:index]
        return self.ans[:self.ans.index("|")]



# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)