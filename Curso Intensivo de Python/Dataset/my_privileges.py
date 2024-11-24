class Privileges:
    def __init__(self, privileges=None):
        """Inicializa os atributos dos privilégios."""
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        """Mostra os privilégios do administrador."""
        print("\nPrivilégios do administrador:")
        for privilege in self.privileges:
            print("- " + privilege)