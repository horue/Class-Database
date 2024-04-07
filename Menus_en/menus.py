import webbrowser as wb
import sqlite3
import sys
import os
from psw import senha


connection=sqlite3.connect("class.db")

cursor=connection.cursor()

#cursor.execute("CREATE TABLE Alunos (Nome TEXT, Curso TEXT, Matrícula INTERGER)")




def principal_menu():
    option=input("> ")
    if option.lower() == ("search") or option.lower() == ('busca'):
        buscar()
    elif option.lower() == ('aadd student') or option.lower() == ('add'):
        aluno()
    elif option.lower() ==  ('help'):
        ajuda()
    elif option.lower() == ("exit"):
        sys.exit
    elif option.lower() == ("admin"):
        login()
    while option.lower() not in ['search', 'busca', 'add student', 'add', 'help', 'exit', 'admin']:
        print("Por favor, entre um comando válido.")
        option=input("> ")


def add_aluno():
    nome=input("Nome do aluno: ")
    curso=input("Curso do aluno: ")
    mat=input("Matrícula do aluno: ")
    cursor.execute(f"INSERT INTO Alunos VALUES ('{nome}', '{curso}', {mat})")
    print('Aluno adicinado com sucesso!')
    r=input('Deseja registrar outro aluno? (S/N) ')
    if r == "S" or r == "s":
        aluno()
    elif r == 'N' or r == 'n':
        r2=input('Deseja voltar à tela iniicla? (S/N) ')
        if r2 == 'S' or r2 == "s":
            principal()
    return


def ajuda_menu():
    option=input("> ")
    if option.lower() ==  ('more'):
        wb.open('https://github.com/horue')
        principal()
    if option.lower() == ('back'):
        principal()
    while option.lower() not in ['more', 'back']:
        print('Por favor, entre um comando válido. ')
        option=input("> ")
        return

def adm_menu():
    print('Entre a senha de administrador abaixo: ')
    psw=input('> ')
    if psw == senha:
        adm()
    else:
        os.system('cls')
        print('Senha incorreta. Aperte enter para voltar à tela inicial.')
        input('> ')
        principal()



def adm_scr():
    print('Entre o comando desejado')
    c=input('> ')
    cursor.execute(c)
    adm()



    
def principal():
    os.system('cls')
    print("#" * 35)
    print('# Class Database - Main Screen #')
    print('# Welcome to Class Database! #')
    print("#" * 35)
    print('— Search on Database')
    print('— Add Student')
    print('— Help')
    print('— Exit')
    print('Made by horue.')
    principal_menu()


def busca():
    os.system('cls')
    print("#" * 35)
    print('# Class Database - Tela de Busca #')
    print('# Aonde você gostaria de buscar? #')
    print("#" * 35)





def aluno():
    os.system('cls')
    print("#" * 35)
    print('# Class Database - Adicionando Aluno #')
    print("#" * 35)
    print("Entre as informações do Aluno a ser adicionado:")
    add_aluno()
    return(principal)




def ajuda():
    os.system('cls')
    print("#" * 35)
    print('# Class Database - Help Screen #')
    print("#" * 35)
    print('— Use commands to access, change or erase data.')
    print("— In case you need more help, use 'More' to see the documentation.")
    print("— To go back to main screen, use 'back'.")
    print('Made by horue.')
    ajuda_menu()
    return(principal)




def login():
    os.system('cls')
    print("#" * 35)
    print('# Class Database - Tela de Administrador #')
    print("#" * 35)
    adm_menu()

def adm():
    os.system('cls')
    print("#" * 35)
    print('# Área do Administrador #')
    print("#" * 35)
    adm_scr()