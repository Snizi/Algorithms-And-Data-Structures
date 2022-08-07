from tabelas import Tabelas

t = Tabelas(5)

t.insert("primeiro", "carro1")
t.insert("segundo", "carro2")
t.insert("terceiro", "carro3")
t.insert("quarto", "carro4") 
t.insert("quinto", "carro5")


t.remove("segundo")

print(t)


