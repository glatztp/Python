class F:
    def __init__(self, n, i, s):
        self.n = n
        self.i = i
        self.s = s
    def cs(self):
        return self.s
    def inf(self):
        print(f'n: {self.n}, i: {self.i}, s: {self.cs()}')
class G(F):
    def __init__(self, n, i, s, bns):
        super().__init__(n, i, s)
        self.bns = bns

    def cs(self):
        return self.s + self.bns

class D(F):
    def __init__(self, n, i , s, a):
        super().__init__(n, i, s)
        self.a = a

    def cs(self):
        return self.s + self.a

f1 = F("glatz", 30, 3000)
f2 = G("gbariel", 40, 5000, 2000)
f3 = D("fellipe", 50, 7000, 50)

f1.inf()
f2.inf()
'''
f3.inf()
'''