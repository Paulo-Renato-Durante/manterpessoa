
lista_tarefas = []

def adicionar_tarefa(tarefa):
   
    lista_tarefas.append(tarefa)




def remover_tarefa(nome_tarefa):
    
    global lista_tarefas
    lista_tarefas = [tarefa for tarefa in lista_tarefas if tarefa != nome_tarefa]


lista_tarefas = ["Tarefa 1", "Tarefa 2", "Tarefa 3"]
remover_tarefa("Tarefa 2")
print(lista_tarefas) 