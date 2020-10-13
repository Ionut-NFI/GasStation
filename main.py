import random
import threading
import time

exitFlag = 0

class Car:
    
    def __init__(self, carTank):
        self.tank = carTank

class Truck:
    
    def __init__(self, truck):
        self.tank = truck



def worker(fuelTank,carList):
    
    selectedCar =random.choice(carList) 
    
    if fuelTank >= selectedCar.tank :  
        fuelTank -= selectedCar.tank
        print(selectedCar)
        
    
        
    return fuelTank

def my_service():
    if 1000-fuelTank <= truck1.tank:  
        fuelTank+=truck1.tank
        print("truck 1")
    
    if 1000-fuelTank <= truck2.tank:  
        fuelTank+=truck2.tank
        print("truck 2")

    if 1000-fuelTank <= truck3.tank:  
        fuelTank+=truck3.tank
        print("truck 3")
    

if(__name__=="__main__"):
    global fuelTank 
    fuelTank = 100 
    
    truck1 = Truck(random.randint(500,800))
    truck2= Truck(random.randint(500,800))
    truck3 = Truck(random.randint(500,800))
    
    car1 = Car(1)
    car2 = Car(random.randint(50,80))
    car3 = Car(random.randint(50,80))
    car4 = Car(random.randint(50,80))
    car5 = Car(random.randint(50,80))
    
    
    q = True
    print("Fuel capacity for car1 "+ str (car1.tank))
    print("Fuel capacity for car2 "+ str (car2.tank))
    print("Fuel capacity for car3 "+ str (car3.tank))
    print("Fuel capacity for car4 "+ str (car4.tank))
    print("Fuel capacity for car5 "+ str (car5.tank))
    
    print("Fuel capacity for truck1 "+ str (truck1.tank))
    print("Fuel capacity for truck2 "+ str (truck2.tank))
    print("Fuel capacity for truck3 "+ str (truck3.tank))
    
    
    print("--------------------------------")
    time.sleep(3)
    
    while(q):
        x = threading.Thread(target = worker, args = (fuelTank,carList,))
        y = threading.Thread(target = my_service)
        x.start()
        #fuelTank = worker(fuelTank)
        print("------ FUEL TANK------ " + str(fuelTank))
        time.sleep(2)
        q = False
        
            