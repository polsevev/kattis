message = input()
messageList = list(message)
i = 0
while i < len(messageList) - 1:
    if messageList[i] == "a":
        if messageList[i+1] == "p":
            messageList[i + 1] = ""
        if messageList[i+2] == "a":
            messageList[i + 2] = ""
    elif messageList[i] == "e":
        if messageList[i+1] == "p":
            messageList[i + 1] = ""
        if messageList[i+2] == "e":
            messageList[i + 2] = ""
    elif messageList[i] == "o":
        if messageList[i+1] == "p":
            messageList[i + 1] = ""
        if messageList[i+2] == "o":
            messageList[i + 2] = ""
    elif messageList[i] == "i":
        if messageList[i+1] == "p":
            messageList[i + 1] = ""
        if messageList[i+2] == "i":
            messageList[i + 2] = ""
    elif messageList[i] == "u":
        if messageList[i+1] == "p":
            messageList[i + 1] = ""
        if messageList[i+2] == "u":
            messageList[i + 2] = ""
    i=i+1
message = "".join(messageList)
print(message)