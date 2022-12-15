import re
elves_snacks_calories = open('C:\Projects\Git\AoC-2022\src\Day1\Day1Input.txt', 'r').readlines()

elf_total_calories = 0
top_three_elves_total_calories = 0
totals = []

for calories_in_a_snack in elves_snacks_calories:    
    if  re.findall('[0-9]', calories_in_a_snack):
        calories_in_a_snack = int(calories_in_a_snack.replace('\n', ''))
        elf_total_calories += calories_in_a_snack               
    else:
        totals.append(elf_total_calories)
        elf_total_calories = 0
totals.append(elf_total_calories)

i = 0
while(i < 3):
    top_three_elves_total_calories += sorted(totals, reverse=True)[i]
    i += 1

print(f'The top three Elves are carrying **{str(top_three_elves_total_calories)}** calories in total.')