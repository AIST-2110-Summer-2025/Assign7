from random import randint

# Complete this function
def get_yesno(prompt):
    ...


# And this one as well
def get_number(prompt):
    ...


# You shouldn't have to modify anything below here...but DO look at the code to
# see how it all works. You're welcome to change it if you want...just make sure
# it still runs when you're done.
def main():
    name = input("What is your name? ")
    
    if not name:                        # same as `if name == None or len(name) == 0`
        print("You can't even answer a simple question. You die.")
        return                          # EARLY RETURN STRATEGY

    print(f"Hello {name}! You silly English knight!")

    cross = get_yesno("Do you want to cross this bridge? ")

    if not cross:                       # same as `if cross == False`
        print(f"Very well {name}. Be on your way!")
        return                          # EARLY RETURN STRATEGY

    print("Okay then. To cross you must answer a very difficult math problem.")
    print("It's very hard. And if you miss it, I will toss you off the bridge")
    print("and you will fall to your certain death.")

    cross = get_yesno("Are you absolutely certain you want to cross this bridge? ")

    if not cross:
        print(f"Very well {name}. Be on your way!")
        return

    num1 = randint(1,10)
    num2 = randint(1,10)

    ans = get_number(f"What do you get when you add {num1} and {num2}? ")

    if ans == num1 + num2:
        print("Oh! You got it right. Fine. Cross and be gone!")
    else:
        print("HA! I got you! (ahhhhhhhhhhhhhhhhh)")


if __name__ == "__main__":
    main()
