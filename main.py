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



def worker():
    if 1000-fuelTank >= car1.tank:  
        fuelTank -= car1.tank
        
    if 1000-fuelTank >= car2.tank:  
        fuelTank -= car2.tank
        
    if 1000-fuelTank >= car3.tank:  
        fuelTank -= car3.tank
        
    if 1000-fuelTank >= car4.tank:  
        fuelTank -= car4.tank
        
    if 1000-fuelTank >= car5.tank:  
        fuelTank -= car5.tank

def my_service():
    if 1000-fuelTank <= truck1.tank:  
        fuelTank+=truck1.tank
        truck1.tank = str(random.randint(500,800))
    
    if 1000-fuelTank <= truck2.tank:  
        fuelTank+=truck2.tank
        truck2.tank = str(random.randint(500,800))

    if 1000-fuelTank <= truck3.tank:  
        fuelTank+=truck3.tank
        truck3.tank = str(random.randint(500,800))
    
    # print (threading.currentThread().getName(), 'Exiting')

   # t = threading.Thread(name='my_service', target=my_service)
   # w = threading.Thread(name='worker', target=worker)
    #w2 = threading.Thread(target=worker) # use default name
if(__name__=="__main__"):
    fuelTank = 1000 ;
    
    truck1 = Truck(random.randint(500,800))
    truck2= Truck(random.randint(500,800))
    truck3 = Truck(random.randint(500,800))
    
    car1 = Car(1)
    car2 = Car(random.randint(50,80))
    car3 = Car(random.randint(50,80))
    car4 = Car(random.randint(50,80))
    car5 = Car(random.randint(50,80))
 

    print(car5.tank)