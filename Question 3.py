List1 = [1,2,3,4,5,6,7]
List2 = []
for i in List1:
    if(i%2==0):
        List1.remove(i)
        List2.append(i)
print("List containing odd numbers is: ",List1)
print("List containing even numbers is: ",List2) 