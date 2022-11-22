"""
allergen corresponds 1 to 1 with ingredient
"""

possible_allergenic_ingredients = dict()
all_ingredients = []

for line in open('input.txt').read().split('\n'):
    ingredients, allergens = line.split(' (contains ')
    allergens = allergens[:-1].split(', ')
    ingredients = set(ingredients.split(' '))

    all_ingredients.extend(ingredients)
    for a in allergens:
        if possible_allergenic_ingredients.get(a, None):
            possible_allergenic_ingredients[a] = possible_allergenic_ingredients[a].intersection(ingredients)
        else:
            possible_allergenic_ingredients[a] = ingredients

# map one on one
allergenic_ingredients = set()
while len(allergenic_ingredients) < len(possible_allergenic_ingredients.keys()):
    for l in possible_allergenic_ingredients.values():
        if len(l) == 1:
            allergenic_ingredients = allergenic_ingredients.union(l)
        else:
            l -= allergenic_ingredients

p1 = 0
for i in all_ingredients:
    if not i in allergenic_ingredients:
        p1 += 1
print(p1)

pair_list = [(key, possible_allergenic_ingredients[key].pop()) for key in possible_allergenic_ingredients.keys()]
pair_list = sorted(pair_list, key=lambda x: x[0])

canonical = ''
for p in pair_list:
    canonical += ',' + p[1]
print(canonical[1:])
