parties = ['a', 'b', 'c', 'd', 'e', 'f','c','d','e','f','a','b','c','d','e','f','a','b', 'c', 'd', 'e', 'f','c','f','f']

freq = {}

for party in parties:
    if party in freq:
        freq[party] += 1
    else:
        freq[party] = 1

print(freq)

max_no = 0

for key in freq.keys():
    if freq[key] > max_no:
        max_no = freq[key]
        winner_party = key
print(winner_party)
