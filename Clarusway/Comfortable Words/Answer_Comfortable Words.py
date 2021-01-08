
left_hand =  "qwertasdfgzxcvb"
right_hand = "yuiophjklnm"

word = set(input())

if word.issubset(right_hand) or word.issubset(left_hand):
    print(False)
else:
    print(True)


