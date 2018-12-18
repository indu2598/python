name , char = input("Enter name and character comma seprated:").split(",")
print(f"The length of name is {len(name)}")
# print(f"lower name is {name.lower()}")
print(f"number of count of char in variable: {name.lower().count(char.lower())}")