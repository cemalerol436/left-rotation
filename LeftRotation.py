# Left Rotation Codes turn the elements to the left side.

a = [4,56,45,89,56,45,7]

# d number determines the steps of rotation.

d = 3
res = [0]*len(a)

k = 0

# the loop replaces the numbers in the array.

while k<(len(a)):

    res[k] = a[(k+d)%len(a)]
    k += 1


print(res)
