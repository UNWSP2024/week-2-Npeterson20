def average_age():
    # Program to calculate the average age of five friends
    age1 = float(input("Enter the age of friend 1: "))
    age2 = float(input("Enter the age of friend 2: "))
    age3 = float(input("Enter the age of friend 3: "))
    age4 = float(input("Enter the age of friend 4: "))
    age5 = float(input("Enter the age of friend 5: "))

# Calculate the average age
    average_age = (age1 + age2 + age3 + age4 + age5) / 5

# Display the average age
    print(f"The average age is {average_age:.2f}")


# Line which calls the above function.
average_age()
