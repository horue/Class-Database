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
    if option.lower() == ("buscar") or option.lower() == ('busca'):
        buscar()
    elif option.lower() == ('adicionar aluno') or option.lower() == ('adicionar'):
        aluno()
    elif option.lower() ==  ('ajuda'):
        ajuda()
    elif option.lower() == ("sair"):
        sys.exit
    elif option.lower() == ("admin"):
        login()
    while option.lower() not in ['buscar', 'busca', 'adicionar aluno', 'adicionar', 'ajuda', 'sair', 'admin']:
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
    if option.lower() ==  ('mais'):
        wb.open('https://github.com/horue')
        principal()
    if option.lower() == ('voltar'):
        principal()
    while option.lower() not in ['mais', 'voltar']:
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
    print('# Class Database - Tela Inicial #')
    print('# Bem vindo à Class Database! #')
    print("#" * 35)
    print('— Buscar na Base de Dados')
    print('— Adicionar Aluno')
    print('— Ajuda')
    print('— Sair')
    print('Feito por horue.')
    principal_menu()


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
    print('# Class Database - Tela de Ajuda #')
    print("#" * 35)
    print('— Use comandos para acessar, alterar ou apagar dados no banco de dados.')
    print("— Caso ainda tenha alguma dúvida, use o comando 'Mais' para ser redirecionado à docmuentação do programa.")
    print("— Para voltar à tela anterior, use o comando 'Voltar'.")
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