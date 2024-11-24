
class Car(): 
    """Uma tentativa simples de representar um carro."""
    def __init__(self, make, model, year): 
        self.make = make 
        self.model = model 
        self.year = year 
        self.odometer_reading = 0
        
    def get_descriptive_name(self): 
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()
    
    def read_odometer(self): 
        print("Este carro tem " + str(self.odometer_reading) + " milhas.")
        
    def update_odometer(self, mileage): 
        if mileage >= self.odometer_reading: 
            self.odometer_reading = mileage 
        else: 
            print("Você não pode retroceder o hodômetro!")
        
    def increment_odometer(self, miles): 
        self.odometer_reading += miles

        


    