# Function: 3-level speed control, adjust speed via Button B, display speed value on LED screen
from microbit import *
import Tinybit

# Define three speed levels: Low, Medium, High
speed_list = [50, 70, 90]
current_index = 1  # Default speed
current_speed = speed_list[current_index]

# Main loop
def on_forever():
    global current_index, current_speed
    # Press B button to switch speed
    if button_b.was_pressed():
        current_index = (current_index + 1) % 3
        current_speed = speed_list[current_index]
        basic.show_number(current_speed)
        sleep(300)
    # Keep vehicle static for independent speed test
    Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)

basic.forever(on_forever)