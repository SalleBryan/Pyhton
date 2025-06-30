while True:
    print("Who are you?")
    name = input("> ")
    if (name != "The Saint") and (name != "Joe"):
        continue
    print(f"Hello, {name}. What's the password? (It's a fish)")
    password = input("> ")
    if password == "swordfish":
        break
print("Access Granted")