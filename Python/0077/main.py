if __name__ == '__main__':

    wine_bottle = 1000
    empty_bottle = 0
    drink_bottle = 0

    while wine_bottle > 0:
        wine_bottle -= 1
        drink_bottle += 1
        empty_bottle += 1
        if empty_bottle == 3:
            wine_bottle += 1
            empty_bottle = 0

    if empty_bottle == 2:
        drink_bottle += 1

    print drink_bottle
