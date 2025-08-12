import random

num = random.randint(1,20)

guess = int(input("Can you guess the number I am thinking ? Its less than 20 :"))

            
while num!= guess and count <= attempt :
        if guess > num:
            print("Your guess in higher")
        else:
             print("Your guess is lower")
        
        guess = int(input("Guess again:"))


print("you won!")
                  
                  
