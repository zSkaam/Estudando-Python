manteiga = 7.49
carne = 27.69
oleo = 10.70
arroz = 20.00
feijao = 12.00
açucar = 11.45
cafe = 20.34
sal = 7.34
macarrao = 19.35
leite = 11.34

quantidade_manteiga = int(input("Digite a quantidade de manteiga desejado: "))
quantidade_carne = int(input("Digite a quantidade de carne desejado: "))
quantidade_oleo = int(input("Digite a quantidade de oleo desejado: "))
quantidade_arroz = int(input("Digite a quantidade de arroz desejado: "))
quantidade_feijao = int(input("Digite a quantidade de feijão desejado: "))
quantidade_açucar = int(input("Digite a quantidade de açucar desejado: "))
quantidade_cafe = int(input("Digite a quantidade de cafe desejado: "))
quantidade_sal = int(input("Digite a quantidade de sal desejado: "))
quantidade_macarrao = int(input("Digite a quantidade de macarrão desejado: "))
quantidade_leite = int(input("Digite a quantidade de leite desejado: "))
 
preco_total = (manteiga * quantidade_manteiga) + (carne * quantidade_carne) + (oleo * quantidade_oleo) + (arroz * quantidade_arroz) + (feijao * 
quantidade_feijao) + (açucar * quantidade_açucar) + (cafe * 
quantidade_cafe) + (sal * quantidade_sal) + (macarrao * 
quantidade_macarrao) +  (leite * quantidade_leite)

print(f"O preço total da compra é: R$, {preco_total:.2f}")


