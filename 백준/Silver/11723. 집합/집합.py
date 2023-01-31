class S:
    def __init__(self):
        self.s = [0] * 21
    
    def add(self, x):
        if self.s[x] == 1:
            return
        self.s[x] = 1
    
    def remove(self, x):
        if self.s[x] == 0:
            return
        self.s[x] = 0
    
    def check(self, x):
        print(self.s[x])
    
    def toggle(self, x):
        if self.s[x] == 1:
            self.s[x] = 0
        else:
            self.s[x] = 1
    
    def all(self):
        self.s = [1] * 21
    
    def empty(self):
        self.s = [0] * 21
input = __import__('sys').stdin.readline
s = S()
for _ in range(int(input())):
    word = list(input().split())
    if word[0] == "add":
        s.add(int(word[1]))
    elif word[0] == "remove":
        s.remove(int(word[1]))
    
    elif word[0] == "check":
        s.check(int(word[1]))
        
    elif word[0] == "toggle":
        s.toggle(int(word[1]))
        
    elif word[0] == "all":
        s.all()
    else:
        s.empty()