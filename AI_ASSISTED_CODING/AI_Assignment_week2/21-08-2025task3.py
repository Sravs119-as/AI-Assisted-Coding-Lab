def classify_age(age):
    if age<13:
        return "child"
    elif 13<=age<20:
        return "teenager"
    elif 20<=age<60:
        return "adult"
    else:
        return "senior"
try:
    age=int(input("enter age:"))
    print("Category:",classify_age(age))
except ValueError:
    print("Please enter a valid number.")
