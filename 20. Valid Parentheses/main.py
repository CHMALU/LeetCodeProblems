def isValid(s='()'):
    lista = []
    for litera in s:
        if litera in "({[":
            lista.append(litera)
        else:
            if len(lista) == 0:
                return False
            if litera == ')' and lista[-1] == "(":
                lista.pop()
            elif litera == '}' and lista[-1] == "{":
                lista.pop()
            elif litera == ']' and lista[-1] == "[":
                lista.pop()
            else:
                return False
    if len(lista) == 0:
        return True
    else:
        return False


print(isValid())
