import turtle
from turtle import *
import random
import time
import keyboard as kb


class MyTurtle(turtle.Turtle):                                         #A 'Turtle' osztályt leszármaztatom az én osztályomnak,
    def __init__(self, color, shapesize, xpoz, name):                  #hogy példányosításkor gyorsabban be lehessen állítani
        super().__init__(shape='turtle')                               #a teknős tulajdonságait.
        self.speed(7)
        self.color(color)
        self.shapesize(shapesize)
        self.left(90)
        self.penup()
        self.goto(xpoz, -220)                           #xpoz - X tengelyen a poz beállítása.
        self.pendown()
        self.name = name


def line():                                             #A célvonal kirajzolása.
    turtle.pensize(2)
    turtle.setpos(-200, 190)
    turtle.pendown()
    turtle.forward(400)


def finish_line_txt():                                  #A célvonal szövegének kirajzolása.
    turtle.hideturtle()
    turtle.speed(0)
    turtle.color("Black")
    turtle.penup()
    turtle.setpos(-110, 130)
    turtle.pendown()
    turtle.write("FINISH LINE", font=("Arial", 30, "bold"))
    turtle.penup()


def starting_positions():                       #A rajtrácsszámok kirajzolása 'while' ciklussal.add()
    xpos = -240                                         #Azért '-240'-től indul, mert azt akartam, hogy ua.
    i = 0                                               #legyen a távolság minden versenyző közöttt, így
    while (i < 4):                               #így +90-el lépegetek a szám kiíráskor, balról-jobbra.
        xpos += 90
        turtle.penup()
        turtle.setpos(xpos, -270)
        turtle.pendown()
        turtle.write((i+1), font=("Arial", 15, "bold"))
        turtle.penup()
        i += 1


def rand_color(number):                                 #Véletlenszerű színgenerálás. Setbe lett felvéve 4 db szín,
    color_set = {"pink", "red", "blue", "green"}        #ami utána egy listának adok át, mert a setből nem lehet
    color_array = []                                    #kiolvastatni, de a set arra jó, hogy a listába mindig
    for i in color_set:                                 #random tegye át. Utána a listából mindig egy fix indexű
        color_array.append(i)                           #elemet kap egy versenyző, pl.: Az első versenyző mindig a 0.
    return color_array[number]                          #de a színek persze mindig változnak.


def results(finish_arr, timelist):                                #A végeredmény, helyezés+név kiíratása. Hasonló a rajtszámok
    i = 0                                               #kirajzolásához, úgyhogy ide már nem írom le.
    ypos = 80
    while (i < 4):
        ypos -= 20
        turtle.penup()
        turtle.setpos(180, ypos)
        turtle.pendown()
        turtle.write("{0}. helyezett: {1}\t  Idő: {2} sec\n".format(
            i+1, finish_arr[i], timelist[i], font=("Arial", 10, "bold")))
        i += 1


def window():                                           #Az ablak megrajzolása.
    wn = turtle.Screen()
    wn.bgcolor("#9999ff")
    wn.title("Turtle Race")
    root = turtle.Screen()._root
    root.iconbitmap("turtle.ico")


def play():

    try:

        # Teknősök
        turtlelist = []
        timelist = []
        turtlelist.append(MyTurtle(rand_color(0), 2, -150, "Tomi")) #Versenyzők példányosítása.
        turtlelist.append(MyTurtle(rand_color(1), 2, -60, "Noémi"))
        turtlelist.append(MyTurtle(rand_color(2), 2, 30, "Evelin"))
        turtlelist.append(MyTurtle(rand_color(3), 2, 120, "Dávid"))

        state = True
        finish_arr = []
        start = time.time()                                         #Idő példányból létrehoztam egyet, ami elkezd számolni
        while (state):                                              #Amíg nem érik el a cél, addig véletlenszerűen,
            xpos = -240                                             #mindig másmekkora szám lesz a 'sebességük'.
            for i in range(len(turtlelist)):                        #Emiatt szoros verseny lesz.
                xpos += 90                                          #Amint valaki beér a célba, megáll, a neve be-
                if (turtlelist[i].pos() < (xpos, 215)):             #kerül egy listába, és a végeredménynél lesz
                    turtlelist[i].forward(random.randint(1, 12))    #kiolvasva onnan.
                else:
                    stop = time.time()
                    turtlelist[i].penup()
                    if turtlelist[i].name not in finish_arr:
                        finish_arr.append(turtlelist[i].name)
                        timelist.append(round(stop-start, 2))       #Amikor egy teknős beér, akkor annak az idejét egy listába dobom, tovább adom a 'results'nak, majd ott kiíródik.

            if(len(finish_arr) == 4):                               #Ha mindenki benne van, kilép a ciklusból.
                state = False
                
        results(finish_arr, timelist)                                         #Átadja a listát az eljárásnak.
        turtle.done()

    except Exception as e:
        print("Váratlan hiba történt, a program futása megszakadt! Hiba kód: {0}" .format(str(e)))


def main():
    window()
    finish_line_txt()
    starting_positions()
    line()
    play()


if __name__ == "__main__":
    main()
