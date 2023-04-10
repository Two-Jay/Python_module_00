
# * cookbook_dictionary
# --------------------------------------------------------------------------
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

# * print helper
# --------------------------------------------------------------------------
def print_header_options():
    for key, value in cookBook_prompt_options.items():
        print(f"  {key}: {value[0]}")

def print_header():
    print("Welcome to the Python Cookbook !\nList available options:")
    print_header_options()


def print_recipe():
    recipe_name = input('Enter a recipe name: ')
    print_recipe_impl(recipe_name)

def print_recipe_impl(recipe_name):
    if recipe_name in cookbook:
        print(f"Recipe for {recipe_name}:")
        print(f"  Ingredients list: {cookbook[recipe_name]['ingredients']}")
        print(f"  To be eaten for {cookbook[recipe_name]['meal']}.")
        print(f"  Takes {cookbook[recipe_name]['prep_time']} minutes of cooking.")
    else:
        print('This recipe does not exist')

def print_cookbook():
    if len(cookbook) > 0:
        print('Here is the list of recipes in Python Cookbook: ')
        for key, value in cookbook.items():
            print(f"  - {key}")
    else:
        print('this Cookbook is empty')

# * feature helper
# --------------------------------------------------------------------------
def add_recipe_impl(recipe_name, ingredients, meal, prep_time):
    cookbook[recipe_name] = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time
    }

def get_input_ingrediants():
    print('Enter an ingredients: ')
    ingredients = []
    while True:
        ingredient = input()
        if ingredient == '':
            break
        ingredients.append(ingredient)
    return ingredients

def add_recipe():
    recipe_name = input('Enter a name: ')
    if recipe_name in cookbook:
        print('The recipe you entered already exists.')
        return 
    ingredients = get_input_ingrediants()
    meal = input('Enter a meal type: ')
    prep_time = input('Enter a preparation time in minutes: ')
    add_recipe_impl(recipe_name, ingredients, meal, prep_time)

def delete_recipe():
    recipe_name = input('Enter a recipe name: ')
    delete_recipe_impl(recipe_name)

def delete_recipe_impl(recipe_name):
    if recipe_name not in cookbook:
        print('The recipe you entered does not exist.')
        return
    del cookbook[recipe_name]

def quit():
    exit('Cookbook closed. Goodbye!')

# * main
# --------------------------------------------------------------------------
cookBook_prompt_options = {
    '1': ['Add a recipe', add_recipe],
    '2': ['Delete a recipe', delete_recipe],
    '3': ['Print a recipe', print_recipe],
    '4': ['Print the cookbook', print_cookbook],
    '5': ['Quit', quit],
    '-help': ['print options again', print_header_options]
}

def main():
    print_header()
    while True:
        choice = input("Please select an option (to print options : '-help'): ")
        if choice in cookBook_prompt_options:
            function = cookBook_prompt_options[choice][1]
            function()
        else:
            print('This option does not exist, please type the corresponding number.')

if __name__ == "__main__":
    main()
