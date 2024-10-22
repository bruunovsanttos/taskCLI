# TaskCLI
Criação de um todolist com comando via cmd  
Este projeto veio de uma ideia do [Roadmapsh](https://roadmap.sh/projects/task-tracker), o projeto consiste em ciar uma lista de tarefa com alguns obstaculos. 

## Definições do projeto  

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
> 

>Aqui estão algumas restrições para orientar a implementação:    
Você pode usar qualquer linguagem de programação para construir este projeto.  
Use argumentos posicionais na linha de comando para aceitar entradas do usuário.  
Use um arquivo JSON para armazenar as tarefas no diretório atual.
O arquivo JSON deve ser criado se não existir.  
Use o módulo do sistema de arquivos nativo da sua linguagem de programação para interagir com o arquivo JSON.  
Não use nenhuma biblioteca ou estrutura externa para construir este projeto.  
Certifique-se de lidar com erros e casos extremos com elegância.
>
>
  

### _*Bibliotacas Utilizadas*_

[Datetime](https://docs.python.org/pt-br/3/library/datetime.html) utilizado para a atualização de datas do programa nos prints de atualização e criação.


[OS](https://docs.python.org/pt-br/3/library/os.html#module-os) para manipulação de caminhos do programa e atualização de tarefas.  

[JSON](https://docs.python.org/pt-br/3/library/json.html) utilizada para a manipulação do arquivo que serve de base para as atualização, adições e terminos de tarefas.

[Argparse](https://docs.python.org/pt-br/3/library/argparse.html#module-argparse) a utilização dessa biblioteca consistem na maipulação correta dos argumentos dados pelo usuário do programa não havendo erros.  

