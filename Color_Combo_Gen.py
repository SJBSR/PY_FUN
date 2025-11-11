# Random color generator
import random

colors_list = ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange', 'Pink', 'Brown', 'Black', 'White']

# Random color generator to append to above printed color
color_combo_list = ['Cyan', 'Magenta', 'Lime', 'Teal', 'Violet', 'Indigo', 'Gold', 'Silver', 'Maroon', 'Navy']

random_color = random.choice(colors_list) + " & " + random.choice(color_combo_list)
print(f"Your random color combination is: {random_color}")
