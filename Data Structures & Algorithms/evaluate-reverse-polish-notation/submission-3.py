class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        for s in tokens:
            if len(self.stack)>=2 and s == '+':
                val = self.stack[-2] + self.stack[-1]
                self.pop()
                self.pop()
                self.push(val)
            elif len(self.stack)>=2 and s == '-':
                val = self.stack[-2] - self.stack[-1]
                self.pop()
                self.pop()
                self.push(val)
            elif len(self.stack)>=2 and s == '*':
                val = self.stack[-2] * self.stack[-1]
                self.pop()
                self.pop()
                self.push(val)
            elif len(self.stack)>=2 and s == '/':
                val = int(self.stack[-2] / self.stack[-1])
                self.pop()
                self.pop()
                self.push(val)
            else:
                self.push(int(s))
        return self.stack[-1]

    def push(self,val):
        self.stack.append(val)
    def pop(self):
        self.stack.pop()
        