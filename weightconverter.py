# define the variables and gather input from user

weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
    # converts from L to Kg
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
    # converts from Kg to L
