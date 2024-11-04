age = int(input("Qual é a tua idade?"))
cos = input("Tens disfarçe?")
medo = input("Tens medo de monstros?")

if age >= 12 and cos == "sim" and medo == "não":
    print("Ok. Podes entrar.")
else:
    print("Não podes ir para aqui.")
    print()
    print("Regras:")
    print("Tens que ter mais de 12 anos")
    print("Tens que ir disfarçado")
    print("Não podes ter medo!")