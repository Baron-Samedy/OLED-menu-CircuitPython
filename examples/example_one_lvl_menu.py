from time import sleep
import board
import digitalio
import busio
from oled_menu_ssd1306 import OledMenu  # Импортируем класс меню

    # Initialize I2C interface
    i2c = busio.I2C(board.GP19, board.GP18)  # Use appropriate GPIO pins

    # Create menu
    menu = OledMenu(i2c)

    # Define callbacks
    def option_one_callback():
        print("Option One Selected")

    def option_two_callback():
        print("Option Two Selected")

    # Add menu options
    menu.add_option("Option One", option_one_callback)
    menu.add_option("Option Two", option_two_callback)
    menu.add_option("Option Three")

    # Main loop
    while True:
        menu.render()

        # Simulated button handling
        # Replace these with actual GPIO button checks
        if False:  # Replace with condition to move up
            menu.move_selection(-1)
        elif False:  # Replace with condition to move down
            menu.move_selection(1)
        elif False:  # Replace with condition to select
            menu.select_option()

        sleep(0.1)