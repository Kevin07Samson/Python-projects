from turtle import Turtle

starting_position = [(0,0),(-20,0),(-40,0)]
moving_distance = 20




class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.mid = self.segments[1]
        self.tail = self.segments[2]
    def create_snake(self):
        for positions in starting_position:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(positions)
            self.segments.append(snake)

    def extend(self):
         snake = Turtle(shape="square")
         snake.color("white")
         snake.penup()
         snake.goto(self.segments[-1].position())
         self.segments.append(snake)
            
    def tail_collision(self):
        for segment in self.segments[1:]:
            if segment.distance(self.head) < 10:
                return True
        return False   

    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1 ):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)

        self.segments[0].forward(moving_distance)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading() != 180:
                self.segments[0].setheading(0)

