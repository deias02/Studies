from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Devolve o código de duas letras do Pygal para um país, dado o seu nome."""
    
    # Casos específicos para países cujos nomes não são automaticamente reconhecidos
    if country_name == 'Yemen, Rep.':
        return 'ye'
    elif country_name == 'Venezuela, RB':
        return 've'
    elif country_name == 'Vietnam':
        return 'vn'
    elif country_name == 'Bolivia':
        return 'bo'
    elif country_name == 'Egypt, Arab Rep.':
        return 'eg'
    elif country_name == 'Gambia, The':
        return 'gm'
    elif country_name == 'Iran, Islamic Rep.':
        return 'ir'
    elif country_name == 'Korea, Dem. Rep.':
        return 'kp'
    elif country_name == 'Korea, Rep.':
        return 'kr'
    elif country_name == 'Macedonia, FYR':
        return 'mk'
    elif country_name == 'Tanzania':
        return 'tz'
    elif country_name == 'Kyrgyz Republic':
        return 'kg'
    elif country_name == 'Hong Kong SAR, China':
        return 'hk'
    elif country_name == 'Macao SAR, China':
        return 'mo'
    
    # Verifica o nome do país no dicionário COUNTRIES do Pygal
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    
    # Se o país não foi encontrado, devolve None
    return None

# Exemplo de como você pode testar isso:
get_country_code('Afghanistan')  # Deve retornar 'af'
get_country_code('Korea, Rep.')  # Deve retornar 'kr'
get_country_code('Invalid Country')  # Deve retornar None
get_country_code('Venezuela, RB')
get_country_code('Bolivia')
get_country_code('Egypt, Arab Rep.')
get_country_code('Gambia, The')
get_country_code('Iran, Islamic Rep.')
get_country_code('Korea, Dem. Rep.')
get_country_code('Macedonia, FYR')
get_country_code('Tanzania')
get_country_code('Kyrgyz Republic')
get_country_code('Hong Kong SAR, China')
get_country_code('Macao SAR, China')
