cookbook = {
    "sandwich": {
        'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal' : 'lunch',
        'prep_time' : 10
    },
    "cake": {
        'ingredients' : ['flour', 'sugar', 'eggs'],
        'meal' : 'dessert',
        'prep_time' : 60
    },
    "salad": {
        'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal' : 'lunch',
        'prep_time' : 15
    }
}

def print_recipe(recipe_name):
    if recipe_name in cookbook:
        print(f"Recipe for {recipe_name}:")
        print(f"  Ingredients list: {cookbook[recipe_name]['ingredients']}")
        print(f"  To be eaten for {cookbook[recipe_name]['meal']}.")
        print(f"  Takes {cookbook[recipe_name]['prep_time']} minutes of cooking.")
    else:
        print('This recipe does not exist')

def print_cookbook():
    print('Here is the list of recipes in Python Cookbook: ')
    for key, value in cookbook.items():
        print(f"  - {key}")

def add_recipe(recipe_name, ingredients, meal, prep_time):
    cookbook[recipe_name] = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time
    }

def delete_recipe(recipe_name):
    if recipe_name in cookbook:
        del cookbook[recipe_name]
    else:
        print('This recipe does not exist')

if __name__ == "__main__":
    add_recipe('pizza', ['cheese', 'tomatoes', 'ham'], 'lunch', 30)
    print_cookbook()
    print_recipe('pizza')