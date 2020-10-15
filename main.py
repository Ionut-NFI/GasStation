import random
import threading
import time
import os

exitFlag = 0

class Car:
    
    def __init__(self, carTank, name):
        self.tank = carTank
        self.name = name

class Truck:
    
    def __init__(self, truck):
        self.tank = truck



def worker(carList,fuelTank, scope):
    if(scope == 1):
        while(fuelTank > 0):
            time.sleep(3)
            
            selectedCar = random.choice(carList)
            print(fuelTank)
            if fuelTank >= selectedCar.tank :  
                fuelTank -= selectedCar.tank
            
                writeLogFile(fuelTank, str( selectedCar.name))
    else:
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
    
def writeLogFile(fuelTank,car):
    if(not os.path.isfile("log.txt") ):
        f = open("log.txt", "w")
        f.close()
    else:
        f = open("log.txt", "a+")
        toWrite = "\n" + "CAR " + car + "\n"+"Fuel tank " + str(fuelTank)
        f.write(toWrite)
        f.close()

if(__name__=="__main__"):
    
    fuelTank = 450 
   
    truck1 = Truck(random.randint(500,800))
    truck2= Truck(random.randint(500,800))
    truck3 = Truck(random.randint(500,800))
    
    car1 = Car(1, "1")
    car2 = Car(random.randint(50,80), "2")
    car3 = Car(random.randint(50,80), "3")
    car4 = Car(random.randint(50,80), "4")
    car5 = Car(random.randint(50,80), "5")
    
    carList = []
    carList.append(car1)
    carList.append(car2)
    carList.append(car3)
    carList.append(car4)
    carList.append(car5)
    
    print("Fuel capacity for gas station "+ str(fuelTank))
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
    
        
    x = threading.Thread(target = worker, args = (carList,fuelTank,1,))
    #y = threading.Thread(target = my_service)
    x.start()
    fuelTank = worker(fuelTank, carList, 0)

    if fuelTank == 0:
        x.kill()    
        print("FINISH")    
    
        
            