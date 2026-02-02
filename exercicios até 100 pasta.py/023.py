numero = int(input("Digite um número entre 0 e 9999: "))

# Extrai cada dígito do número
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

print (f"""unidade: {unidade}
dezena: {dezena}
centena: {centena}
milhar: {milhar}""")