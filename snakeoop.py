from turtle import Turtle
startingposition = [(0,0),(-20,0),(-40,0)]
Move_Distance = 20
Up =90
Down = 270
Left = 180
Right= 0


class Snake:
    def __init__(self):
        self.seg = []
        self.head = self.seg[0]

    def create_snake(self):
        for i in startingposition:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(i)
            self.seg.append(snake)
    def move(self):
        for segment in range(len(self.seg) - 1, 0, -1):
            new_x = self.seg[segment - 1].xcor()
            new_y = self.seg[segment - 1].ycor()
            self.seg[segment].goto(new_x, new_y)
        self.head.forward(Move_Distance)

    def up(self):
        if self.head.heading() != Down:
               self.head.setheading(Up)

    def Down(self):
      if  self.head.heading()!= Up:
           self.head.setheading(Down)

    def Left(self):
      if self.head.heading() !=Right:
          self.head.setheading(Left)

    def Right(self):

        if self.head.heading()!= Left:
            self.head.setheading(Right)