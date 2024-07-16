if choose == "smile" :
    print("Opening Turtle Graphic Window")
    time.sleep(1.9)
    print("Failed To Manually Open Window, Please Click Feather Icon In TaskBar, it may take a few clicks...")
t.penup()
t.goto(0,0)
t.pencolor("black")
t.pendown()
t.width(20)
t.speed(100)
for i in range(37):
    t.forward(15)
    t.left(10)
    
t.penup()
t.goto(-15,100)
t.pencolor("black")
t.pendown()
t.width(15)
t.speed(100)
for i in range(1):
    t.forward(1)
    t.left(1)
    
t.penup()
t.goto(20,100)
t.pencolor("black")
t.pendown()
t.width(15)
t.speed(100)
for i in range(1):
    t.forward(1)
    t.left(1)

t.penup()
t.goto(-20,60)
t.pencolor("black")
t.pendown()  
t.right(90)
for i in range(16):
    t.forward(5)
    t.left(10)
