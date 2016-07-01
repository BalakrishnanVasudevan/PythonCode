import itertools, random
a = [1,2,3,4,5,6,7,8,9,"A","Jack","Queen","King"]
deck = list(itertools.product(a,["Spade","Diamond","Clover","Hearts"]))
random.shuffle(deck)
print("You got:")
for i in range(4):
 print(deck[i][0], "of", deck[i][1])

