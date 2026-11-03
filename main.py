print("MYSTERY ISLAND")

name = input("What is your name? ").strip()
while name == "":
    print("Please type a name.")
    name = input("What is your name? ").strip()
print("Welcome,", name)

location = "Beach"

while True:
    choice = input("1 = look around, 2 = go to the jungle, q = quit: ").strip().lower()
    if choice == "1":
        print("You are at the", location)
    elif choice == "2":
        location = "Jungle"
        print("Thick vines hang around you. Welcome to the jungle.")
    elif choice == "q":
        print("see ya later")
        break
    else:
        print("Not a valid choice, try again")