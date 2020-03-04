'''#1___________________________________________
topping = ''
while topping != 'quit':
    topping = input("Insert your pizza topping: ")
    if topping != 'quit' and topping != '':
        print("-------------->You just added " + topping + " to your pizza.<-------------------")
    
#2___________________________________________
age = 0
while age != -1:
    age = int(input("Insert the customer age: (-1 to quit): "))   #not validated for negative numbers
    if age < 3:
        print("Free ticket for you.")              
    elif age < 12:
        print("10$ ticket cost")
    else:
        print("15$ ticket cost")

#3__________________________________________
age = 0
iteration = 0                            #iteration counter
while age != -1:
    iteration += 1
    age = int(input("Insert the customer age: (-1 to quit): "))    
    if age < 3:
        print("Free ticket for you.")
    elif age < 12:
        print("10$ ticket cost")
    else:
        print("15$ ticket cost")
print('This program iterated ' + str(iteration) + ' times.')


#4____________________________________________
sandwich_orders = ["Tuna Sandwich", "Club Sandwich", "Veggie Sandwich", "Chicken avocado Sandwich"]
finished_sandwiches = []
for sandwich in sandwich_orders:
    print("I made a " + sandwich + ".")
    finished_sandwiches.append(sandwich)      #adding sandwiches we have made
for s in finished_sandwiches:
    print(s + " was made.")
    

#5_____________________________________________
sandwich_orders = ["Tuna Sandwich", "Pastrami Sandwich", "Club Sandwich", "Veggie Sandwich", "PASTRAMI", "Chicken avocado Sandwich", "pastrami sandwich"]
print("We have run out of Pastrami =(")
for s in sandwich_orders:
    if s.lower().find('pastrami') == 0:      #finding pastrami substring in our list
        sandwich_orders.remove(s)            #removing element
print(sandwich_orders)

'''
#6____________________________________________
poll = {}
place = ''
while place != 'Quit':   #upper Q because of title for input
    place = input("If you could visit one place in the world, where would you go?: ").title()
    if place == 'Quit':
        break;
    if place in poll:
        poll[place] += 1
    else:
        poll[place] = 1
print("Poll results: ")
print(poll)
