texto_inteiro = input ("Digite um número inteiro: ")
texto_float = input ("Digite um número flutuante: ")
texto_bool = input ("Digite um alor booleano (True ou False): ")

numero_inteiro = int(texto_inteiro)
numero_float = float(texto_float)
limpar_bool = texto_bool.strip().lower()
valor_booleano = limpar_bool == "true"

print("\nValores convertidos:")
print(f" - Número inteiro: {numero_inteiro}(tipo: {type(numero_inteiro).__name__})")
print(f" - Número flutuante: {numero_float}(tipo: {type(numero_float).__name__})")
print(f" - Valor booleano: {valor_booleano}(tipo: {type(valor_booleano).__name__})")