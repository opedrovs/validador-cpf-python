cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
limpar = cores['limpar']
vermelho = cores['vermelho']
verde = cores['verde']
amarelo = cores['amarelo']
azul = cores['azul']


def linha():
    print(f'{azul}-{limpar}' * 30)


def menu():
    linha()
    print(f'{amarelo}VALIDADOR DE CPF{limpar}'.center(39))
    linha()


def validaCPF(cpfEnviado):
    cpfLimpo = cpfEnviado.replace('.', '').replace('-', '')
    return cpfLimpo


def geraDigito(cpfSemDigitos):
    total = 0
    reverso = len(cpfSemDigitos) + 1

    for stringNumerica in cpfSemDigitos:
        total += reverso * int(stringNumerica)
        reverso -= 1

    digito = 11 - (total % 11)
    return str(digito) if digito <= 9 else '0'


def geraNovoCpf():
    cpfSemDigitos = cpfLimpo[0:-2]
    digito1 = geraDigito(cpfSemDigitos)
    digito2 = geraDigito(cpfSemDigitos + digito1)
    novoCPF = cpfSemDigitos + digito1 + digito2
    return novoCPF


def isSequencia():
    sequencia = cpfLimpo in cpfLimpo[0] * 11
    return sequencia


def valida():
    if not cpfLimpo.isnumeric():
        return False
    if len(cpfLimpo) != 11:
        return False
    if isSequencia():
        return False
    novoCPF = geraNovoCpf()

    return novoCPF == cpfLimpo


menu()
while True:
    cpf = str(input('Digite um CPF: ')).strip()
    cpfLimpo = validaCPF(cpf)
    if valida():
        print(f'{verde}CPF válido!{limpar}')
        break
    else:
        print(f'{vermelho}CPF inválido! Digite um válido!{limpar}')
linha()
print(f'{azul}<<< {amarelo}FIM DO PROGRAMA! {azul}>>>{limpar}'.center(53))
linha()
