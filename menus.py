import webbrowser as wb
import sqlite3
import sys
import os


def princiapl_menu():
    option=input("> ")
    if option.lower() ==("buscar"):
        sys.exit #start_game()
    elif option.lower() == ("Adicionar Aluno"):
        aajuda()
    elif option.lower() ==  ('ajuda'):
        ajuda()
    elif option.lower() == ("sair"):
        sys.exit
    while option.lower() not in ['buscar', 'adicionar aluno', 'ajuda', 'sair']:
        print("Por favor, entre um comando válido.")
        option=input("> ")
        return

def ajuda_menu():
    option=input("> ")
    if option.lower() ==  ('mais'):
        wb.open('https://github.com/horue')
    while option.lower() not in ['mais']:
        print('Por favor, entre um comando válido. ')
        option=input("> ")
        return





    
def principal():
    print("#" * 30)
    print('# Bem vindo à Class Database! #')
    print("#" * 30)
    print('Buscar Aluno')
    print('Adicionar Aluno')
    print('Ajuda')
    print('Sair')
    print('Feito por horue.')
    princiapl_menu()


def ajuda():
    print("#" * 30)
    print('# Class Database - Tela de Ajuda #')
    print("#" * 30)
    print('— Use comandos para acessar, alterar ou apagar dados no banco de dados.')
    print("— Caso ainda tenha alguma dúvida, use o comando 'Mais' para ser redirecionado à docmuentação do programa.")
    print('Made by horue.')
    ajuda_menu()
    return(principal)
