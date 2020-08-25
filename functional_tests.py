from selenium import webdriver

browser = webdriver.Firefox()

# Edith ouviu falar de uma nova aplicação online interessante para
# lista de tarefas. Ela decide verificar sua homepage
browser.get('http://localhost:8000')

# Ela percebe que o título da página e o cabeçalho mencionam listas de
# tarefas (to-do)
assert 'To-Do' in browser.title

# Ela é convidada a inserir um item de tarefa imediatamente

# Ela digita "Buy peacock feathers" (Comprar penas de pavão) em uma caixa
# de texto (o hobby de Edith é fazer iscas para pesca com fly)
