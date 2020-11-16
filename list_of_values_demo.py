guests = []
name = " "
while name != "DONE":
    name = input("Enter guest name :")
    if name.upper() != "DONE":
        guests.append(name)

print("List of party guests:")
guests.sort()
for guest in guests:
    print(guest)