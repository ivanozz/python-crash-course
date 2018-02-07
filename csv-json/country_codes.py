from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """возвращает для заданной страны ее код в Pygal"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    return None
