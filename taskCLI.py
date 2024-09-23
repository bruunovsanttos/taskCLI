import os
import json
import argparse
from datetime import datetime

def data_atual():
    data = datetime.now()
    data_formatada = data.strftime("%d/%m/%y %H:%M:%S")
    print(data_formatada)

def add_tarefa():

    nova_tarefa= {
        "ID": 1,
        "descrição" :"",
        "status": "a fazer",
        "inicio": data_atual(),
        "modificado": data_atual()
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


