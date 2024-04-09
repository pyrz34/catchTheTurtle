import random
import turtle


score = 0


catch_turtle_screen = turtle.Screen()
catch_turtle_screen.bgcolor("gray")
catch_turtle_screen.title("CATCH THE TURTLE")


player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.shapesize(2, 2, 1)
player_one.penup()


score_label = turtle.Turtle()
score_label.color("white")
score_label.penup()
score_label.goto(0, 250)
score_label.write("Score: 0", align="center", font=("Arial", 16, "normal"))


def click_handler(x, y):
    global score
    if player_one.distance(x, y) < 50:
        score += 1
        score_label.clear()
        score_label.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))
        player_one.goto(random.randint(-200, 200), random.randint(-200, 200))

catch_turtle_screen.onclick(click_handler)


for i in range(1000):
    random_x = random.randint(-200, 200)
    random_y = random.randint(-200, 200)
    player_one.goto(random_x, random_y)
    catch_turtle_screen.update()
    turtle.ontimer(lambda: None, 100)

turtle.mainloop()