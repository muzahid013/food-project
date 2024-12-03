fav_food = []

while True:
    print('\nFavourite food manager..')
    print('\t0. Exit')
    print('\t1. Add new food')
    print('\t2. Remove any food')
    print('\t3. View all favourite foods.')
    choice = input("\nEnter your choice: \n")
    
    if choice == "0":
        print("Thanks for using favourute food manager.")
        break
    elif choice == "1":
        food = input('Type a food name to add: ')
        fav_food.append(food)
        print(f"{food} added succesfully.......")
    elif choice == "2":
        if not fav_food:
            print("No food available for remove..")
        else:
            food = input('Type a food name to remove: ')
            fav_food.remove(food)
            print(f"{food} removed succesfully.....\n")

    elif choice == "3":
        print('All your favourite foods are.')
        if fav_food:
            for index,value in enumerate(fav_food,start=1):
                print(f"\t{index} {value}")
        else:
            print('\nSorry! food list is empty, did not added yet.')
    else:
        print('Invalid Choice')
    