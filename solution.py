import math

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

def cakes(recipe, available):
    ingredient_amounts=[]
    for recipe_key, recipe_amount in recipe.items():
        for available_key, available_amount in available.items():
            if available_key == recipe_key:
                if available_amount<recipe_amount:
                    return(0)
                else:
                    ingredient_amounts.append(math.trunc(available_amount/recipe_amount))
    return min(ingredient_amounts)
