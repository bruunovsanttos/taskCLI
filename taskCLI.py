import os
import json
import argparse
from datetime import datetime


#formato_hora = hora_momento.strftime("%dd %mm %yy %H:%M")

def abrir_json():
    if os.path.exists(caminho_arquivo):
        with open("task.json", "r", encoding="utf-8") as arquivo:
            tarefas = json.load(arquivo)


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

    #precisa ajustar esse contatador ta criando numero repetido
    proximo_id = len(tarefas) + 1
    descricao = input("Digite aqui a tarefa que você deseja marcar: ")

    nova_tarefa = {
        "id": proximo_id,
        "descrição": descricao,
        "status": "a fazer",
        "início": data_atual(),
        "modificado": data_atual()
    }

    tarefas.append(nova_tarefa)

    with open("task.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4)

    print(f"Você adicionou uma nova tarefa ID: {nova_tarefa['id']}, Descrição: {nova_tarefa['descrição']}")


def deletar_tarefa():
    if os.path.exists(caminho_arquivo):
        with open("task.json", "r", encoding="utf-8") as arquivo:
            tarefas = json.load(arquivo)

    else:
        print("Arquivo de tarefas não encontrado")

    id_tarefa = int(input("Qual tarefa você deseja deletar (ID): "))

    for tarefa in tarefas:

        if tarefa['id'] == id_tarefa:
            tarefas.remove(tarefa)
            print(f"Tarefa ID: {id_tarefa} deletada com sucesso.")
            break

    else:
        print("tarefa com Id não encontrada")

    with open("task.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4)


def tarefa_em_processo(id_tarefa):
    if not os.path.exists(caminho_arquivo):
        print("Arquivo de tarefas não encontrado.")
        return

    with open("task.json", "r", encoding="utf-8") as arquivo:
        tarefas = json.load(arquivo)



    tarefa_encontrada = False

    for tarefa in tarefas:
        if tarefa['id'] == id_tarefa:
            tarefa['status'] = "em progresso"
            tarefa['modificado'] = data_atual()
            tarefa_encontrada = True
            print(f"Tarefa ID: {tarefa['id']} atualizada como em processo.")
            break

    if not tarefa_encontrada:
        print("Tarefa não encontrada.")


    with open("task.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4)


def terminar_tarefa():
    pass


def mostrar_tarefas():
    if os.path.exists(caminho_arquivo):
        with open("task.json", "r", encoding="utf-8") as arquivo:
            tarefas = json.load(arquivo)

            if not tarefas:
                print("você ainda não adicionou nenhuma tarefa")
            else:
                for tarefa in tarefas:
                    print(f"\n ID: {tarefa["id"]}, \n Descrição: {tarefa["descrição"]},\n Status: {tarefa["status"]},\n Data de início: {tarefa["início"]},\n Modificado em: {tarefa['modificado']}")

    else:
        print("Arquivo de tarefas não encontrado")


#formato_hora = hora_momento.strftime("%dd %mm %yy %H:%M")

#as para nomear o arquivo como quiser

#with open("task.json", "w", encoding="utf-8") as arquivo:
#    tarefas = json.load(arquivo)
diretorio = "C:/Users/bruvieira/Desktop/Nova_pasta/taskCLI"
nome_arquivo = "task.json"
caminho_arquivo = os.path.join(diretorio, nome_arquivo)


def main():
    parser = argparse.ArgumentParser(description="Gerenciador de tarefas CLI")
    subparsers = parser.add_subparsers(dest="comando")

    parser_add = subparsers.add_parser("add", help="Adicionar uma nova tarefa")
    parser_add.add_argument("descricao", type=str, help="Descrição de tarefa")

    parser_add = subparsers.add_parser("mostrar", help="Mostrar todas as tarefas")
    parser_add.add_argument("mostrar", type=str, help="Mostrar tarefas")

    parser_add = subparsers.add_parser("deletar", help="Deletar tarefas")
    parser_add.add_argument("id", type=int, help="ID da tarefa a ser deletada")

    parser_add = subparsers.add_parser("fazendo", help="colocar tarefa como fazendo")
    parser_add.add_argument("id", type=int, help="ID da tarefa a ser colocada em progresso")

    args = parser.parse_args()

    if args.comando == "add":
        add_tarefa(args.descricao)
    elif args.comando == "mostrar":
        mostrar_tarefas()
    elif args.comando == "deletar":
        deletar_tarefa(args.id)# Passando o ID para a função
    elif args.comando == "fazendo":
        tarefa_em_processo(args.id)# Passando o ID para a função


if __name__ == "__main__":
    main()
