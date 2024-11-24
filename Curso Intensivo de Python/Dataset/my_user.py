class User:
    def __init__(self, first_name, last_name, age, email, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        print("Nome: " + self.first_name + " " + self.last_name)
        print("Idade: " + str(self.age))
        print("Email: " + self.email)
        print("Nome de usuário: " + self.username)

    def greet_user(self):
        print("Olá, " + self.first_name + " " + self.last_name + "! Seja bem-vindo(a).")

    def increment_login_attempts(self):
        """Incrementa o valor de login_attempts em 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reinicia o valor de login_attempts para 0."""
        self.login_attempts = 0