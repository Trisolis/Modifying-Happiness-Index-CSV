from menu import Menu

if __name__ == "__main__":
    menu = Menu("2015.csv")
    dm = menu.data_modifier
    # menu.run()
    dm.display()
    print(dm.get_columns())
    print(dm.aggregate("Happiness Score", "mean"))
    print(dm.aggregate("Happiness Score", "sum"))
    print(dm.correlate("Happiness Score", "Freedom"))

    # single condition
    dm.filter([("Family", ">", 1.00)])
    dm.display()

    dm.reset()

    # multiple conditions (AND)
    dm.filter([("Family", ">", 1.00), ("Happiness Rank", "<=", 25)])
    dm.display()

    dm.reset()

    # string equality
    dm.filter([("Region", "==", "Western Europe")])
    dm.display()

    dm.reset()

    # edge case: bad column name
    dm.filter([("height", ">", 10)])