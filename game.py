from turtle import Turtle , Screen
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
startingposition = [(0,0),(-20,0),(-40,0)]


seg = []
for i in startingposition:
    snake = Turtle("square")
    snake.color("white")
    snake.penup()
    snake.goto(i)
    seg.append(snake)
print(seg[0])
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)
    for segment in range(len(seg)-1,0,-1):
        new_x = seg[segment-1].xcor()
        new_y = seg[segment-1].ycor()
        seg[segment].goto(new_x,new_y)
    seg[0].forward(20)
    seg[0].right(90)


    # for segm in seg:
    #     segm.forward(20)
    #     screen.update()
    #     time.sleep(1)
    # seg[0].right(90)



# print(seg[len(seg)])
# Set Maryam Method
# for i in startingposition:
#     snake.forward(100)
#     snake.goto(i)
#     snake.stamp()
#     snake.right(100)
















screen.exitonclick()
