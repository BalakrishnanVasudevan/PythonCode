import itertools, random
print("Note: 10=A, 11=Jack, 12=Queen, 13=King")
a_balance = int(100)
b_balance = int(100)
count = 0
a_win = 0
b_win = 0
while (a_balance and b_balance != 0):
    count+=1
    deck = list(itertools.product(range(1,14),["Spade","Diamond","Clover","Hearts"]))
    random.shuffle(deck)
    print("**************************************")
    print("Player A selected:")
    selection = random.choice(deck)
    print(selection)
    card, symbol = selection
    print("**************************************")
    deck.remove(selection)
    print("Player A ==================== Player B")
    print("**************************************")
    for i in range(len(deck)):
        c, s = deck[i]
        if i%2 == 0:
            a = deck[i]
            if c == card:
                print a
                a_balance, b_balance = a_balance+10, b_balance-10
                a_win+=1
                print("Mankatha!!! Player A wins!!")
                break
        else:
            b = deck[i]
            print a,"**********",b
            if c == card:
                a_balance, b_balance = a_balance-10, b_balance+10
                b_win+=1
                print("Mankatha!!!! Player B wins!!")
                break
print count, "matches were played"
print "Player A won", a_win, "times"
print "Player B won", b_win, "times"

