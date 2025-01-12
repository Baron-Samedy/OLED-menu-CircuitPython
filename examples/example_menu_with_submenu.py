from time import sleep
import board
import digitalio
import busio
from oled_menu_ssd1306 import OledMenu  # Импортируем класс меню

    # Initialize I2C interface
    i2c = busio.I2C(board.GP19, board.GP18)  # Use appropriate GPIO pins

    # Initialize Buttons
    button_up = digitalio.DigitalInOut(board.GP25)  # Button UP pin
    button_up.switch_to_input(pull=digitalio.Pull.DOWN)

    button_down = digitalio.DigitalInOut(board.GP24)  #  Button DOWN pin
    button_down.switch_to_input(pull=digitalio.Pull.DOWN)

    button_select = digitalio.DigitalInOut(board.GP23)  #  Button ENTER pin
    button_select.switch_to_input(pull=digitalio.Pull.DOWN)

    button_back = digitalio.DigitalInOut(board.GP22)  #  Button BACK pin
    button_back.switch_to_input(pull=digitalio.Pull.DOWN)

    # Create menu
    menu = OledMenu(i2c)
    
    # Create submenu
    submenu = OledMenu(i2c)

    # Define callbacks
    def option_one_callback():
        print("Option One Selected")

    def option_two_callback():
        print("Option Two Selected")
        
    def option_one_submenu_callback():
    global current_menu
    current_menu = submenu
    
    def back_to_main_menu():
    global current_menu
    current_menu = main_menu

    # Add menu options
    menu.add_option("Option One", option_one_callback)
    menu.add_option("Option Two", option_two_callback)
    menu.add_option("Option submenu", option_submenu_callback)
    menu.add_option("Option Three")
    
    # Add submenu options
    
    submenu.add_option("Option 1", option_one_submenu_callback)
    submenu.add_option("Back", back_to_main_menu)
    

    current_menu = main_menu
    
    # Main loop
    while True:
        # Processing button UP
        if button_up.value:  # if button click
            current_menu.move_selection(-1)
            sleep(0.1)  # Задержка для предотвращения многократного срабатывания

        # Processing button DOWN
        if button_down.value:  # if button click
            current_menu.move_selection(1)
            sleep(0.1)

        # Processing button ENTER
        if button_select.value:  # if button click
            current_menu.select_option()
            sleep(0.1)

        # Processing button back
        if button_back.value and current_menu != main_menu:  # if button click in submenu
            back_to_main_menu()
            sleep(0.1)

        # Draw menu
        current_menu.render()

        sleep(0.01) 
        