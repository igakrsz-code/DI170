#exercise-1 
my_fav_numbers = {3, 7, 21} 
my_fav_numbers.add(42)
my_fav_numbers.add(99)
my_fav_numbers.remove(99)

friend_fav_numbers = {5, 7, 13}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)


#exercise-2
my_tuple = (1, 2, 3)
my_tuple = my_tuple + (4, 5)
print("Updated tuple:", my_tuple)


#exercise-3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apples_count = basket.count("Apples")
basket.clear()
print("Final state of the list:", basket)


#exercise-4
float_list = [i/2 for i in range(3, 11)] 
print("List of floats and integers:", float_list)


#exercise-5
for i in range(1, 21):
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


#exercise-6
name = "Iga"
if not name.isdigit() and len(name) >= 3:
    print("Thank you")


#exercise-7
favorite_fruits = ["apple", "banana", "mango"]
fruit_choice = "apple"
if fruit_choice in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")


#exercise-8
toppings = ["cheese", "mushrooms", "pepperoni"]
for topping in toppings:
    print(f"Adding {topping} to your pizza.")

total_cost = 10 + 2.5 * len(toppings)
print("Toppings added:", toppings)
print("Total cost: $", total_cost)


#exercise-9
ages = [2, 5, 15]  
total_cost = 0
for age in ages:
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
    total_cost += cost

# Bonus
teen_ages = [15, 16, 18, 22]
allowed_ages = [age for age in teen_ages if 16 <= age <= 21]
print("Allowed attendees:", allowed_ages)
