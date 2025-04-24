from pet import Pet

def main():
    my_pet = Pet("Pixel")
    
    
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    
    
    my_pet.get_status()
    
    
    my_pet.train("Sit")
    my_pet.train("Roll Over")
    my_pet.train("Fetch")
    
    
    my_pet.show_tricks()

if __name__ == "__main__":
    main()
