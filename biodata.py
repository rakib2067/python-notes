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

# Create a new file.
# Create two variables, one that contains the name of your hometown and one that contains statistics about your hometown.
# Create a function that calculates the population density of your hometown, you might need to add more statistics to your statistics variables now.
# Create a function that returns a sentence telling users the population density of your hometown
# Call the function and print it out.
# What happens if there is no hometown variable stored, can we put a default in place instead?
# Can you reduce the number of lines of code you’ve written. Spend some time refactoring.
