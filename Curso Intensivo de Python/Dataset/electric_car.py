from my_car import Car

class Battery():
    """Uma tentativa simples de modelar uma bateria para um carro elétrico."""
    def __init__(self, battery_size=70):
        """Inicializa os atributos da bateria."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print("Este carro tem " + str(self.battery_size) + "-kWh de bateria.")
        
    def get_range(self):
        """Exibe uma frase sobre a distância que o carro é capaz de percorrer com essa bateria."""
        if self.battery_size ==70:
            range = 240
        elif self.battery_size ==85:
            range = 270
        
        message = "Este carro pode ir aproximadamente " + str(range)
        message += " quilômetros com a carga cheia."
        print(message)
        
class ElectricCar(Car):
    """Representa aspectos específicos de veículos elétricos"""
    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe pai, em seguida, 
        inicializa os atributos específicos de um carro elétrico
        """
        super().__init__(make, model, year)
        self.battery = Battery()