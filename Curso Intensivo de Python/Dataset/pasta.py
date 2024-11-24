def make_pasta(size, *toppings):
    """Apresenta a pasta que estamos prestes a preparar."""
    print("\nMaking a " + str(size) + "-inch pasta with the following toppings:")
    
    for topping in toppings:
        print("- " + topping)
        
        