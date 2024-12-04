# Define custom exceptions
class SofaIsDamaged(Exception):
    pass

class FishIsUnderAttack(Exception):
    pass

class CatIsHungry(Exception):
    pass

# Define the Cat class
class Cat:
    def sharpen_claws(self):
        raise SofaIsDamaged("Oh no! The sofa is damaged..")
    
    def drink_water_from_aquarium(self):
        raise FishIsUnderAttack("The fish is under attack!")
    
    def say_meow(self):
        raise CatIsHungry("The cat is hungry!")
    
    def sleep(self):
        print("zZz")

# Main function
def main():
    my_cat = Cat()
    try:
        my_cat.say_meow()
        my_cat.sharpen_claws()
        my_cat.drink_water_from_aquarium()
    
    except SofaIsDamaged as e1:
        print(f"Caught exception:", e1)
    except FishIsUnderAttack as e2:
        print(f"Caught exception:", e2)
    except CatIsHungry as e3:
        print(f"Caught exception:", e3)
    finally:
        my_cat.sleep()  

# Run the main function
if __name__ == "__main__":
    main()
