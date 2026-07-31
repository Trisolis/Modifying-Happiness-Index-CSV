from data_modifier import DataModifier

class Menu:
    def __init__(self, filename):
        # Create a DataModifier instance to operate on
        self.data_modifier = DataModifier(filename)

    def run(self):
        # Main loop: print the menu, get input, handle w functions below, repeat until quit
        while True:
            self.print_menu()
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
        dm = self.data_modifier
        if choice == "1":
            # Reset
            dm.reset()
            print("Data reset to original CSV")

        elif choice == "2":
            # Sort
            print("Available columns: ", dm.get_columns())
            col = input("Which column would you like to sort by? ").strip()
            asc = input("Ascending or descending? (a/d) ").strip()
            dm.sort(col, ascending=(asc != "d"))
            dm.display()

        elif choice == "3":
            # Filter
            print("Available columns: ", dm.get_columns())
            raw = input(
            "Enter condition(s), format: column operator value | column operator value ...\n"
            "Example: Region == Western Europe | Happiness Score > 5\n> "
            )
            conditions = self._parse_conditions(raw)
            if conditions is not None:
                dm.filter(conditions)
                dm.display()
        
        elif choice == "4":
            # Aggregate
            print("Available columns: ", dm.get_columns())
            column = input("What column would you like to aggregate? ")
            method = input("What would you like to do? (mean/median/sum) ")
            result = dm.aggregate(column, method)

            print(f"{method} of {column} is {result}")

        
        elif choice == "5":
            # Correlate
            print("Available columns: ", dm.get_columns())
            col_a = input("First column: ")
            col_b = input("Second column: ")
            correlation = dm.correlate(col_a, col_b)

            if correlation is None:
                return

            else:
                # Have to account for positive or negative correlations, as well as strength
                strength = abs(correlation)
                direction = "positive" if correlation > 0 else "negative"

                if strength <= 0.3:
                    label = "no meaningful"
                elif strength <= 0.5:
                    label = "a weak"
                elif strength <= 0.8:
                    label = "a moderate"
                else:
                    label = "a strong"

                print(f"Your correlation value is: {correlation:.2f}. This means there is {label} {direction} correlation between your two variables")

        
        elif choice == "6":
            # Display
            dm.display()

        elif choice == "7":
            # Display columns
            print(dm.get_columns())

        else:
            print("Invalid choice. Please try again.")

    def _parse_conditions(self, raw):
        # Helper for parsing strings for Filter
        valid_operators = ["==", "!=", ">=", "<=", ">", "<"] # longer operations go first, otherwise > would be recognized first even if using >=
        conditions = []

        # Checks each raw data 'chunk' for a valid operator, and returns None if none found
        for chunk in raw.split("|"):
            chunk = chunk.strip()
            found_operator = None
            for op in valid_operators:
                if op in chunk:
                    found_operator = op
                    break

            if found_operator is None:
                print(f"Could not find a valid operator in '{chunk}'")
                return None

            # Another split to find column and value out of the already split chunk
            column, value = chunk.split(found_operator)
            column = column.strip()
            value = value.strip()

            try:
                value = float(value)
            except ValueError:
                pass # keep as string if it's not a number value

            conditions.append((column, found_operator, value))

        return conditions