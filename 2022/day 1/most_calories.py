"""
Name - Anant luthra
Date - 4/12/22
Purpose - Solving day1 advent of code.
"""

def highest_calories() -> str:

    with open("./inputs/day1.txt") as f:
        data = f.readlines()
        calory_list = []
        calories = 0
        for index, i in enumerate(data):
            if i == "\n":
                calory_list.append(calories)
                calories = 0
            else:
                if index == len(data) - 1:
                    calories += int(i)
                    calory_list.append(calories)
                else:
                    calories += int(i)
    calory_list.sort(reverse=True)

    return calory_list[0]

def top_three_highest() -> str:
    """Returns the sum of top three highest Elves"""

    with open("./inputs/day1.txt") as f:
        data = f.readlines()

        calory_list = []
        calories = 0
        for index, i in enumerate(data):
            if i == "\n":
                calory_list.append(calories)
                calories = 0
            else:
                if index == len(data) - 1:
                    calories += int(i)
                    calory_list.append(calories)
                else:
                    calories += int(i)

    calory_list.sort(reverse=True)
    return calory_list[0] + calory_list[1] + calory_list [2]

if __name__ == "__main__":
    result1 = highest_calories()
    result2 = top_three_highest()
    print(result1, result2)
