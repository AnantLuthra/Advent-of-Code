"""
Name - Anant luthra
Date - 4/12/22
Purpose - Solving day1 advent of code.
"""

# reading input data
with open("./inputs/day1.txt") as f:
    data = f.readlines()


def count_calories(data:list[str]) -> list[int]:
    
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
    
    return calory_list


def highest_calories(calories: list[int]) -> int:
    return calories[0]

def top_three_highest(calories: list[int]) -> int:
    """Returns the sum of top three highest Elves"""
    return sum(calories[:3])

if __name__ == "__main__":
    calories = count_calories(data)
    result1 = highest_calories(calories)
    result2 = top_three_highest(calories)
    print(result1, result2)
