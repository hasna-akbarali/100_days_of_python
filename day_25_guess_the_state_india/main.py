from turtle import Turtle,Screen
import pandas as pd

screen = Screen()
image = "map.gif"
screen.title('India States Game')
screen.setup(600,600)
screen.bgpic(image)

data = pd.read_csv('states.csv')
states_list = data['state'].tolist()
game_is_on = True

guessed_states = []

turtle = Turtle()
turtle.hideturtle()
turtle.penup()

while len(guessed_states) <= 28:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/28',prompt='What is your guess? ').title()
    if answer_state == 'Exit':
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print(missing_states)
        break

    if answer_state in states_list:
        guessed_states.append(answer_state)
        x_cor = int(data[data['state'] == answer_state]['x'])
        y_cor = int(data[data['state'] == answer_state]['y'])
        turtle.goto(x_cor,y_cor)
        turtle.write(answer_state,font=("Verdana",6, "normal"))




# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# screen.onscreenclick(get_mouse_click_coor)
# screen.mainloop()
