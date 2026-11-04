from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_len=2,stretch_wid=1)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(300,random.randint(-250,250))
        self.cars.append(new_car)

    def move_car(self):
        for cars in self.cars:
            new_x = cars.xcor()  - STARTING_MOVE_DISTANCE
            new_y = cars.ycor()
            cars.goto(new_x,new_y)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT

    def collision(self, player):
        for car in self.cars:
            if player.distance(car) < 20:
                return True
        return False


