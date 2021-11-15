ingredients = {'eggs': '2 pcs', 'milk': '60 g', 'salt':'20g'}
print(ingredients['eggs'])


recipe_1 = {
   'name': 'chicken soup',
   'annotation': 'vegetable soup with chicken breast',
   'cooking time':40,
   'number of cooking stages': 2,
   'ingredients':['potato', 'chiken breast', 'salt','carrot','onion'],
   'stages of preparation': {'broth':'pour a saucepan with clean water, put chicken breast in it', 'vegetables':'cut into small pieces'}

}
print(("\033[35m {}" .format(recipe_1)))

recipe_2 = {
   'name': 'hot dog',
   'annotation': 'wheat bun with sausage seasoned with ketchup, mayonnaise, mustard',
   'cooking time':10,
   'number of cooking stages': 3,
   'ingredients':['sausage', 'bun', 'ketchup','mayonnaise'],
   'stages of preparation': {'bun':'Ножом сделать надрез вдоль булочек до половины глубины','sausage': 'Сосиски отварить или поджарить', 'компоновка':'положить сосиски на булочку и залить кетчупов и майонезом по вкусу'}

}
print(("\033[34m {}" .format(recipe_2)))

recipe_3 = {
   'name': 'омлет',
   'annotation': 'нежный омлет с молоком',
   'cooking time':20,
   'number of cooking stages': 3,
   'ingredients':['milk','eggs','milk'],
   'stages of preparation': {'eggs':'разбить яйца в миску', 'milk': 'залить яйца молоком', 'запекание':'взболтать и выложить в форму'}

}
print(("\033[31m {}" .format(recipe_3)))