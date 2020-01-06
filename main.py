import turtle;import time
screen=turtle.Screen()
Turtle=turtle.Turtle()
Turtle.speed(0)
Turtle.ht()
Smooth=input("Do you want curvy letters? Y/N")
def A():
	Turtle.reset()
	Turtle.rt(-75);Turtle.fd(60);Turtle.rt(150);Turtle.fd(60);Turtle.rt(180);Turtle.fd(20);Turtle.rt(105);Turtle.fd(-20)
def B():
        if Smooth == 'Y':
            Turtle.reset()
            Turtle.rt(-90);Turtle.fd(60);Turtle.rt(90);Turtle.fd(15);Turtle.circle(-15,180);Turtle.fd(15);Turtle.fd(-15);Turtle.rt(180);Turtle.circle(-15,180);Turtle.fd(15)
        else:
            Turtle.reset()
            Turtle.rt(-90);Turtle.fd(60);Turtle.rt(90);Turtle.fd(15);Turtle.rt(45);Turtle.fd(20);Turtle.rt(45);Turtle.fd(15);Turtle.rt(45);Turtle.fd(5);Turtle.rt(45);Turtle.fd(25);Turtle.fd(-25);Turtle.rt(45);Turtle.fd(-5);Turtle.rt(45);Turtle.fd(-15);Turtle.rt(45);Turtle.fd(-15);Turtle.rt(45);Turtle.fd(-15)
def C():
        if Smooth == 'Y':
            Turtle.reset()
            Turtle.rt(180);Turtle.pu;Turtle.circle(-30,-30);Turtle.pd;Turtle.circle(-30,230)
        else:
            Turtle.reset()
            Turtle.fd(20);Turtle.rt(180);Turtle.fd(20);Turtle.rt(45);Turtle.fd(20);Turtle.rt(45);Turtle.fd(30);Turtle.rt(45);Turtle.fd(20);Turtle.rt(45);Turtle.fd(20)
def D():
        if Smooth == 'Y':
            Turtle.reset()
            Turtle.rt(-90);Turtle.fd(60);Turtle.rt(90);Turtle.fd(15);Turtle.circle(-30,180);Turtle.fd(15)
        else:
            Turtle.reset()
            Turtle.rt(-90);Turtle.fd(60);Turtle.rt(90);Turtle.fd(15);Turtle.rt(45);Turtle.fd(20);Turtle.rt(45);Turtle.fd(35);Turtle.rt(45);Turtle.fd(20);Turtle.rt(45);Turtle.fd(15)
def E():
	Turtle.reset()
	Turtle.fd(30);Turtle.rt(180);Turtle.fd(30);Turtle.rt(90);Turtle.fd(30);Turtle.rt(90);Turtle.fd(30);Turtle.rt(180);Turtle.fd(30);Turtle.rt(90);Turtle.fd(30);Turtle.rt(90);Turtle.fd(30)
def F():
	Turtle.reset()
	Turtle.rt(-90);Turtle.fd(30);Turtle.rt(90);Turtle.fd(30);Turtle.rt(180);Turtle.fd(30);Turtle.rt(90);Turtle.fd(30);Turtle.rt(90);Turtle.fd(30)
def G():
        if Smooth == 'Y':
            Turtle.reset()
            Turtle.fd(20);Turtle.circle(15,90);Turtle.fd(20);Turtle.rt(90);Turtle.fd(10);Turtle.fd(-20);Turtle.fd(10);Turtle.rt(-90);Turtle.fd(-20);Turtle.circle(15,-90);Turtle.fd(-20);Turtle.rt(180);Turtle.circle(-35,90);Turtle.fd(20);Turtle.circle(-35,180)
            
        else:
            Turtle.reset()
            Turtle.fd(20);Turtle.rt(-45);Turtle.fd(15);Turtle.rt(-45);Turtle.fd(20);Turtle.rt(90);Turtle.fd(10);Turtle.fd(-20);Turtle.fd(10);Turtle.rt(-90);Turtle.fd(-20);Turtle.rt(45);Turtle.fd(-15);Turtle.rt(45);Turtle.fd(-20);Turtle.rt(45);Turtle.fd(-15);Turtle.rt(225);Turtle.fd(40);Turtle.rt(45);Turtle.fd(20);Turtle.rt(45);Turtle.fd	(20);Turtle.rt(45);Turtle.fd(10);Turtle.rt(45);Turtle.fd(2);
