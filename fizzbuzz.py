import sys

if (len(sys.argv) == 2):
    try:
        upper_limit = int(sys.argv[1])
    except ValueError:
        print("You need to supply a numeric value. Please try again.")
        upper_limit = int(input("Please input an upper limit: "))

else:
    try:
        upper_limit = int(input("Please input an upper limit: "))
    except ValueError:
        print("You need to supply a numeric value. Please try again.")
        upper_limit = int(input("Please input an upper limit: "))
    
m=1

print("Fizzbuzz counting up to", upper_limit)

while (m!=(upper_limit+1)):
    if (m%3 == 0 and m%5 == 0):
        print("fizzbuzz")
    elif (m%3 == 0):
        print("fizz")
    elif (m%5 == 0):
        print("buzz")
    else:
        print(m)
    m+=1
    