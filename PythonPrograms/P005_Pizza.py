
print('1.Small(150) 2.Medium(250) 3.Large(500)')
choice = int(input('enter your selection: '))
qty = int(input('enter quantity: '))
match choice:
    case 1:
        bill = qty * 150
        print(bill)
    case 2:
        bill = qty * 250
        print(bill)
    case 3:
        bill = qty * 500
        print(bill)
    case _:
        print('Invalid choice')

# small -> 4 => offer 500 ml coke free
# medium-> 3 => 1ltr coke free
# large -> 2 => 1ltr coke + ice cream





