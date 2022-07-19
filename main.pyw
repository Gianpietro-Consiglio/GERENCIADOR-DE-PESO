import PySimpleGUI as psg
import sqlite3
import os
import telas
import funcoes

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
    cursor.execute("CREATE TABLE MeuPeso(id integer primary key, peso int, altura int, imc int, data_cadastro text)")
    banco.commit()
    cursor.execute("CREATE TABLE MinhaAgua(id integer primary key, agua int, data_cadastro text)")
    banco.commit()
except:
    pass

janela1,janela2,janela = telas.Tela_Principal(),None,None

while True:
    window,event,values = psg.read_all_windows()
    if window == janela1 and event == psg.WIN_CLOSED:
        break
    elif window == janela1 and event == 'Inserir dados do dia':
        janela2 = telas.Tela_Dados()
        janela1.close()
    elif window == janela2 and event == 'Voltar':
        janela2.close()
        janela1 = telas.Tela_Principal()    
    elif window == janela2 and event == psg.WIN_CLOSED:
        break    
    elif window == janela2 and event == 'Cadastrar':
        peso = values['peso']
        altura = values['altura']
        try:
            peso = float(peso)
            altura = float(altura)
        except Exception as erro:
            funcoes.send_to_txt(erro)
            psg.popup('Erro na conversão de valores!')   
            continue
        try:
            imc = peso / (altura * altura)
        except Exception as erro:
            funcoes.send_to_txt(erro)
            psg.popup("Erro ao calcular imc!")
            continue    
        
        resultado = funcoes.horas()
        try:
            cursor.execute(F"INSERT INTO MeuPeso(peso,altura,data_cadastro,imc) VALUES({peso},{altura},'{resultado}',{imc})")  
        except Exception as erro:
            funcoes.send_to_txt(erro)
            psg.popup('ERRO AO ENVIAR DADOS!')    
            continue  
        else:
            banco.commit()
            psg.popup('Dados enviados!')

    elif window == janela1 and event == 'Ver informações':
        janela1.close()
        janela3 = telas.Tela_Informacoes()

    elif janela3 and event == 'Voltar':
        janela3.close()
        janela1 = telas.Tela_Principal()
    elif janela3 and event == psg.WIN_CLOSED:
        break      
    elif janela3 and event == 'Buscar':
        window['mensagem'].update('')
        altura1 = []
        peso1 = []
        data1 = []
        imc1 = []
        try:
            cursor.execute("SELECT peso FROM MeuPeso")
            peso = cursor.fetchall()
            cursor.execute("SELECT data_cadastro FROM MeuPeso")
            data = cursor.fetchall()
            cursor.execute("SELECT imc FROM MeuPeso")
            imc = cursor.fetchall()
            cursor.execute("SELECT altura FROM MeuPeso")
            altura = cursor.fetchall()
        except Exception as erro:
            psg.popup('Erro ao buscar informações!')   

        for x in peso:
            peso1.append(x)
        for x in data:
            data1.append(x)
        for x in altura:
            altura1.append(x)
        for x in imc:
            imc1.append(x)    
  
        cont = - 1
        try:
            while True:
                cont += 1
                peso = str(peso1[cont]).replace("[","").replace("]","").replace("(","").replace(")","").replace(",","").replace("'","")       
                data = str(data1[cont]).replace("[","").replace("]","").replace("(","").replace(")","").replace(",","").replace("'","")   
                altura = str(altura1[cont]).replace("[","").replace("]","").replace("(","").replace(")","").replace(",","").replace("'","")   
                imc = str(imc1[cont]).replace("[","").replace("]","").replace("(","").replace(")","").replace(",","").replace("'","")      
                imc_transform = float(imc)           
                print(F"Peso: {peso}")
                print(F"Altura: {altura}")
                try:
                    if imc_transform < 18.5:
                        print(f"IMC: {imc_transform:.1f} [{'Abaixo do peso'}]")
                    elif imc_transform < 24.9:
                        print(f"IMC: {imc_transform:.1f} [{'Peso normal'}]") 
                    elif imc_transform < 29.9:
                        print(f"IMC: {imc_transform:.1f} [{'Sobrepeso'}]")    
                    elif imc_transform < 34.9:
                        print(f"IMC: {imc_transform:.1f} [{'Obesidade Grau 1'}]")     
                    elif imc_transform < 39.9:
                        print(f"IMC: {imc_transform:.1f} [{'Obesidade Grau 2'}]")   
                    else: 
                        print(f"IMC: {imc_transform:.1f} [{'Obesidade Grau 3'}]") 

                except Exception as erro:
                    psg.popup(erro)
                    funcoes.send_to_txt(erro)        

                print(F"Cadastro: {data}") 
                print('')
                print('')
                

        except Exception as erro:
            print(F'Total de dados carregados: {cont}')
            pass
            funcoes.send_to_txt(erro)
            
   