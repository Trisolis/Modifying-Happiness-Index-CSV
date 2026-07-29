import pandas as pd

class DataModifier:
    def __init__(self, filename):
        # Load CSV, store original (untouched), and working (mutable) copies
        self.filename = filename
        self.original_df = pd.read_csv(filename)
        self.working_df = self.original_df.copy()

    def reset(self):
        # Revert working_df back to a fresh copy of original_df
        pass

    def sort(self, column, ascending=True):
        # Sort working_df by column, ascending (default) or descending
        pass

    def filter(self, conditions):
        # Filter working_df by condition(s)
        pass

    def aggregate(self, column, method):
        # Compute mean/median/sum for a chosen column
        pass

    def correlate(self, column_a, column_b):
        # Calculates correlation between two columns, returns plain-English interpretation
        pass

    def display(self):
        # Displays working_df in console
        print(self.working_df)

    def get_columns(self):
        # Return/print list of available columns (used by multiple menu options)
        pass