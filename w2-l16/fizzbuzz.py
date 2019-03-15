#/usr/bin/python3

for num in range(1,100):
    # if divisible by 3    
    if num % 3 == 0:
        print(f'Fizz',end='')
    # if divisible by 5 
    if num % 5 == 0:
        print(f'Buzz',end='')
    # if NOT divisible by 3 and 5    
    if num % 5 and num % 3:
        print(f"{num}",end='')
    # newline
    print ('')
