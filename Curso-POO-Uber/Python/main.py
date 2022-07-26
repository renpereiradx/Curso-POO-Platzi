from account import Account
from car import Car
from uberX import UberX

if __name__ == "__main__":
    print("Hola Mundo")
    car = Car("RMK167", Account("Gustavito", "5.731.478"))
    print(vars(car.driver))
    uberX = UberX("DLE943", Account("Andres Peralta", "3.846.157"), "Toyota", "Corolla")
    print(vars(uberX.driver))