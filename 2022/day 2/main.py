"""         1|2  Score
Rock        A X   1
Paper       B Y   2
Scissors    C Z   3
"""


#Getting the data.
with open("./inputs/day2.txt") as f:
    data = f.readlines()


def total_score(data:list[str]) -> int:
    """  POINTS GIVEN ON SITUATIONS --
    1-Rock, 2-Paper, 3-Scissors
    0-Lost, 3-Draw, 6-Won 
    """

    total_score = 0

    my = 0
    computer = 0
    for index, i in enumerate(data):
        if index == len(data) - 1:
            i += "\n"

        for k in i:
            if k == "A":
                computer += 1
            elif k == "B":
                computer += 2
            elif k == "C":
                computer += 3
            elif k == "X":
                my += 1
            elif k == "Y":
                my += 2
            elif k == "Z":
                my += 3
        
        if my == computer:
            my += 3
            total_score += my

        elif computer == 1 and my == 2:
            my += 6
            total_score += my
        
        elif computer == 3 and my == 1:
            my += 6
            total_score += my

        elif computer == 2 and my == 3:
            my += 6
            total_score += my
        
        else:
            total_score += my
        my = 0
        computer = 0   

    return total_score

def total_score2(data:list[str]) -> int:
    
    
    """  POINTS GIVEN ON SITUATIONS --
    1-Rock, 2-Paper, 3-Scissors
    0-Lost, 3-Draw, 6-Won 

    """
    total_score = 0

    my = 0
    computer = 0
    for index, i in enumerate(data):
        if index == len(data) - 1:
            i += "\n"

        for k in i:
            if k == "A":
                computer += 1
            elif k == "B":
                computer += 2
            elif k == "C":
                computer += 3
            elif k == "X":
                total_score += 1
                break
            elif k == "Y":
                my += computer
                total_score += my + 3
                break
            elif k == "Z":
                if computer == 1:
                    total_score += 2 + 6
                elif computer == 2:
                    total_score += 3 + 6
                else:
                    total_score += 7

        my = 0
        computer = 0   

    return total_score

if __name__ == "__main__":
    result1 = total_score(data)
    result2 = total_score2(data)
    print(result2)
