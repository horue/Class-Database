import webbrowser as wb
import sqlite3
import sys
import os


connection=sqlite3.connect("class.db")

cursor=connection.cursor()

#cursor.execute("CREATE TABLE Alunos (Nome TEXT, Curso TEXT, Matrícula INTERGER)")




def principal_menu():
    option=input("> ")
    if option.lower() == ("buscar"):
        buscar()
    elif option.lower() == ('adicionar aluno'):
        aluno()
    elif option.lower() ==  ('ajuda'):
        ajuda()
    elif option.lower() == ("sair"):
        sys.exit
    while option.lower() not in ['buscar', 'adicionar aluno', 'ajuda', 'sair']:
        print("Por favor, entre um comando válido.")
        option=input("> ")


def add_aluno():
    nome=input("Nome do aluno: ")
    curso=input("Curso do aluno: ")
    mat=input("Matrícula do aluno: ")
    cursor.execute(f"INSERT INTO Alunos VALUES ('{nome}', '{curso}', {mat})")
    print('Aluno adicinado com sucesso!')
    r=input('Deseja voltar para a tela incial? (S/N) ')
    if r == "S" or r == "s":
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


    
def principal():
    os.system('cls')
    print("#" * 35)
    print('# Class Database - Tela Inicial #')
    print('# Bem vindo à Class Database! #')
    print("#" * 35)
    print('— Buscar Aluno')
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
