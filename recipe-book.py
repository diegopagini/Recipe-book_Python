import os
from pathlib import Path
from os import system

my_rute = Path(Path.home(), "recipes")


def count_recipes(path: Path):
    counter = 0
    for _ in Path(path).glob("**/*.txt"):
        counter += 1
    return counter


def init():
    system('cls')
    print(f"""
    {"*" * 50}
     {"*" * 5} Welcome to the recipes administrator {"*" * 5}
    {"*" * 50}""")
    print("\n")
    print(f"The recipes are in {my_rute}")
    print(f"Total of recipes {count_recipes(my_rute)}")

    user_selection = 'x'
    while not user_selection.isnumeric() or int(user_selection) not in range(1, 7):
        print("Choose one option: ")
        print("""
        [1] - Read recipe.
        [2] - Create new recipe.
        [3] - Create new category.
        [4] - Delete a recipe.
        [5] - Delete a category.
        [6] - Finish program.              
        """)
        user_selection = input()
    return int(user_selection)


def show_categories(path: Path):
    print("Categories: ")
    category_path = Path(path)
    category_list = []
    counter = 1

    for folder in category_path.interdir():
        folder_str = str(folder.name)
        print(f"[{counter}] - {folder_str}")
        category_list.append(folder)
        counter += 1

    return category_list


def choose_category(category_list: list):
    selection = 'x'
    while not selection.isnumeric() or int(selection) not in range(1,len(category_list) + 1):
        selection = input("\nChoose a category: ")
    return list[int(selection) - 1]


def show_recipes(path: Path):
    print("Recipes: ")
    recipes_path = Path(path)
    recipes_list = []
    counter = 1
    for recipe in recipes_path.glob('*.txt'):
        recipe_str = str(recipe.name)
        print(f"[{counter}] - {recipe_str}")
        counter += 1
        recipes_list.append(recipe)

    return recipes_list


def choose_recipe(recipes_list: list):
    selection = 'x'
    while not selection.isnumeric() or int(selection) not in range(1, len(recipes_list) + 1 ):
        selection = input("\nChoose a recipe: ")

    return list[int(selection)]


def read_recipe(recipe):
    print(Path.read_text(recipe))


def create_recipe(path: Path):
    exists = False
    while not exists:
        print("Write the name of your recipe: ")
        name = input() + '.txt'
        print("Write tour new recipe: ")
        content = input()
        new_path = Path(path, name)
        if not os.path.exists(new_path):
            Path.write_text(new_path, content)
            print(f"Your recipe {name} has been created.")
            exists = True
        else:
            print("I'm sorry, that recipe already exists.")


def create_category(path: Path):
    exists = False
    while not exists:
        print("Write the name of your category: ")
        name = input()
        new_path = Path(path, name)
        if not os.path.exists(new_path):
            Path.mkdir(new_path)
            print(f"Your category {name} has been created.")
            exists = True
        else:
            print("I'm sorry, that category already exists.")


def delete_recipe(recipe):
    Path(recipe).unlink()
    print(f"Your recipe: {recipe.name} has been deleted")


def delete_category(category):
    Path(category).rmdir()
    print(f"Your category: {category.name} has been deleted")


def return_main_menu():
    election = 'x'
    while election.lower() != 'v':
        election = input("\n Press V to return main menu.")


# Show init menu
end_program = False
while not end_program:
    menu = init()

    if menu == 1:
        # show all categories
        my_categories = show_categories(my_rute)
        # choose a category
        my_category = choose_category(my_categories)
        # show all recipes
        my_recipes = show_recipes(my_category)
        if(len(my_recipes) ) < 1:
            print("There are no recipes for this category")
        else:
            # choose a recipe
            my_recipe = choose_recipe(my_recipes)
            # read the recipe
            read_recipe(my_recipe)
        # return to menu
        return_main_menu()

    elif menu == 2:
        # show all categories
        my_categories = show_categories(my_rute)
        # choose a category
        my_category = choose_category(my_categories)
        # create a recipe
        create_recipe(my_category)
        # return to menu
        return_main_menu()

    elif menu == 3:
        # create a category
        create_category(my_rute)
        # return to menu
        return_main_menu()

    elif menu == 4:
        # show all categories
        my_categories = show_categories(my_rute)
        # choose a category
        my_category = choose_category(my_categories)
        # show all recipes
        my_recipes = show_recipes(my_category)
        # choose a recipe
        my_recipe = choose_recipe(my_recipes)
        # delete the recipe
        delete_recipe(my_recipe)
        # return to menu
        return_main_menu()

    elif menu == 5:
        # show all categories
        my_categories = show_categories(my_rute)
        # choose a category
        my_category = choose_category(my_categories)
        # delete a category
        delete_category(my_category)
        # return to menu
        return_main_menu()

    elif menu == 6:
        # finalize
        end_program = True


