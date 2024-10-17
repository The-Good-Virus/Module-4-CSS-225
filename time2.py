#Lela Parks
#Oct 17, 2024

str_time = input("What time is it now? ")
str_wait_time = input("What is the number of hours to wait? ")

time = int(str_time)
wait_time = int(str_wait_time)

# Calculate the time when the alarm goes off, using modulo 24 to wrap around
time_when_alarm_go_off = (time + wait_time) % 24

# Print the final time
print("The time when the alarm goes off will be:", time_when_alarm_go_off)

#The wait_time is not properly defined causing the code to jam up.

#Check your spelling before you submit the code in to python.

#Use an integer code before you use a string code. An integer uses numeric values while strings
#represent text instead of numbers. For this code you would want to focus on usuing integers 
#since this code focues on time.

#Seperate your print for better clarity for yourself and the code.