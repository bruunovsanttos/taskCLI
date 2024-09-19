import os
import json
import argaparse
from datetime import datetime

def data_atual():
    data = datetime.now()
    data_formatada = data.strftime("%d/%m/%y %H:%M:%S")
    print(data_formatada)

def add_tarefa():

    task= {
        "ID": 1,
        "descrição" :"",
        "status": "a fazer",
        "inicio": data_atual(),
        "modificado": data_atual()
    }

    with open ("task.json", "w", encoding="utf-8", indent=4) as arquivo:
        json.dump(arquivo)




def alterar_tarefa():
    pass

def tarefa_em_processo():
    pass

def terminar_tarefa():
    pass

def mostrar_tarefas():
    pass


#formato_hora = hora_momento.strftime("%dd %mm %yy %H:%M")

#as para nomear o arquivo como quiser

#with open("task.json", "w", encoding="utf-8") as arquivo:
#    tarefas = json.load(arquivo)


