#Modules
import turtle
import time
import random

posponer = 0.1

#Marcador
score = 0
high_score = 0

#Ventana
wn = turtle.Screen()
wn.title("Juego de Pong")
wn.bgcolor("deepskyblue")
wn.setup(width = 600, height = 600)
wn.tracer(0)

#Cuerpo tortuga
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("turtle")
cabeza.color("limegreen")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Pizza
pizza = turtle.Turtle()
pizza.speed(0)
pizza.shape("triangle")
pizza.color("orange")
pizza.penup()
pizza.goto(0,100)


#Tortugas
segmentos = []

#Score
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0        Hight Score: 0", align = "center", font = ("Corier", 25, "normal"))

#Funciones
def arriba():
   cabeza.direction = "up"
def abajo():
   cabeza.direction = "down"
def izquierda():
   cabeza.direction = "left"
def derecha():
   cabeza.direction = "right"

def mov():
   if cabeza.direction == "up":
       y = cabeza.ycor()
       cabeza.sety(y + 20)
   if cabeza.direction == "down":
       y = cabeza.ycor()
       cabeza.sety(y - 20)
   if cabeza.direction == "left":
       x = cabeza.xcor()
       cabeza.setx(x - 20)
   if cabeza.direction == "right":
       x = cabeza.xcor()
       cabeza.setx(x + 20)

#teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

while True:
   wn.update()
   #Colisiones bordes
   if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
       time.sleep(1)
       cabeza.goto(0,0)
       cabeza.direction = "stop"

       #Econder segmentos
       for segmentos in segmentos:
           segmentos.goto(1000,1000)

       #limpiar lista de segmentos
       segmentos.clear()

       #resetear marcador1
       score = 0
       texto.write("Score: {}        Hight Score: {}".format(score, high_score), align="center",
                   font=("Corier", 25, "normal"))

   if cabeza.distance(pizza) < 20:
       x = random.randint(-200, 280)
       y = random.randint(-200, 280)
       pizza.goto(x,y)

       new_seg = turtle.Turtle()
       new_seg.speed(0)
       new_seg.shape("turtle")
       new_seg.color("greenyellow")
       new_seg.penup()
       segmentos.append(new_seg)

       #Aumentar marcador
       score += 1

       if score > high_score:
           high_score = score

       texto.clear()
       texto.write("Score: {}        Hight Score: {}".format(score, high_score), align = "center", font = ("Corier", 25, "normal"))

   #Mover el cuerpo de la tortuga2
   totalSeg = len(segmentos)
   for index in range(totalSeg -1, 0, -1):
       x = segmentos[index - 1].xcor()
       y = segmentos[index - 1].ycor()
       segmentos[index].goto(x,y)

   if totalSeg > 0:
       x = cabeza.xcor()
       y = cabeza.ycor()
       segmentos[0].goto(x,y)

   mov()

   #Colisiones con las tortugas
   for segmento in segmentos:
       if segmento.distance(cabeza) < 20:
           time.sleep(1)
           cabeza.goto(0,0)
           cabeza.direction = "stop"

           #Esconder los segmentos
           for segmento in segmentos:
               segmento.goto(2000,2000)

           segmentos.clear()

           # resetear marcador2
           score = 0
           texto.write("Score: {}        Hight Score: {}".format(score, high_score), align="center",
                       font=("Corier", 25, "normal"))

   time.sleep(posponer)
