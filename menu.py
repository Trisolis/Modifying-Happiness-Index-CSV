from data_modifier import DataModifier

class Menu:
    def __init__(self, filename):
        # Create a DataModifier instance to operate on
        self.data_modifier = DataModifier(filename)

    def run(self):
        # Main loop: print the menu, get input, handle w functions below, repeat until quit
        while True:
            self.printmenu()
            choice = input("Enter your choice: ")

            if choice == "8":
                print("Goodbye!")
                break

            self.handle_input(choice)

    def print_menu(self):
        # Display available options to the user
        print("\n--- Data Modifier Menu ---")
        print("1) Reset to original data")
        print("2) Sort")
        print("3) Filter")
        print("4) Aggregate (mean/median/sum)")
        print("5) Correlate")
        print("6) Display current data")
        print("7) Show columns")
        print("8) Quit")
        # Loop the default menu. Have multiple options for the user (reset, sort, filter, aggregate, correlate, display, quit)
        pass

    def handle_input(self, choice):
        # Map user choice to appropriate DataModifier method
        pass