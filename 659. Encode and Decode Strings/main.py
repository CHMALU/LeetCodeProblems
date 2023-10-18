def encode(strs):
    result = ''
    for string in strs:
        result += str(len(string)) + '#' + string
    return result


def decode(string):
    result, i = [], 0

    while i < len(string):
        j = i
        while string[j] != '#':
            j += 1
        length = int(string[i:j])
        result.append(string[j+1: j+1+length])
        i = j + 1 + length
    return result


print(encode(strs=["lint", "code", "love", "you"]))
print(decode(string=encode(strs=["lint", "code", "love", "you"])))

print(encode(strs=["we", "say", ":", "yes"]))
print(decode(string=encode(strs=["we", "say", ":", "yes"])))
