def city_country(city, country, population=None):
    """Devolve uma string formatada como 'Cidade, País – população xxx'."""
    if population:
        return city.title() + ", " + country.title() + " – população " + str(population)
    else:
        return city.title() + ", " + country.title()