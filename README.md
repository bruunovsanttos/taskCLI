# TaskCLI 📃
Criação de um todolist com comando via cmd  
Este projeto veio de uma ideia do [Roadmapsh](https://roadmap.sh/projects/task-tracker), o projeto consiste em ciar uma lista de tarefa com alguns obstaculos. 

## Ferramentas Do projeto 🔨🔧  
### Lingaugem de programação
#### Python 3.12  🐍
#### _*Bibliotacas Utilizadas*_ 📚

[Datetime](https://docs.python.org/pt-br/3/library/datetime.html) utilizado para a atualização de datas do programa nos prints de atualização e criação.


[OS](https://docs.python.org/pt-br/3/library/os.html#module-os) para manipulação de caminhos do programa e atualização de tarefas.  

[JSON](https://docs.python.org/pt-br/3/library/json.html) utilizada para a manipulação do arquivo que serve de base para as atualização, adições e terminos de tarefas.

[Argparse](https://docs.python.org/pt-br/3/library/argparse.html#module-argparse) a utilização dessa biblioteca consistem na maipulação correta dos argumentos dados pelo usuário do programa não havendo erros.  



## Definições do projeto  📏 📐

O projeto possui algumas particularidades, fazendo com que os ensinamentos basicos de python estejam sendo entregues.  
Seguem os requisitos do site rodmapsh para a criação do projeto:

>Requisitos:  
O aplicativo deve ser executado a partir da linha de comando, aceitar ações e entradas do usuário como argumentos e armazenar as tarefas em um arquivo JSON. O usuário deve ser capaz de:

>Adicionar, atualizar e excluir tarefas  
>Marcar uma tarefa como em andamento ou concluída  
Listar todas as tarefas  
Listar todas as tarefas que foram feitas  
Liste todas as tarefas que não foram feitas  
Listar todas as tarefas em andamento  
 

>Aqui estão algumas restrições para orientar a implementação:    
Você pode usar qualquer linguagem de programação para construir este projeto.  
Use argumentos posicionais na linha de comando para aceitar entradas do usuário.  
Use um arquivo JSON para armazenar as tarefas no diretório atual.
O arquivo JSON deve ser criado se não existir.  
Use o módulo do sistema de arquivos nativo da sua linguagem de programação para interagir com o arquivo JSON.  
Não use nenhuma biblioteca ou estrutura externa para construir este projeto.  
Certifique-se de lidar com erros e casos extremos com elegância.

  


## Utilizando o projeto  💾

1. Para utilizar o projeto você deve clonar este repositório no seu computador utilizando o link HTTPS clicando em code e utilizando o comando  
`git clone https://github.com/user-attachments/assets/6fcf66e4-c5cb-48c0-81e7-835ea25bcc9a`.

    ![clonando repositório](https://github.com/user-attachments/assets/6fcf66e4-c5cb-48c0-81e7-835ea25bcc9a)   


2. Apos isso você deve abrir seu prompt de comando para rodar o projeto apertando juntamente os botôes  
   ![image](https://github.com/user-attachments/assets/edd37825-1b68-49ba-8902-897f075d02a3) 
   ![image](https://github.com/user-attachments/assets/62d7e0e4-c61a-47e3-8d3c-70f06408af72)



3. Para rodar o programa você pode arratar para dentro da sua linha de comando o arquivo `taskCLI.py` que vai lhe dar o caminho do programa ou inserir o caminho manualmente (recomendo a primeira opção)


4. Os comandos para rodar o programa são: 
### add "tarefa"
      para adicionar alguma tarefa a ser feita 

![image](https://github.com/user-attachments/assets/41571e39-c4d4-4325-98bd-41cba94a107c)
### mostrar "tarefa"
      aqui você terá a opção de mostrar todas as tarefas, apenas tarefas
      a fazer, apenas tarefas fazendo, apenas tarefas terminadas selecionando o número que deseja. 
![image](https://github.com/user-attachments/assets/c7f5b000-e8ac-4cc0-ad27-f4163d969ef9)

### deletar 'id'
      Nesta função caso ocorra algum erro você pdoe deletar a tarefa pelo seu numero de 'id'.

![image](https://github.com/user-attachments/assets/d0601309-f0b9-4f26-993b-159ef024a04b)
### fazendo 'id'
      Aqui você podera alterar o status da tarefa para fazendo

![image](https://github.com/user-attachments/assets/0cafa168-6c2d-4fff-a934-0ea26ba23e45)
### terminar 'id'
      Nesta função você poderá atualizar o status de uma tarefa para terminada

![image](https://github.com/user-attachments/assets/5837fb20-79ef-4b25-baa3-79f8c1385e0d)
### alterar 'id'
      Função para alterar descrição de tarefa.

![image](https://github.com/user-attachments/assets/cafe1d14-81ab-4598-8d07-321deeddf6b4)
      



