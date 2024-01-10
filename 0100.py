import turtle
import os
import time
import pyttsx3
text_speech=pyttsx3.init()

def view_history():
    t.clear()
    f=open("history.txt","r")
    t.right(90)
    t.goto(-200,200)
    ch=f.readlines()
    for y in ch:
        if y[0]=="-": 
            t.color("red")
            t.write(y,font=("airal",30,"bold"))
        else:
            t.color("White")
            t.write(y,font=("airal",30,"bold"))
        t.forward(40)
    time.sleep(5)
    main_interface()

def history(x):
    fg=open("history.txt","a")
    fg.write("-"+str(x)+"\n")
    fg.close()

def history1(x):
    fg=open("history.txt","a")
    fg.write("+"+str(x)+"\n")
    fg.close()

def addcredit():
    text_speech.say("Enter the amount")
    text_speech.runAndWait()
    f=open("current_balance.txt","r")
    x=int(f.readline())
    y=turtle.numinput(title="Enter the amount",prompt="")
    history1(int(y))
    x=x+int(y)
    f.close()
    f=open("current_balance.txt","w")
    f.write(str(x))
    text_speech.say("Amount added successfully")
    text_speech.runAndWait()
    f.close()
    main_interface()

def adddebit():
    text_speech.say("Enter the amount")
    text_speech.runAndWait()
    f=open("current_balance.txt","r")
    x=int(f.readline())
    y=turtle.numinput(title="Enter the amount",prompt="")
    history(int(y))
    x=x-int(y)
    f.close()
    f=open("current_balance.txt","w")
    f.write(str(x))
    text_speech.say("Amount debited successfully")
    text_speech.runAndWait()
    f.close()
    main_interface()

def add_dccc():
    t.color("black")
    t.clear()
    win.bgpic("debit_image.gif")
    f=open("debit_info.txt","w")
    text_speech.say("Enter Your card number")
    text_speech.runAndWait()
    x=""
    while len(x)!=16:
        x=turtle.textinput(title="Enter your Card Number",prompt="Should Be Of 16 Digits")
    t.goto(-140,350)
    t.write(x,font=("airal",20,"bold"))
    f.write(str(x)+"\n")
    text_speech.say("Enter Your card expiry date")
    text_speech.runAndWait()
    x=turtle.textinput(title="Enter your Card",prompt="EXP DT")
    t.goto(-300,250)
    t.write(x,font=("airal",20,"bold"))
    f.write(str(x)+"\n")
    text_speech.say("Enter Your name on the card")
    text_speech.runAndWait()
    x=turtle.textinput(title="Enter Name On",prompt="The Card")
    
    t.goto(100,250)
    t.write(x,font=("airal",20,"bold"))
    f.write(str(x)+"\n")
    text_speech.say("Enter Your cards CVV Code")
    text_speech.runAndWait()
    x=""
    while len(x)!=3:
        x=turtle.textinput(title="Enter Card CVV Code",prompt="Should Be Of 3 Digits")
    t.goto(100,-300)
    t.write(x,font=("airal",20,"bold"))
    f.write(str(x))
    
    t.color("black")
    t.goto(-100,0)
    text_speech.say("Card saved successfully")
    text_speech.runAndWait()
    t.write("card saved sucesfully",font=("airal",20,"bold"))
    f.close()
    time.sleep(3)
    main_interface()

def currentbalance():
    f=open("current_balance.txt","r")
    t.clear()
    t.goto(-200,0)
    t.color("green")
    x=f.readline()
    text_speech.say("Your current balance is"+str(x))
    text_speech.runAndWait()
    t.write("Your Current Balace Is RS-"+x,font=("airal",30,"bold"))
    f.close()
    time.sleep(3)
    main_interface()

def view_dccc():
    f=open("debit_info.txt","r")
    t.clear()
    t.color("black")
    win.bgpic("debit_image.gif")
    t.goto(-140,330)
    x=f.readline()
    t.write(x,font=("airal",20,"bold"))
    t.goto(-300,250)
    x=f.readline()
    t.write("EXP DT "+x,font=("airal",20,"bold"))
    t.goto(100,250)
    x=f.readline()
    t.write(x,font=("airal",20,"bold"))
    t.goto(100,-300)
    x=f.readline()
    t.write("CVV "+x,font=("airal",20,"bold"))
    t.color("red")
    turtle.numinput(title="Press Any Key For Exit",prompt="")
    f.close()
    main_interface()

