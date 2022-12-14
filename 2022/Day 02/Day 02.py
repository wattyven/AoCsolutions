filepath = 'Day 02 input.txt'

def openFile(filepath):
    '''reads the raw file'''
    with open(filepath, 'r') as f:
        data = f.readlines()
        data = [i.split() for i in data]
    return(data)

def scoreRound(data):
    '''scores each round in the input file'''
    score = 0
    for i in data:
        if i[0] == 'A':
            if i[1] == 'X':
                score += 4
            elif i[1] == 'Y':
                score += 8
            elif i[1] == 'Z':
                score += 3
        elif i[0] == 'B':
            if i[1] == 'X':
                score += 1
            elif i[1] == 'Y':
                score += 5
            elif i[1] == 'Z':   
                score += 9
        elif i[0] == 'C':
            if i[1] == 'X':
                score += 7
            elif i[1] == 'Y':
                score += 2
            elif i[1] == 'Z':
                score += 6

    return(score)

def scoreRound2(data):
    '''scores each round in the input file according to the new rules'''
    score = 0
    for i in data:
        if i[0] == 'A':
            if i[1] == 'X':
                score += 3
            elif i[1] == 'Y':
                score += 4
            elif i[1] == 'Z':
                score += 8
        elif i[0] == 'B':
            if i[1] == 'X':
                score += 1
            elif i[1] == 'Y':
                score += 5
            elif i[1] == 'Z':   
                score += 9
        elif i[0] == 'C':
            if i[1] == 'X':
                score += 2
            elif i[1] == 'Y':
                score += 6
            elif i[1] == 'Z':
                score += 7
    return(score)

if __name__ == '__main__':
    data = openFile(filepath)
    score = scoreRound(data) # part one
    print(score)
    score2 = scoreRound2(data) # part two
    print(score2)
    
