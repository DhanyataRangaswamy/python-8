class Ford():
    def Max_speed(self):
        print("Max speed id 216 mph")

    def Mileage(self):
        print("Mileage of ford id 14.8 kmpl")

    def year(self):
        print("Established in 1903")

class Honda():
    def Max_speed(self):
        print("Max speed id 19 mph")

    def Mileage(self):
        print("Mileage of honda is 16 kmpl")

    def year(self):
        print("Established in 2001")

obj_f=Ford()
obj_h=Honda()

for Vehical in (obj_f , obj_h):
    Vehical.Max_speed()
    Vehical.Mileage()
    Vehical.year()