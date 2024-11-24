class Employee:
    """Representa um funcionário."""
    
    def __init__(self, first_name, last_name, annual_salary):
        """Inicializa os atributos do funcionário."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, amount=5000):
        """Adiciona o valor de aumento ao salário anual."""
        self.annual_salary += amount