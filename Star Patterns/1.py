"""
*
**
***
****
*****
"""

n = int(input("Enter the no. of rows: "))
for i in range(1,n+1): #for rows
    for j in range(1,i+1): #for coloumn
        print("*",end="")
    print()