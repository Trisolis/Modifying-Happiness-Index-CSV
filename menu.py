from data_modifier import DataModifier

class Menu:
    def __init__(self, filename):
        # Create a DataModifier instance to operate on
        self.data_modifier = DataModifier(filename)

    def run(self):
        # Main loop: print the menu, get input, handle w functions below, repeat until quit
        pass

    def print_menu(self):
        # Display available options to the user
        pass

    def handle_input(self, choice):
        # Map user choice to appropriate DataModifier method
        pass