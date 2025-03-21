class Solution:
    # Topological sorting - Graph + BFS approach
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        remaining_ingredients = {}
        needed_for = {}

        for recipe, ingredient_list in zip(recipes, ingredients):
            remaining_ingredients[recipe] = len(ingredient_list)

            for ing in ingredient_list:
                if ing not in needed_for:
                    needed_for[ing] = []
                needed_for[ing].append(recipe)
            
        available = deque(supplies)
        result = []

        while available:
            item = available.popleft()

            if item in needed_for:
                for recipe in needed_for[item]:
                    remaining_ingredients[recipe] -= 1
                    if remaining_ingredients[recipe] == 0:
                        result.append(recipe)
                        available.append(recipe)
                    
                
            
        return result


    def findAllRecipes1(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        result = []
        haspmap = {}

        for i in range(len(recipes)):
            
            recipe = recipes[i]
            ingredient = ingredients[i]
          
            isAllIng = True

            for ing in ingredient:
                if ing not in supplies:
                    print("in: ",ingredient )
                    isAllIng = False;

            if isAllIng:
                result.append(recipe)
                supplies.append(recipe)


        print("result:", result)
        return result