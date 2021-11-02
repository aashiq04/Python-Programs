max=int(input())
for n in range(1,max):
    if n%15==0:
        print ("FizzBuzz")
        continue
    elif n%3 == 0:
        print ("Fizz")
        continue
    elif n%5 == 0:
        print ("Buzz")
        continue
    print(n)
    
print("Hello")