def H():
	Turtle.reset()
	Turtle.rt(-90);Turtle.fd(60);Turtle.fd(-40);Turtle.rt(90);Turtle.fd(20);Turtle.rt(90);Turtle.fd(20);Turtle.fd(-40)
def I():
	Turtle.reset()
	Turtle.fd(30);Turtle.fd(-15);Turtle.rt(-90);Turtle.fd(60);Turtle.rt(90);Turtle.fd(15);Turtle.fd(-30)
def J():
        if Smooth == 'Y':
            Turtle.reset()
            Turtle.circle(15,-90);Turtle.circle(15,180);Turtle.fd(55);Turtle.rt(90);Turtle.fd(15);Turtle.fd(-30)
        else:
            Turtle.reset()
            Turtle.fd(15);Turtle.rt(-45);Turtle.fd(12.5);Turtle.rt(-45);Turtle.fd(55);Turtle.rt(90);Turtle.fd(15);Turtle.fd(-30)
def K():
	Turtle.reset()
	Turtle.rt(-90);Turtle.fd(60);Turtle.fd(-30);Turtle.rt(45);Turtle.fd(40);Turtle.fd(-40);Turtle.rt(90);Turtle.fd(45)
def L():
	Turtle.reset()
	Turtle.fd(25);Turtle.fd(-25);Turtle.rt(-90);Turtle.fd(60)
def M():
	Turtle.reset()
	Turtle.rt(-90);Turtle.fd(60);Turtle.rt(135);Turtle.fd(40);Turtle.rt(-90);Turtle.fd(40);Turtle.rt(135);Turtle.fd(60)
def N():
	Turtle.reset()
	Turtle.rt(-90);Turtle.fd(60);Turtle.rt(150);Turtle.fd(70);Turtle.rt(-150);Turtle.fd(60)
def O():
        if Smooth == 'Y':
            Turtle.reset()
            Turtle.circle(-30,360)
        else:
                Turtle.reset()
                Turtle.fd(40);Turtle.rt(-45);Turtle.fd(40);Turtle.rt(-45);Turtle.fd(40);Turtle.rt(-45);Turtle.fd(40);Turtle.rt(-45);Turtle.fd(40);Turtle.rt(-45);Turtle.fd(40);Turtle.rt(-45);Turtle.fd(40);Turtle.rt(-45);Turtle.fd(40);Turtle.rt(-45)
def P():
        if Smooth == 'Y':
                Turtle.reset()
                Turtle.rt(-90);Turtle.fd(60);Turtle.rt(90);Turtle.fd(20);Turtle.circle(-15,180);Turtle.fd(20)
        else:
                Turtle.reset()
                Turtle.rt(-90);Turtle.fd(60);Turtle.rt(90);Turtle.fd(20);Turtle.rt(45);Turtle.fd(15);Turtle.rt(45);Turtle.fd(12.5);Turtle.rt(45);Turtle.fd(15);Turtle.rt(45);Turtle.fd(20)
def Q():
        if Smooth == 'Y':
                Turtle.reset()
                Turtle.circle
        Turtle.reset()
	Turtle.fd(40);Turtle.rt(-45);Turtle.fd(40);Turtle.rt(-45);Turtle.fd(40);Turtle.rt(-45);Turtle.fd(40);Turtle.rt(-45);Turtle.fd(40);Turtle.rt(-45);Turtle.fd(40);Turtle.rt(-45);Turtle.fd(40);Turtle.rt(-45);Turtle.fd(40);Turtle.rt(-45);Turtle.fd(40);Turtle.rt(-45);Turtle.fd(20);Turtle.rt(90);Turtle.fd(20);Turtle.fd(-40)
