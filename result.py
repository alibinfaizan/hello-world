cls = input("Which class? ")
print("")
def result(n):
    d = {}
    d2 = {}
    d3 = {}


    print("CLASS", n)
    print("")
    s = int(input("How many students are there in the class? "))

    for i in range(s):
        a,b = input("Roll No. : " +str(i+1)+ " --> ").upper(), int(input("Marks :"))
        print("")
        if b<33:
            d[a] = "Failed!"
        else:
            d3[a] = "Passed!"
        d2[a] = b

    print('List of PASSED students :')
    for k3, v3 in d3.items():
        print(k3, "-", v3)
    print("")

    print('List of FAILED students :')
    for k, v in d.items():
        print(k, "-", v)

result(cls)
