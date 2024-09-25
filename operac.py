''' ------------------1-------------
e = "oi oi tchau tchau ola"
d = {}
pa = e.lower().split()

for p in pa:
    if p in d:
        d[p] += 1
    else:
        d[p] = 1

print(d)
'''##1

'''-------------------2-------------------
nA = {'Ana': [9, 8, 7], 'João': [10, 6], 'Maria': [8, 7, 9]}
m_d = {}

for a, n in nA.items():
    if n:
        m_d[a] = sum(n) / len(n)
    else:
        m_d[a] = 0

print(m_d)
'''##2

'''-----------3---------------
d = {
    'ana': 8.5,
    'joao': 7.2,
    'maria': 9.0,
    'pedro': 6.8
}
l = list(d.items())

def s_desc(glatz):
    for i in range(len(glatz)):
        for j in range(i + 1, len(glatz)):
            if glatz[i][1] < glatz[j][1]:
                glatz[i], glatz[j] = glatz[j], glatz[i]
    return lst

l = s_desc(l)

for a, n in l:
    print(a)
'''##3

'''------------------4----------------
d1 = {'a': 10, 'b': 5, 'c': 7}
d2 = {'b': 3, 'c': 10, 'd': 4}
result = {}

for k, v in d1.items():
    result[k] = v

for k, v in d2.items():
    if k in result:
        result[k] += v
    else:
        result[k] = v

print(result)
'''##4

'''-------------------------5--------------
d = {'a': 10, 'b': 5, 'c': 7, 'd': 12}
r = ['b', 'd']

for g in r:
    if g in d:
        del d[g]

print(d)
'''##5

'''------------------------------6--------------------
s1 = "ola"
s2 = "alo"

if len(s1) != len(s2):
    print(False)
else:
    cont_s1 = {}
    cont_s2 = {}

    for char in s1:
        if char in cont_s1:
            cont_s1[char] += 1
        else:
            cont_s1[char] = 1

    for char in s2:
        if char in cont_s2:
            cont_s2[char] += 1
        else:
            cont_s2[char] = 1

    if cont_s1 == cont_s2:
        print(True)
    else:
        print(False)
'''##6


sud = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [2, 1, 4, 3, 5, 6, 7, 9, 8],
    [3, 4, 1, 2, 6, 7, 8, 5, 9],
    [4, 3, 2, 1, 7, 8, 9, 6, 5],
    [5, 6, 7, 8, 1, 2, 3, 4, 9],
    [6, 5, 8, 7, 2, 9, 1, 3, 4],
    [7, 9, 6, 5, 3, 1, 2, 8, 4],
    [8, 7, 9, 6, 4, 3, 5, 1, 2]

]
v = True

for i in range(9):
    if sorted(sud[i]) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        v = False
        break

for i in range(9):
    if sorted([sud[j][i] for j in range(9)]) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        v = False
        break
print(v)
##7

'''-------------------8---------------------
g = [("nota1", 10), ("nota2", 3), ("nota3", 4)]

d = {}
for ch, vlr in g:
    d[ch] = vlr

print(d)
'''##8

'''--------------------9--------------------
D = {
    'Nota 1':12,
    'Nota 2': 10,
    'Nota 3': 9
}

vlrP = 10

if vlrP == 10 :
    print("Valor encontrado")
'''##9

'''---------------------10-----------------
e = input("D:")
freq = {}
for g in e:

    if g in freq:
        freq[g] += 1
    else:
        freq[g] = 1

print(":")
for g, cont in freq.items():
    print(f"'{g}': {cont}")
'''#10