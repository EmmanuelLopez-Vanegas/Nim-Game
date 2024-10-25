import random

piles = [0,0,0]
counters = random.randint(3,100)
piles[0] = random.randint(1,counters - 2)
piles[1] = random.randint(1,counters - piles[0] - 1)
piles[2] = counters - piles[0] - piles[1]


temp0 = piles[0]
temp1 = piles[1]
temp2 = piles[2]
xor = None
temp = [temp0, temp1, temp2]
pos = temp.index(max(temp))
while xor != 0:
    temp[pos] = temp[pos] -1
    xor = temp[0] ^ temp[1] ^ temp[2]
print(xor)
print(piles)
print(temp)

print('hi')