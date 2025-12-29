def indexOfMax(list, startIndex, length):
    # aux = startIndex
    # res = startIndex
    # while aux < length:
    #     if list[res] < list[aux]:
    #         res = aux
    #     aux += 1

    # return res

    res = startIndex

    for i in range(startIndex + 1, length):
        if list[res] < list[i]:
            res = i
    
    return res

def bankJoltage(bank):
    firstBattery = indexOfMax(bank, 0, len(bank) - 1)
    secondBattery = indexOfMax(bank, firstBattery + 1, len(bank))
    joltage = int(bank[firstBattery] + bank[secondBattery])
    
    return joltage

def totalJoltage(banks):
    return sum(map(bankJoltage, banks))

if __name__ == '__main__':
    with open('03.in', 'r') as file:
        inputText = file.read()
    
    banks = inputText.split('\n')

    print(totalJoltage(banks))