def main_interface():
    win.bgpic("0100.gif")
    t.clear()
    t.goto(-600,300)
    t.color("White")
    t.write("*****WELCOME TO THE MONEY MANAGEMENT SYSTEM*****",font=("airal",30,"bold"))
    t.goto(-500,-300)
    t.write("Press 1 to Add a Credit\n\n\nPress 2 to Add a Debit\n\n\nPress 3 to Add a Debit or Credit card\n\n\nPress 4 to View Current Balance\n\n\nPress 5 to View Saved Card\n\n\nPress 6 To Check Transaction History",font=("airal",20,"bold"))
    switch2=turtle.textinput(title="Enter your choice",prompt="")
    match(int(switch2)):
        case 1:
            addcredit()
        case 2:
            adddebit()
        case 3:
            add_dccc()
        case 4:
            currentbalance()
        case 5:
            view_dccc()
        case 6:
            view_history()

def register():
    t.clear()
    t.goto(-500, 200)
    t.color("white")
    t.write("                       ***WE WELCOME YOU*\n\nFILL THE DETAILS TO CREATE A NEW ACCOUNT***",font=("arial", 30, "bold"))
    t.goto(-500,-100)
    text_speech.say("Please enter your Name")
    text_speech.runAndWait()
    t.write("NAME\n\nMOBILE NUMBER\n\nPIN",font=("arial",20,"bold"))
    turtle.textinput(title="Please enter your Name",prompt="")
    
    x=""
    
    while len(x)!=10:
        text_speech.say("Please enter your Mobile Number")
        text_speech.runAndWait()
        x=turtle.textinput(title="Please enter your Mobile Number",prompt="Number should be of 10 digits")
        x=str(x)
    
    y=""
    
    while len(y)!=4:
        text_speech.say("Please enter your PIN Number")
        text_speech.runAndWait()
        y=turtle.textinput(title="Please enter your PIN Number",prompt="Number should be of 4 digits")
        y=str(y)
    f=open("login.txt","a")
    f.write(" "+x)
    f.write(" "+y)
    f.close()
    text_speech.say("Your Account Created Sucessfully")
    text_speech.runAndWait()
    login_register()
    
def error_screen():
    text_speech.say("User  not found")
    text_speech.runAndWait()
    t.clear()
    t.color("red")
    t.goto(-350, 50)
    t.write("***USER NOT FOUND*\n\n*Redirecting to the main page***",
            font=("arial", 40, "bold"))
    login_register()

def login():
    text_speech.say("PLEASE ENTER YOUR CREDENTIALS FOR LOGIN")
    text_speech.runAndWait()
    t.up()
    t.clear()
    t.color("white")
    t.goto(-550, 300)
    t.write("***PLEASE ENTER YOUR CREDENTIALS FOR LOGIN***",
            font=("arial", 30, "bold"))
    x = ""
    while len(x) != 10:
        text_speech.say("PLEASE ENTER YOUR MOBILE NUMBER")
        text_speech.runAndWait()
        x = turtle.textinput(title="Please enter your Mobile Number",prompt="Number shouls be of 10 digits")
        x = str(x)

    y = ""
    while len(y) != 4:
        text_speech.say("PLEASE ENTER YOUR PIN")
        text_speech.runAndWait()
        y = turtle.textinput(title="Please enter your PIN",prompt="PIN should be of 4 digits")
        y = str(y)

    f = open("login.txt", "r")
    users = f.readline().split()
    z = 0
    while z < len(users):
        if users[z] == x and users[z+1] == y:
            main_interface()
            break
        z += 2
    else:
        error_screen()
    f.close()

def login_register():
    t.clear()
    t.color("white")
    t.goto(-600, 300)
    text_speech.say("WE WELCOME YOU TO OUR MONEY MANAGEMENT SYSTEM")
    text_speech.runAndWait()
    t.write("***WELCOME TO THE MONEY MANAGEMENT SYSTEM***",
            font=("arial", 30, "bold"))
    text_speech.say("PRESS 1 TO SIGH IN OR 2 TO SIGN UP")
    text_speech.runAndWait()
    t.goto(-600, 100)
    t.color("white")
    t.write("Press 1 for Sign in", font=("arial", 20, "bold"))

    t.goto(-600, -100)
    t.color("white")
    t.write("Press 2 for Sign up", font=("arial", 20, "bold"))

    time.sleep(3)

    switch1 = turtle.numinput(title="Please enter your input",
                              prompt="")

    match(switch1):
        case 1:
            login()
        case 2:
            register()

t = turtle.Turtle()
t.hideturtle()
t.up()
win = turtle.Screen()
win.bgpic("0100.gif")
login_register()
turtle.done()