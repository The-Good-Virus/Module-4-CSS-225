#Lela Parks
#Oct 17, 2024

currentTimeStr = input("What is the current time (in hours 0-23)? ")
waitTimeStr = input("How many hours do you want to wait? ")

# Convert input strings to integers
currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

# Calculate final time, using modulo 24 to wrap around
finalTimeInt = (currentTimeInt + waitTimeInt) % 24

# Print the final time
print("The final time will be:", finalTimeInt)

#Parentheses's have to be closed at ALL TIMES!

#The variable names need to be corrected from current_time_str to
#currentTimeStr

#If you want the 24 hours to be wrapped add a modulo opperation

#The print statment needs to be corrected so the code can flow correctly
#This is the correct print "finalTimeInt"