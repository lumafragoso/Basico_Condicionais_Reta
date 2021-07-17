import turtle
cor = str(input('Escolha uma cor: (1) Azul, (2) Vermelho ou (3) Verde'))
tam = int(input("Escolha um tamanho para a reta:"))
t = turtle.Turtle()
t.pensize(10)
if cor == 1:
    t.color("blue")
elif cor == 2:
    t.color("red")
elif cor == 3:
    t.color("green")
t.forward(tam)
