from account import Account
from car import Car

if __name__ == "__main__":
    print("Hola Mundo")
    car = Car("RMK167", Account("Gustavito", "5.731.478"))
    print(vars(car.driver))