import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard_crossing import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score =Scoreboard()

screen.listen()
screen.onkey(player.go_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    cars.generate_cars()
    cars.move_cars()

    # collision with the car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
    if player.successful_crossing():
        score.increase_level()
        player.go_to_start()
        cars.level_up()
screen.exitonclick()
