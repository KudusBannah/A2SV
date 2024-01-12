class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        def dfs(curr, visited):
            if curr not in adj_list:
                return False
            if curr in visited:
                return False
            visited.add(curr)

            for item in adj_list[curr]:
                if item not in supplies and not dfs(item, visited):
                    return False
            
            supplies.add(curr)
            return True

        supplies = set(supplies)

        adj_list = defaultdict(list)
        for i in range(len(recipes)):
            adj_list[recipes[i]].extend(ingredients[i])

        output = []
        for recipe in recipes:
            if dfs(recipe, set()):
                output.append(recipe)

        return output

