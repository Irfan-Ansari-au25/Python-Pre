


setA = set("aeioueaeiou")
print(setA, "setA")

setB = set("iwantyou")
print(setB, "setB")

setC = setA.union(setB)
print(setC, "union")

setD = setA.intersection(setB)
print(setD, "intersection")

setE = setA.difference(setB) # A-B present in A but not in B
print(setE, "difference")

union_list = sorted(list(setC))
print(union_list,"union list")

# program for testing letters present in two word

vowel = set('aeiou')
word = set('iamnewhere')

common = list(vowel.intersection(word))
print(common)