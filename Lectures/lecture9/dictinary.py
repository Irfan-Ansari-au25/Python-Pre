"""
dict = {
    "BJP":32,
    "Congress": 12,
    "AAP": 29

}

print(dict)
print (dict.items())
print(dict.keys())
print(dict.values())



"""
parties = ["BJP", "AAP", "Congress", "BJP","AAP", "BJP", "BJP"]
party_dict = {}

for party in parties:
    if party in party_dict:
        party_dict[party] += 1
    else:
        party_dict[party] = 1
print(party_dict)

votes = 0
winner_party = ""

for party, vote in party_dict.items():
    if vote > votes:
        votes = vote
        winner_party =party
print(winner_party)



