from time import sleep
import board
import digitalio
import busio
import adafruit_ssd1306


class OledMenu:
    def __init__(self, i2c, width=128, height=32):
        self.oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
        self.options = []
        self.selected_index = 0
        self.display_offset = 0
        self.visible_lines = height // 8  # Each line is 8 pixels tall

    def add_option(self, label_text, callback=None):
        """Adds an option to the menu."""
        self.options.append({'label': label_text, 'callback': callback})

    def move_selection(self, direction):
        """Moves the selection up (-1) or down (+1)."""
        self.selected_index = (self.selected_index + direction) % len(self.options)

        # Adjust display offset if necessary
        if self.selected_index < self.display_offset:
            self.display_offset = self.selected_index
        elif self.selected_index >= self.display_offset + self.visible_lines:
            self.display_offset = self.selected_index - self.visible_lines + 1

    def select_option(self):
        """Executes the callback of the selected option if it exists."""
        callback = self.options[self.selected_index].get('callback')
        if callback:
            callback()

    def render(self):
        """Renders the menu on the OLED screen."""
        self.oled.fill(0)  # Clear the display
        for i, option in enumerate(self.options[self.display_offset:self.display_offset + self.visible_lines]):
            y = i * 8
            prefix = '>' if self.display_offset + i == self.selected_index else ' '
            text = f"{prefix} {option['label']}"
            self.oled.text(text, 0, y, 1)  # Built-in method for rendering text
        self.oled.show()  # Refresh the display
