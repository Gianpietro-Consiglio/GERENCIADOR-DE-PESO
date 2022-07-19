import time
import os

def horas():
    hora = time.strftime('%d-%m-%Y %H:%M:%S')
    return hora

def send_to_txt(msg):
    os.chdir(r"D:\\Projeto Fitness\\")
    log = open('log.txt', 'a')
    hora = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
    log.write(f'{hora} -> {msg}\n')
    log.close()
