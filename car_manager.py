from turtle import Turtle
from random import randint


class Car(Turtle):

    def __init__(self, n_car=5):
        super().__init__()
        self.hideturtle()
        self.n_car = n_car
        self.car_speed = 10
        self.cars = []
        self.create_cars(n_car)
        self.cars_speed = 0.1

    @staticmethod
    def randon_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        color = (r, g, b)
        return color

    @staticmethod
    def random_position():
        new_y_position = randint(-250, 260)
        new_x_position = randint(-280, 270)
        position = (new_x_position, new_y_position)
        return position

    def create_cars(self, number_of_cars):
        for car in range(number_of_cars):
            new_car = self.car()
            self.cars.append(new_car)

    def car(self):
        car = Turtle("square")
        car.penup()
        car.color(self.randon_color())
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.goto(self.random_position())
        return car

    def move_car(self):
        for car in self.cars:
            speed = car.xcor()
            speed -= self.car_speed
            car.goto(speed, car.ycor())

    def reset_car_position(self):
        for car in self.cars:
            if car.xcor() < -310:
                car.goto(300, self.random_position()[1])
                car.color(self.randon_color())

    def increase_cars_speed(self):
        self.cars_speed *= 0.7

    def collision_with_turtle(self, turtle):
        for car in self.cars:
            if car.distance(turtle) < 25:
                return True









