import random

poss_comp_action = ("Sten", "Sax", "Påse")
win = "Du vinner!"
loss = "Du förlorar :("
print("\nVälkommen till Sten, Sax eller Påse")
while True:    
    comp_action = random.choice(poss_comp_action)
    user_action = input("\nVälj Sten[1], Sax[2] eller Påse[3]: ")    

    if user_action == "1": 
        user_action = "Sten"
    elif user_action == "2":
        user_action = "Sax"
    elif user_action == "3":
        user_action = "Påse"       
    
    elif user_action != "1" or "2" or "3":
        print(f'Felaktigt val. Spela genom att ange "1", "2" eller "3" !')
        play_again = input("Spela igen? (J/N): ")
        if play_again.lower() == "j":
            continue
        break       

    print(f"\nDu valde {user_action}, datorn valde {comp_action}.\n")

    if user_action == comp_action:
        print(f"Båda valde {user_action}. Oavgjort!")    
    elif user_action == "Sten":
        if comp_action == "Sax":
            print(f"Sten krossar sax! {win}")
        else:
            print(f"Påse täcker sten! {loss}")
    elif user_action == "Sax":
        if comp_action == "Påse":
            print(f"Sax klipper påse! {win}")
        else:
            print(f"Sten krossar sax! {loss}")
    elif user_action == "Påse":
        if comp_action == "Sten":
            print(f"Påse täcker sten! {win}")
        else:
            print(f"Sax klipper påse! {loss}")   
    break