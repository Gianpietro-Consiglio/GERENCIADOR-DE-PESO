from doctest import testfile
import sqlite3
import _sqlite3
import os


try:
    os.mkdir(r"D:\\Projeto Fitness\\")
except:
    pass

try:
    os.chdir(r"D:\\Projeto Fitness\\")
except:
    pass

try:
    banco = sqlite3.connect('banco-fitness')
    cursor = banco.cursor()
except:
    print('erro')
else:
    cont = 0
    while True:
        cont +=1
        if cont == 10000000:
            break
        else:
            peso = 120
            altura = 210
            resultado = 'teste'
            imc = peso / (altura * altura)
            cursor.execute(F"INSERT INTO MeuPeso(peso,altura,data_cadastro,imc) VALUES({peso},{altura},'{resultado}',{imc})")  
            banco.commit()
            print(F'Dados enviados!{cont}')  

