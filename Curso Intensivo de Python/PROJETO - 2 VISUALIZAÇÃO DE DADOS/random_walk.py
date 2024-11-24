from random import choice

class RandomWalk:
    """Uma classe para gerar passeios aleatórios."""

    def __init__(self, num_points=5000):
        """Inicializa os atributos de um passeio."""
        self.num_points = num_points

        # Todos os passeios começam em (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Determina a direção e a distância para um passo."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        step = direction * distance
        return step

    def fill_walk(self):
        """Calcula todos os pontos do passeio."""
        
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # Rejeita movimentos que não vão a lugar nenhum.
            if x_step == 0 and y_step == 0:
                continue

            # Calcula os próximos valores de x e y.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)