def R():
	Turtle.reset()
	Turtle.rt(-90);Turtle.fd(60);Turtle.rt(90);Turtle.fd(20);Turtle.rt(45);Turtle.fd(15);Turtle.rt(45);Turtle.fd(12.5);Turtle.rt(45);Turtle.fd(15);Turtle.rt(45);Turtle.fd(20);Turtle.rt(225);Turtle.fd(40)
def S():
	Turtle.reset()
	Turtle.fd(30);Turtle.rt(-45);Turtle.fd(10);Turtle.rt(-45);Turtle.fd(25);Turtle.rt(-45);Turtle.fd(10);Turtle.rt(-45);Turtle.fd(25);Turtle.rt(45);Turtle.fd(10);Turtle.rt(45);Turtle.fd(25);Turtle.rt(45);Turtle.fd(10);Turtle.rt(45);Turtle.fd(30)
def T():
	Turtle.reset()
	Turtle.rt(-90);Turtle.fd(60);Turtle.rt(90);Turtle.fd(15);Turtle.fd(-30)
def U():
	Turtle.reset()
	Turtle.fd(25);Turtle.rt(-45);Turtle.fd(15);Turtle.rt(-45);Turtle.fd(50);Turtle.rt(180);Turtle.fd(50);Turtle.rt(45);Turtle.fd(15);Turtle.rt(45);Turtle.fd(25);Turtle.rt(45);Turtle.fd(15);Turtle.rt(45);Turtle.fd(50)
def V():
	Turtle.reset()
	Turtle.rt(-60);Turtle.fd(80);Turtle.fd(-80);Turtle.rt(120);Turtle.fd(-80)
def W():
	Turtle.reset()
	Turtle.rt(-60);Turtle.fd(80);Turtle.fd(-80);Turtle.rt(120);Turtle.fd(-80);Turtle.fd(80);Turtle.rt(-120);	Turtle.fd(80);Turtle.rt(120);Turtle.fd(80);Turtle.rt(-120);Turtle.fd(80)
def X():
	Turtle.reset()
	Turtle.rt(-45);Turtle.fd(120);Turtle.rt(180);Turtle.fd(60);Turtle.rt(90);Turtle.fd(60);Turtle.fd(-120);
def Y():
	Turtle.reset()
	Turtle.rt(-90);Turtle.fd(40);Turtle.rt(30);Turtle.fd(35);Turtle.fd(-35);Turtle.rt(-60);Turtle.fd(35)
def Z():
	Turtle.reset()
	Turtle.fd(40);Turtle.fd(-40);Turtle.rt(-45);Turtle.fd(60);Turtle.rt(-135);Turtle.fd(40)
def goto(line) :
	global lineNumber
	line = lineNumber

Char = input("Input ONE Capital Latin Character")
if Char.upper() =='A':
	A()
elif Char.upper() =='B':
	B()
elif Char.upper() =='C':
	C()
elif Char.upper() =='D':
	D()
elif Char.upper() =='E':
	E()
elif Char.upper() =='F':
	F()
elif Char.upper() =='G':
	G()
elif Char.upper() =='H':
	H()
elif Char.upper() =='I':
	I()
elif Char.upper() =='J':
	J()
elif Char.upper() =='K':
	K()
elif Char.upper() =='L':
	L()
elif Char.upper() =='M':
	M()
elif Char.upper() =='N':
	N()
elif Char.upper() =='O':
	O()
elif Char.upper() =='P':
	P()
elif Char.upper() =='Q':
	Q()
elif Char.upper() =='R':
	R()
elif Char.upper() =='S':
	S()
elif Char.upper() =='T':
	T()
elif Char.upper() =='U':
	U()
elif Char.upper() =='V':
	V()
elif Char.upper() =='W':
	W()
elif Char.upper() =='X':
	X()
elif Char.upper() =='Y':
	Y()
elif Char.upper() =='Z':
	Z()
else:
	print ("That is not a recognised character. Please input a singular ppercase latin charcter with no accents and no special characters.")
