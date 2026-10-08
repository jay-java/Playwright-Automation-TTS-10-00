d = {
    1: "c",
    2: "c++",
    3: "java"
}
value = input("Enter value to search: ")
# Check whether value exists in dictionary
if value in d.values():
    print("Yes, value exists in dictionary.")
else:
    print("No, value does not exist.")
    choice = input("Do you want to add it? (Y/n): ")
    if choice.lower() == "y":
        new_key = max(d.keys()) + 1
        d[new_key] = value
        print("Value added successfully.")
        print("New dictionary:", d)
    elif choice.lower() == "n":
        print("Original dictionary:", d)
    else:
        print("Invalid choice.")