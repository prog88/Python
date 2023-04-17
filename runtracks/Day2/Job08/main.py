# definition
def Evaluate(type, season):
    if type == "fruit" and season == "summer":
        print("pear, strawberry, cassis")
    elif type == "fruit" and season == "winter":
        print("orange, mandarin, kiwi")
    elif type == "vegetable" and season == "summer":
        print("artichoke, eggplant, turnip")
    elif type == "vegetable" and season == "winter":
        print("carrot, artichoke, endive")
    else:
        print("undefined result.")

# evaluate
Evaluate("vegetable", "summer")
Evaluate("vegetable", "winter")
Evaluate("fruit", "summer")
Evaluate("fruit", "winter")
# ---
Evaluate("summer","vegetable")