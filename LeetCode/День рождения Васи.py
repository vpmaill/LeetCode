numOfDishes = int(input())
dishes = {}
for i in range(numOfDishes):
    nameOfDish, amount, numOfIngredients = input().split()
    dishes[nameOfDish] = {"amount": int(amount)}
    for j in range(int(numOfIngredients)):
        nameOfIngredient, amountOfIngredient, unit = input().split()
        dishes[nameOfDish][nameOfIngredient] = [int(amountOfIngredient), unit]

numOfIngredients = int(input())
Price = {}
for i in range(numOfIngredients):
    name, price, amount, unit = input().split()
    Price[name] = [int(price), int(amount), unit]

numOfIngredients = int(input())
KBJU = {}
for i in range(numOfIngredients):
    name, amount, unit, prot, fats, carboh, kkal = input().split()
    KBJU[name] = {"amount": [amount, unit], "prot": prot, "fats": fats, "carboh": carboh, "kkal": kkal}

numOfIngredientsAtAll = {}
for i in dishes:
    amount = 0
    for j in dishes[i]:
        if j == "amount":
            amount = dishes[i][j]
        else:
            if j in numOfIngredientsAtAll:
                numOfIngredientsAtAll[j][0] += amount * dishes[i][j][0]
            else:
                numOfIngredientsAtAll[j] = [amount * dishes[i][j][0], dishes[i][j][1]]


