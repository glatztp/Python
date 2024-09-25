class Pessoa:
    def __init__(self, n, i):
        self.n = n
        self.i = i
    def ap(self):
        print("n:", self.n)
        print("i:", self.i)

class Pr(Pessoa):
    def __init__(self, n, i, m):
        super().__init__(n, i)
        self.m = m
        self.al = []
    def ap(self):
        print(f"Prof: {self.n}, i: {self.i}, esp: {self.m}")
        for a in self.al:
            a.ap()
    def add_a(self, aluno):
        self.al.append(aluno)
class A(Pessoa):
    def __init__(self, n, i, matr):
        super().__init__(n, i)
        self.matr = matr
    def ap(self):
        print(f"al: {self.n}, i: {self.i}, m: {self.matr}")


n_prof = input("n Prof: ")
i_prof = int(input("i Prof: "))
espec_prof = input("espc Prof: ")
p1 = Pr(n_prof, i_prof, espec_prof)

num_al = int(input("num de al: "))
for _ in range(num_al):
    n_al = input("nome: ")
    i_al = int(input("idade: "))
    matr_al = input("matricula: ")

    aluno = A(n_al, i_al, matr_al)
    p1.add_a(aluno)
p1.ap()