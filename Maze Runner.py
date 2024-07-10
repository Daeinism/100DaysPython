def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()

def follow_along():
    turn_right()
    while front_is_clear():
        move()
    if wall_on_right() != True:
        turn_right()
    elif wall_on_right() == True:
        turn_left()

while at_goal() != True:
    if not wall_on_right():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front() and not wall_on_right():
        turn_right()
        

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
