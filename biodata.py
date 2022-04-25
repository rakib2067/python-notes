hometown = "Hackney"

hometown_stats = {
    'land_area': 19.06,
    'population': 280900,
    'male_pop': 140400	,
    'female_pop': 140600,
}


def population_density(population, land_area):
    print(f'Population density = {population/land_area:.2f}')


population_density(hometown_stats['population'], hometown_stats['land_area'])
