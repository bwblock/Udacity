#
# Find the one food that is eaten by only one animal.
#
# The animals table has columns (name, species, birthdate) for each individual.
# The diet table has columns (species, food) for each food that a species eats.
#

QUERY = '''


select diet.food, count(*) as num from animals join diet on animals.species = diet.species group by diet.food having num =1;

'''

