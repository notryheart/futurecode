from collections import Counter
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
count = Counter(hand)
hand_sorted = sorted(count.keys())
print(count[2],count[1])
print(count[1 + 1] - count[1])