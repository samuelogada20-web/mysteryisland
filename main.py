print("MYSTERY ISLAND")

name = input("What is your name? ").strip()
while name == "":
    print("Please type a name.")
    name = input("What is your name? ").strip()
print("Welcome,", name)

location = "Beach"

while True:
    choice = input("Type 1 to look around, or q to quit: ").strip().lower()
    if choice == "1":
        print("You are at the", location)
    elif choice == "q":
        print("see ya later")
        break
    else:
        print("Not a valid choice, try again")