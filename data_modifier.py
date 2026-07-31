import pandas as pd

class DataModifier:
    def __init__(self, filename):
        # Load CSV, store original (untouched), and working (mutable) copies
        self.filename = filename
        self.original_df = pd.read_csv(filename)
        self.working_df = self.original_df.copy()

    def reset(self):
        # Revert working_df back to a fresh copy of original_df
        self.working_df = self.original_df.copy()

    def sort(self, column, ascending=True):
        # Sort working_df by column, ascending (default) or descending
        if column not in self.working_df.columns:
             print(f"Column '{column}' not found.")
             return
        self.working_df = self.working_df.sort_values(by=column, ascending=ascending)

    def filter(self, conditions):
        # Filter working_df by condition(s). List of (column, operator, value) tuples are passed here, then parsed
        df = self.working_df

        # Creating a dict of lambdas, slightly faster than writing a bunch of if statements
        operators = {
             "==": lambda col, val: df[col] == val,
             "!=": lambda col, val: df[col] != val,
             ">": lambda col, val: df[col] > val,
             "<": lambda col, val: df[col] < val,
             ">=": lambda col, val: df[col] >= val,
             "<=": lambda col, val: df[col] <= val,
        }

        # Edge case handling + enacts changes onto df
        for column, operator, value in conditions:
             if column not in df.columns:
                  print(f"Column '{column}' not found.")
                  return
             if operator not in operators:
                  print(f"Unknown operator '{operator}'.")
                  return
             df = df[operators[operator](column, value)]

        self.working_df = df

    def aggregate(self, column, method):
        # Compute mean/median/sum for a chosen column
        if column not in self.working_df.columns:
             print(f"Invalid column: {column}.")
             return None
        if not pd.api.types.is_numeric_dtype(self.working_df[column]): # checks if String rather than number
            print(f"Column '{column}' is not numeric, cannot aggregate.")
            return None

        if method == "mean":
            return self.working_df[column].mean()
        elif method == "median":
                    return self.working_df[column].median()
        elif method == "sum":
                    return self.working_df[column].sum()
        else:
             print(f"Invalid method: {method}")
             return None

    def correlate(self, column_a, column_b):
        # Calculates correlation between two columns, returns plain-English interpretation
        for col in (column_a, column_b):
             if col not in self.working_df.columns:
                  print(f"Column '{col} not found.")
                  return None
             if not pd.api.types.is_numeric_dtype(self.working_df[col]):
                print(f"Column '{col}' is not numeric, cannot aggregate.")
                return None
        
        return self.working_df[column_a].corr(self.working_df[column_b])

    def display(self):
        # Displays working_df in console
        if self.working_df.empty:
            print("No data to display (current filter/result is empty).")
            return

        # Formatting, changes display options only for this block of code, not throughout the program
        with pd.option_context(
            "display.max_columns", None,   # don't truncate columns
            "display.width", None,         # don't wrap based on terminal guess
            "display.float_format", "{:.2f}".format,  # 2 decimal places
        ):
            print(self.working_df)

    def get_columns(self):
        # Return/print list of available columns (used by multiple menu options)
        return list(self.working_df.columns)