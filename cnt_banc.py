from atvds.classe import ContaBancaria

contas = {
    "glatz": ContaBancaria("Glatz", 1000),
    "kobielski": ContaBancaria("Kobielski", 100),
    "zipper": ContaBancaria("Zipper", 50)
}

def contaAT():
    for titular in contas:
        print(titular)
    n_titular = input("nometitular: ").strip()
    return contas.get(n_titular, None)
conta = None

while True:
    if conta is None:
        conta = contaAT()
        if conta is None:
            print("nao pdoe")
            continue

    print("\nescolha:")
    print("1 - saque")
    print("2 - depsito")
    print("3 - historico")
    print("4 - saldo")
    print("5 - sair")

    acao = int(input(": "))

    if acao == 1:
        quantd = float(input("saque: "))
        conta.sacar(quantd)

    elif acao == 2:
        quantd = float(input("deposito: "))
        conta.deposito(quantd)

    elif acao == 3:
        conta.m_hist()

    elif acao == 4:
        print(f"saldo atual: {conta.m_s():.2f}")

    elif acao == 5:
        break

    else:
        print("nao pode")
        continue