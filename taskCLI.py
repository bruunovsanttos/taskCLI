import os
import json
import argparse
from datetime import datetime


#formato_hora = hora_momento.strftime("%dd %mm %yy %H:%M")
def data_atual():
    data = datetime.now()
    data_formatada = data.strftime("%d/%m/%y %H:%M:%S")
    return data_formatada

def add_tarefa(descricao):
    if os.path.exists(caminho_arquivo):
        with open("task.json", "r", encoding="utf-8") as arquivo:
            tarefas = json.load(arquivo)

    else:
        tarefas = []

    proximo_id = len(tarefas) + 1
    descricao = input("Digite aqui a tarefa que você deseja marcar: ")

    nova_tarefa= {
        "id": proximo_id,
        "descrição" :descricao,
        "status": "a fazer",
        "início": data_atual(),
        "modificado": data_atual()
    }

    tarefas.append(nova_tarefa)

    with open ("task.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4)

    print(f"Você adicionou uma nova tarefa ID: {nova_tarefa["id"]}, Descrição: {nova_tarefa["descrição"]}")

def alterar_tarefa():
    pass

def tarefa_em_processo():
    pass

def terminar_tarefa():
    pass

def mostrar_tarefas():
    if os.path.exists(caminho_arquivo):
        with open("task.json", "r", encoding="utf-8") as arquivo:
            tarefas = json.load(arquivo)

            if tarefas is None:
                print("você aind anão adicionou nenhuma tarefa")

    #elif se tarefas exixtir fazer isso:

        for tarefa in tarefas:
            print(tarefa["id"], tarefa["descrição"], tarefa["status"], tarefa["início"])


#formato_hora = hora_momento.strftime("%dd %mm %yy %H:%M")

#as para nomear o arquivo como quiser

#with open("task.json", "w", encoding="utf-8") as arquivo:
#    tarefas = json.load(arquivo)
diretorio = "C:/Users/bruvieira/Desktop/Nova_pasta/taskCLI/task.json"
nome_arquivo = "task.json"
caminho_arquivo = os.path.join(diretorio, nome_arquivo)

def main():
    parser = argparse.ArgumentParser(description="Gerenciador de tarefas CLI")
    subparsers = parser.add_subparsers(dest="comando")


    parser_add = subparsers.add_parser("add", help="Adicionar uma nova tarefa")
    parser_add.add_argument("descricao", type=str, help="Descrição de tarefa")

    parser_add = subparsers.add_parser("mostrar", help="Mostrar todas as tarefas")
    parser_add.add_argument("mostrar", type=str, help="Mostrar tarefas")

    args = parser.parse_args()

    if args.comando == "add":
        add_tarefa(args.descricao)
    elif args.comando == "mostrar":
        mostrar_tarefas()


if __name__ == "__main__":
    main()
    


