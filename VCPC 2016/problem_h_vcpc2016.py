num = int(input())

words = []
strength = []
doneInputs = []
flag = False

for i in range(num):
    temp0 = input()
    if temp0 in doneInputs:
        flag = True
    else:
        doneInputs.append(temp0)

    # print(doneInputs)
    if not flag:
        temp = temp0.split()
        if temp[0] not in words:
            words.append(temp[0])
            strength.append(1)
        else:
            strength[words.index(temp[0])] += 1

        if temp[1] not in words:
            words.append(temp[1])
            strength.append(0)
    else:
        flag = False

#print(words)
#print(strength)
finalArray = []

for i in range(len(words)):
    finalArray.append([words[i],strength[i]])
    #print(finalArray)
finalArray = sorted(finalArray, key=lambda finalArray: finalArray[0], reverse = True)
finalArray = sorted(finalArray, key=lambda finalArray: finalArray[0])

for i in range(len(words)-1,-1,-1):
    if(finalArray[i][1]==0):
        break
    print(finalArray[i][0])
