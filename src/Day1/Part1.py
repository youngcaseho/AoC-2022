elves_snacks_calories = open('C:\Projects\Local\AoC\Day1\Day1Input.txt', 'r')

most_calories = 0
elf_snacks_total_calories = 0

for calories_in_a_snack in elves_snacks_calories:    
    if calories_in_a_snack != '\n':
        calories_in_a_snack = int(calories_in_a_snack.replace('\n', ''))
        elf_snacks_total_calories += calories_in_a_snack
    else:
        if elf_snacks_total_calories > most_calories:
            most_calories = elf_snacks_total_calories   
        elf_snacks_total_calories = 0
print(f'The Elf with the most calories is carrying **{str(most_calories)}** calories.')
    
