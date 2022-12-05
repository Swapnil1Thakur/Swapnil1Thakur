n=int(input(""))
if 360%n==0:
    print("Yes possible to cut in to n equal pieces")
else:
    print("No")
if n<=360:
    print("Yes possible to cut in any size")
else:
    print("No")
if (n*(n+1/2))<=360:
    print("Yes possible to cut with no two of them are equal")
else:
    print("No")
