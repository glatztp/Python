class M:
    def __init__(self, t, a, an):
        self.t = t
        self.a = a
        self.an = an

    def d(self):
        print(f"Titulo: {self.t}\nAutor: {self.a}\nAno: {self.an}")

class L(M):
    def __init__(self, t, a, an, i):
        super().__init__(t, a, an)
        self.i = i

    def d(self):
        print(f"Titulo: {self.t}\nAutor: {self.a}\nAno: {self.an}\nISBN: {self.i}")

class R(M):
    def __init__(self, t, a, an, e):
        super().__init__(t, a, an)
        self.e = e

    def d(self):
        print(f"\n\nTitulo: {self.t}\nAutor: {self.a}\nAno: {self.an}\nEdição: {self.e}")

class B:
    def __init__(self):
        self.m = []

    def add(self, mat):
        self.m.append(mat)

    def list(self):
        for mat in self.m:
            mat.d()

    def by_a(self, a):
        return [mat for mat in self.m if mat.a == a]

    def by_an(self, an):
        return [mat for mat in self.m if mat.an == an]

b = B()
l1 = L("O Pequeno Príncipe", "Antoine", 1943, "978-3-16-148410-0")
r1 = R("Science", "Edição 1", 2022, 1)
r2 = R("Science", "Edição 2", 2022, 2)

b.add(l1)
b.add(r1)
b.add(r2)

b.list()

for mat in b.by_a("Antoine"):
    print("\nLivro encontrado!\n")
    mat.d()

for mat in b.by_an(2022):
    print("\nLivro encontrado pelo ano!\n")
    mat.d()