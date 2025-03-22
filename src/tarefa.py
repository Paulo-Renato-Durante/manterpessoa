
tarefas = []

def remover_tarefa(nome_tarefa):
    
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if tarefa != nome_tarefa]


tarefas = ["Tarefa 1", "Tarefa 2", "Tarefa 3"]
remover_tarefa("Tarefa 2")
print(tarefas) 