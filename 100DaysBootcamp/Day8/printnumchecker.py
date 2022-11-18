#Write your code below this line 👇

def prime_checker(number):
    # A prime number is a number that is evenly divisible by 1 and itself. 
    # Check if the number is divisible by any number but one and itself:
    # if number == 1:
    #     print("It's not a prime number.")
    # elif number != 2 and number % 2 == 0:
    #     print("It's not a prime number.")
    # elif number != 3 and number % 3 == 0:
    #     print("It's not a prime number.")
    # else:
    #     print("It's a prime number.")

    #Alternate version
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False    
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)