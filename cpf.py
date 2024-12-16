while True:
	cpf = input("Digite o CPF para verificar (só números): ")
	nove_digitos = cpf[:9] #pega os primeiros 9 digitos do cpf
	indice = 0
	somar = 0

	if len(cpf) != 11:
		print("Seu CPF deve ter 11 digitos")
		continue

	while indice < 9:
		digito = int(cpf[indice])
		mult = digito * (10 - indice)

		somar += mult

		indice += 1

	mult = somar * 10
	prim_digito = mult % 11

	if prim_digito >= 10:
		prim_digito = 0

	somar = 0
	indice = 0

	while indice < 10:
		digito = int(cpf[indice])

		mult = digito * (11 - indice)

		somar += mult

		indice += 1

	mult = somar * 10
	segun_digito = mult % 11

	if segun_digito >= 10:
		segun_digito = 0

	cpf_calculado = f"{nove_digitos}{prim_digito}{segun_digito}"

	if cpf == cpf_calculado:
		print("CPF válido!")
	else:
		print("CPF inválido!")