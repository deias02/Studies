class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa os atributos que descrevem um restaurante."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Atributo padrão

    def describe_restaurant(self):
        """Descreve o restaurante."""
        print("O restaurante " + self.restaurant_name + " serve culinária " + self.cuisine_type + ".")

    def open_restaurant(self):
        """Informa que o restaurante está aberto."""
        print("O restaurante " + self.restaurant_name + " está aberto.")
        
    def set_number_served(self, number):
        """Define o número de clientes atendidos."""
        self.number_served = number

    def increment_number_served(self, increment):
        """Incrementa o número de clientes atendidos."""
        self.number_served += increment

