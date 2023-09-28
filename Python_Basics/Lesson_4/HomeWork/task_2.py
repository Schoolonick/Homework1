while True:
    what = input().lower()

    if what == 'off':
        break

    if what == "game":
        for n in range(3):
            what = input("Якое число возьмём ? : ").lower()
            if what == '5':
                print("cool!")
            if what == 'off':
                break
