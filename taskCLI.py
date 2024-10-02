import os
import json
import argparse
from datetime import datetime


#formato_hora = hora_momento.strftime("%dd %mm %yy %H:%M")
def data_atual():
    data = datetime.now()
    data_formatada = data.strftime("%d/%m/%y %H:%M:%S")
    return data_formatada

def add_tarefa():
    if os.path.exists("task.json"):
        with open("task.json", "r", encoding="utf-8", indent=4) as arquivo:
            tarefas = json.load(arquivo)

    else:
        tarefas = []

    proximo_id = len(tarefas) + 1
    descricao = input("Digite aqui a tarefa que você deseja marcar: ")

    nova_tarefa= {
        "ID: ": proximo_id,
        "Descrição: " :descricao,
        "Status: ": "a fazer",
        "Início: ": data_atual(),
        "Modificado em : ": data_atual()
    }


    with open ("task.json", "w", encoding="utf-8", indent=4) as arquivo:
        json.dump(nova_tarefa, arquivo)

    print(f"Você adicionou uma nova tarefa (ID: {nova_tarefa["id", "descrição"]}")




def alterar_tarefa():
    pass

def tarefa_em_processo():
    pass

def terminar_tarefa():
    pass

def mostrar_tarefas():
    pass

def criar_id():
    pass

#formato_hora = hora_momento.strftime("%dd %mm %yy %H:%M")

#as para nomear o arquivo como quiser

#with open("task.json", "w", encoding="utf-8") as arquivo:
#    tarefas = json.load(arquivo)


