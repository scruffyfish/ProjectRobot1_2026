# Tinybit Car Full Project
# Integrated functions: speed adjustment + automatic square path tracking + black line following mode
from microbit import *
import Tinybit

# Global speed parameter for vehicle movement
speed = 70
# Operation mode definition: 1 = automatic square path, 2 = line following mode
# Default mode set to line following
mode = 2

# Display corresponding icon on microbit LED screen for current mode
def show_icon():
    if mode == 1:
        basic.show_icon(IconNames.TARGET) # Icon for automatic square driving mode
    elif mode == 2:
        basic.show_icon(IconNames.ARROW_N)# Icon for black line tracking mode

# Function to make the car automatically travel along a closed square route
def auto_path():
    Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, speed)
    sleep(1500)
    Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINRIGHT, speed)
    sleep(700)
    
    Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, speed)
    sleep(1500)
    Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINRIGHT, speed)
    sleep(700)
    
    Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, speed)
    sleep(1500)
    Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINRIGHT, speed)
    sleep(700)
    
    Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, speed)
    sleep(1500)
    Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)

# Line tracking logic based on left and right infrared line sensors
def line_follow():
    # Both sensors detect white ground, move forward
    if Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.WHITE) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.WHITE):
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, speed)
    # Left sensor detects black line, spin left to correct direction
    elif Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.BLACK) and Tinybit.Line_Sensor(Tinybit.enLineState.WHITE):
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINLEFT, speed)
    # Right sensor detects black line, spin right to correct direction
    elif Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.WHITE) and Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.BLACK:
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINRIGHT, speed)
    # No valid line detected, stop the vehicle
    else:
        Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)

# Main loop function executed continuously
def on_forever():
    global mode, speed
    
    # Short press button A to switch between two operation modes
    if button_a.was_pressed():
        mode = 3 - mode
        show_icon()
        sleep(500)
    
    # Short press button B to cycle through 3 speed levels: 50 -> 70 -> 90
    if button_b.was_pressed():
        if speed == 50:
            speed = 70
        elif speed == 70:
            speed = 90
        else:
            speed = 50
        basic.show_number(speed)
        sleep(300)
    
    # Execute logic according to selected mode
    if mode == 1:
        auto_path()
        mode = 2
        show_icon()
    elif mode == 2:
        # Execute infrared line tracking function
        line_follow()

# Start infinite main loop
basic.forever(on_forever)
