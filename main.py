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
    
    def __init__(self, truck, name):
        self.tank = truck
        self.name = name



def worker(carList,fuelTank, scope):
    if(scope == 1):
        while(fuelTank > 0):
            time.sleep(1)
            
            selectedCar = random.choice(carList)
            print(fuelTank)
            if fuelTank >= selectedCar.tank :  
                fuelTank -= selectedCar.tank
            
                writeLogFile(fuelTank, str( selectedCar.name), 1)
    else:
        return fuelTank        
        
def my_service(truckList, fuelTank, scope):
    if(scope == 1):
        selectedTruck = random.choice(truckList)
        if 1000-fuelTank <= selectedTruck.tank:  
            fuelTank+=truck1.tank
            writeLogFile(fuelTank, str( selectedTruck.name), 0)
    else:
        return fuelTank

def writeLogFile(fuelTank,car, type):
    
    if(not os.path.isfile("log.txt") ):
        f = open("log.txt", "w")
        f.close()
    else:
        f = open("log.txt", "a+")
        if type == 1:
            toWrite = "\n" + "CAR " + car + "\n"+"Fuel tank " + str(fuelTank)
        else:
            toWrite = "\n" + "TRUCK " + car + "\n"+"Fuel tank " + str(fuelTank)
        f.write(toWrite)
        f.close()

if(__name__=="__main__"):
    
    fuelTank = 450 
   
    truck1 = Truck(random.randint(500,800), "1")
    truck2= Truck(random.randint(500,800), "2")
    truck3 = Truck(random.randint(500,800), "3")
    
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
    
    truckList = []
    truckList.append(truck1)
    truckList.append(truck2)
    truckList.append(truck3)

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
    y = threading.Thread(target = my_service, args = (truckList, fuelTank, 1))
    x.start()
    fuelTank = worker(fuelTank, carList, 0)

    
    
        
            