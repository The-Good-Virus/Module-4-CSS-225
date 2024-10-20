#Lela Parks
#Oct 15, 2024

# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

# Get the year of origin from the user
year = int(input("Greetings! What is your year of origin? "))

# Greet the time traveler based on their year of origin
if year < 1900:

    print("Woah, that's the past!")

elif 1900 <= year <= 2024:

    print("That's totally the present!")
    
else:
    print("Far out, that's the future!!")

# Make sure that use close your code fully if you are using ", (), [], or {}
# Using the "&&" sign for your python will confuse it or try overlapping which will result in an error when used incorrectly
