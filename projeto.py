#with open('arquivo.txt', 'r', encoding='utf-8') as file:
  #  conteudo = file.read()
  #  print(conteudo)


#with open('arquivo.txt','r', encoding='utf-8') as file:
 #   for linha in file:
       # print(linha)

#with open('arquivo.txt', 'r', encoding='utf-8') as file:
#        for linha in file:
#         print(linha.rstrip())


with open('arquivo.txt','r', encoding='utf-8') as arquivo:
    linhas = arquivo.readline()


print(f'o tipo de linhas é : {type(linhas)}')
print(f'a quantidade de linhas é : {len(linhas)}')