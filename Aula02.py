# para eu instalar uma biblioteca eu uso: pip install <nome_biblioteca>

#para eu impportar uma biblioteca eu uso import <nome_biblioteca>
#o as eu coloco apelido

import numpy as np
import time
import pandas
import pyautogui as py


#vamos fazer um programa para realizar raiz quadrada de um número

# as metodo é uma ação de objeto

#inpút é o metodo para apessoa digitr
#print é o metodo para receber os valores digfitados ou calculados.

# todo metodo ele fica com () e dentro dos "()" tudo que é colocado se chama parametro que são valores que o meoodo recebe para realizar u ação.

#numero = int(input())
#time.sleep(5)
#resultado = float(np.sqrt(numero))

#print(resultado)


#quero abrir o navegador automaticamente.

#py.press('win')
#time.sleep(2)
#py.write('edge')
#py.press('enter')
#time.sleep(5)
#print(py.position())
#py.click(x=84, y=13)

#numeros = [1,33,3,10,34,544]
#print(numeros[2])
#for i in range(6):
#"i" representa posicao de um dado dentro deu um vetor(por exemplo)
#    print(numeros[i])
#nomes = {"julia":"nome_feminino","henrique":"nome_masculino"}
#nomes.pop("julia")
#print(nomes)
numeros = []
for i in range(10000):
    if(i % 2 == 0):
        numeros.append(i)
        time.sleep(0.0005)
print(numeros)

