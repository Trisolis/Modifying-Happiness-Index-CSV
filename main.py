from menu import Menu

if __name__ == "__main__":
    menu = Menu("2015.csv")
    dm = menu.data_modifier
    # menu.run()
    print("=== Initial load ===")
    dm.display()

    print("\n=== get_columns ===")
    print(dm.get_columns())

    print("\n=== sort: family ascending ===")
    dm.sort("Family", ascending=True)
    dm.display()

    print("\n=== sort: family descending ===")
    dm.sort("Family", ascending=False)
    dm.display()

    print("\n=== sort: bad column (should print error, not crash) ===")
    dm.sort("height", ascending=True)

    print("\n=== reset after sorting ===")
    dm.reset()
    dm.display()

    print("\n=== aggregate: mean of family ===")
    print(dm.aggregate("Family", "mean"))

    print("\n=== aggregate: median of family ===")
    print(dm.aggregate("Family", "median"))

    print("\n=== aggregate: sum of family ===")
    print(dm.aggregate("Family", "sum"))

    print("\n=== aggregate: bad column ===")
    print(dm.aggregate("height", "mean"))

    print("\n=== aggregate: bad method ===")
    print(dm.aggregate("Family", "banana"))

    print("\n=== correlate: family vs happiness score ===")
    print(dm.correlate("Family", "Happiness Score"))

    print("\n=== correlate: bad column ===")
    print(dm.correlate("Family", "height"))

    print("\n=== menu.print_menu() ===")
    menu.print_menu()

    print("\n=== menu.handle_input via option 6 (display) ===")
    menu.handle_input("6")

    print("\n=== menu.handle_input via option 7 (columns) ===")
    menu.handle_input("7")

    print("\n=== menu.handle_input via option 1 (reset) ===")
    menu.handle_input("1")

    print("\n=== menu.handle_input: invalid choice ===")
    menu.handle_input("99")

    print("\n=== Full interactive run() ===")
    menu.run()