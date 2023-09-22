
def decode(string):
    repsonse = ""
    print(string(1, 5))
    # i = 0
    # while i <= len(string):
    #     prefix = string[i]
    #     repsonse += string(i+1, i+1+int(prefix))
    #     i += prefix + 1


def encode(strs):
    response = ""
    for string in strs:
        response += str(len(string)) + string
    decode(response)
    return response


encode(strs=["lint", "code", "love", "you"])
