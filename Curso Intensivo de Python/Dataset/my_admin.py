class Admin(User):
    def __init__(self, first_name, last_name, age, email, username, privileges=None):
        """Inicializa os atributos da classe-pai, em seguida, inicializa os atributos específicos de um administrador."""
        super().__init__(first_name, last_name, age, email, username)
        self.privileges = Privileges(privileges)


