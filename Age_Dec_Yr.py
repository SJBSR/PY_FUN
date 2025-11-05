age = int(input("How old are you?\n"))

# Convert age to whole number using (//)
decades = age // 10
# Get the remaining using modulus (%)
years = age % 10
# Print the result
print("You are approximately " + str(decades) + " decades and " + str(years) + " years old.")