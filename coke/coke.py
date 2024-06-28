#global variables
DUE = 50
COINS = 0

#calculates amount due and change owed
def calc_amount(COINS):
    global DUE
    if COINS in [25, 10, 5]:
        DUE = DUE - COINS
        if DUE <= 0 :
            print(f"Change Owed: {abs(DUE)}")
        else:
            print(f"Amount Due: {DUE}")
    else:
        print(f"Amount Due: {DUE}")


def main():
    print(f"Amount Due: {DUE}")
    while DUE>0:
        COINS = int(input("Insert Coin: "))
        calc_amount(COINS)

main()
