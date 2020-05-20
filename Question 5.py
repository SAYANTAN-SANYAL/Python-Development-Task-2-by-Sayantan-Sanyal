S1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
S2 = {1, 3, 4, 6, 8, 11, 22, 34, 51, 67}
for i in range(1,10):
    if i in S2:
        S1.discard(i)
print("The final set is: ", S1)         