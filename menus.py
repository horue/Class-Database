import webbrowser as wb
import sqlite3
import sys
import os
from psw import senha


connection=sqlite3.connect("class.db")

cursor=connection.cursor()

#cursor.execute("CREATE TABLE Alunos (Nome TEXT, Curso TEXT, Matrícula INTERGER)")


v = ('0.1.1')


## Menus Functions ##


def principal_menu():
    option=input("> ")
    if option.lower() == ("buscar") or option.lower() == ('busca'):
        busca()
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





def busca_menu():
    option=input("> ")
    if option.lower() == ("matrícula"):
        busca_mat()
    elif option.lower () == ("nome"):
        busca_nome()
    elif option.lower() == ("curso"):
        busca_curso()
    while option.lower() not in ['matrícula', 'nome', 'curso']:
        print('Por favor, entre um comando válido.')
        option=input("> ")

def busca_mat_menu():
    print('Insira a matrícula que será buscada')
    mat=input("> ")
    busca=cursor.execute(f'SELECT * FROM Alunos WHERE Matrícula = {mat}')
    final_busca=busca.fetchone()
    print(final_busca)
    r=input('Deseja buscar outro aluno por matrícula? (S/N) ')
    if r == "S" or r == "s":
        busca_mat()
    elif r == 'N' or r == 'n':
        r2=input('Deseja voltar à tela inicial? (S/N) ')
        if r2 == 'S' or r2 == "s":
            principal()
    return

def busca_nome_menu():
    print('Insira o nome que será buscado')
    nome=str(input("> "))
    busca=cursor.execute(f'SELECT * FROM Alunos WHERE Nome = "{nome}"')
    print(busca)
    r=input('Deseja buscar outro aluno por nome? (S/N) ')
    if r == "S" or r == "s":
        busca_nome()
    elif r == 'N' or r == 'n':
        r2=input('Deseja voltar à tela inicial? (S/N) ')
        if r2 == 'S' or r2 == "s":
            principal()
    return

def busca_curso_menu():
    print('Qual curso você deseja ver os alunos?')
    curso=input("> ")
    busca=cursor.execute(f'SELECT * FROM Alunos WHERE Curso = "{curso}"')
    final_busca=busca.fetchone()
    print(final_busca)
    r=input('Deseja buscar outro curso? (S/N) ')
    if r == "S" or r == "s":
        busca_curso()
    elif r == 'N' or r == 'n':
        r2=input('Deseja voltar à tela inicial? (S/N) ')
        if r2 == 'S' or r2 == "s":
            principal()
    return









def add_aluno():
    nome=input("Nome do aluno: ")
    curso=input("Curso do aluno: ")
    mat=input("Matrícula do aluno: ")
    cursor.execute(f"INSERT INTO Alunos VALUES ('{nome}', '{curso}', {mat})")
    connection.commit()
    print('Aluno adicinado com sucesso!')
    r=input('Deseja registrar outro aluno? (S/N) ')
    if r == "S" or r == "s":
        aluno()
    elif r == 'N' or r == 'n':
        r2=input('Deseja voltar à tela inicial? (S/N) ')
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


## General Menus ##


def principal():
    os.system('cls')
    print("#"*len('# Class Database - Tela Inicial #'))
    print('# Class Database - Tela Inicial #')
    print('# Bem vindo à Class Database!   #')
    print("#"*len('# Class Database - Tela Inicial #'))
    print('— Buscar na Base de Dados')
    print('— Adicionar Aluno')
    print('— Ajuda')
    print('— Sair')
    print('Feito por horue.')
    principal_menu()

def busca():
    os.system('cls')
    print("#" * 35)
    print('# Class Database - Tela de Busca #')
    print('# De que forma você gostaria de buscar? #')
    print("#" * 35)
    print("Busca por matrícula")
    print("Busca por nome")
    print("Busca por curso")
    busca_menu()

def busca_mat():
    os.system('cls')
    print("#" * 35)
    print('# Class Database - Tela de Busca #')
    print('# Busca por Matrícula #')
    print("#" * 35)
    busca_mat_menu()

def busca_nome():
    os.system('cls')
    print("#" * 35)
    print('# Class Database - Tela de Busca #')
    print('# Busca por Nome #')
    print("#" * 35)
    busca_nome_menu()

def busca_curso():
    os.system('cls')
    print("#" * 35)
    print('# Class Database - Tela de Busca #')
    print('# Busca por Curso #')
    print("#" * 35)
    busca_curso_menu()


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



## Admin Screen ##

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
    
