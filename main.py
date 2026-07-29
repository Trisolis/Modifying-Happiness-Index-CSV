from menu import Menu

if __name__ == "__main__":
    menu = Menu("2015.csv")
    # menu.run()
    menu.data_modifier.display()
    print(menu.data_modifier.get_columns())
    print(menu.data_modifier.aggregate("Happiness Score", "mean"))
    print(menu.data_modifier.aggregate("Happiness Score", "sum"))
    print(menu.data_modifier.correlate("Happiness Score", "Freedom"))

    menu.data_modifier.reset()
    menu.data_modifier.display()