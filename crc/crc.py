def crcCheck(data,div):
    lengthData = len(div)
    ct = 0
    data = [int(i) for i in data]
    div = [int(i) for i in div]
    zero = [0 for i in range(lengthData)]
    tempData = [data[i] for i in range(lengthData)]
    result = []
    for j in range(len(data) - len(div) + 1):
        print("tmp divide ", tempData)
        msb = tempData[0]
        if msb == 0:
            result.append(0)
            for i in range(lengthData, -1, -1 , -1):
                tempData[i] = tempData[i] ^ zero[i]
        else:
            result.append(1)
            for i in range(lengthData, -1, -1, -1):
                tempData[i] = tempData[i] ^ div[i]

        tempData.pop(0)
        if(lengthData + j < len(data)):
            tempData.append(data[lengthData + j])
    
    crc = tempData
    print("Quotient :",result, "remainder ",crc)
    return crc

while 1 > 0:
    print("enter data")
    data = input()
    