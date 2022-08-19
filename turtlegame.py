import random
import turtle
raceon=False
scren=turtle.Screen()
scren.setup(width=500,height=400)
user=scren.textinput(title="User 1 Make your bet",prompt="Which turtle will win the race ? Enter a colour:")
use2=scren.textinput(title="User 2 Make your bet",prompt="Which turtle will win the race ? Enter a colour:")
y=[-100,-70,-40,-10,20,50]
colors=["red","yellow","orange","blue","green","purple"]
all_t=[]
if user!=None and use2!=None:
    for i in range(6):
        tim = turtle.Turtle(shape="turtle")
        tim.penup()
        tim.color(colors[i])
        tim.goto(x=-230, y=y[i])
        all_t.append(tim)
    if user:
        raceon=True
    while raceon:
        rand=random.randint(1,10)
        randc=random.choice(all_t)
        randc.forward(rand)
        if randc.xcor()>220:
            raceon = False
            scren.bye()
            if randc.pencolor()==user:
                print("yay user1 won")
            elif randc.pencolor()==use2:
                print("yay user2 won")
            else:
                print(f"Sorry u all lost.{randc.pencolor()} won the race.")
else:
    scren.bye()
    print("Users didn't select a turtle.")








