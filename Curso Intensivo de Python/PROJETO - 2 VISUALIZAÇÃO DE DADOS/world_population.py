import json
import pygal
from pygal.maps.world import World
from country_codes import get_country_code

# Carrega os dados em uma lista
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Constrói um dicionário com dados das populações
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        
        if code:
            cc_populations[code] = population

# Cria um mapa mundial e adiciona as populações
wm = World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)

# Salva o mapa em um arquivo
wm.render_to_file('world_population.svg')