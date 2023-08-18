class MaxSizeList:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.thislist = []

    def push(self, value):
        if len(self.thislist) >= self.maxsize:
            self.thislist.pop(0)
        self.thislist.append(value)

    def get_list(self):
        return self.thislist



a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("ho")
a.push("let's")
a.push("go")

b.push("hey")
b.push("ho")
b.push("let's")
b.push("go")

print(a.get_list())     # ['ho', "let's", 'go']
print(b.get_list())     # ['go']



