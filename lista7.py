# z1a
def acronim(lista):
    def acronim_rec(remaining, result):
        try:
            return acronim_rec(remaining[1::], result+remaining[0][0])
        except:
            return result
    return acronim_rec(lista, "")

# z1b
def median(lista):
    def median_rec(remaining, result):
        try:
            return median_rec(remaining[1:-1:], result=float(remaining[0]+remaining[-1])/2)
        except:
            return result
    return median_rec(lista, 0)


# z1c
def sqrt_newt(num:float, epsilon):
    def sqrt_newt_rec(num1, num2):
        return num1 if abs(num1*num1 - num)<epsilon else sqrt_newt_rec((num1+num2)/2, num/((num1+num2)/2))
    return sqrt_newt_rec(float(num/2), float(num)/float(num/2))

# z1d
def make_alpha_dict(text:str):
    def make_alpha_dict_rec(remaining, result:dict):
        {result[x].append(remaining[0]) for x in result if remaining[0].__contains__(x)}
        return result if len(remaining)==1 else make_alpha_dict_rec(remaining[1::], result)
    return make_alpha_dict_rec(text.split(), dict([(x,[]) for x in text if x!=' ']))

# z1e
def flatten(origin:list):
    result = []
    def flatten_rec(elem):
        return result.append(elem) if type(elem) is not list and type(elem) is not tuple else [flatten_rec(e) for e in elem]
    [flatten_rec(x) for x in origin]
    return result













#testy:
#z1a
print(acronim(["Zakład", "Ubezpieczeń", "Społecznych"]))

#z1b
print(median([1,1,19,2,3,4,4,5,1]))
print(median([1,1,19,3,4,4,5,1]))

# z1c
print(sqrt_newt(3, 0.1))

#z1d
print(make_alpha_dict("on i ona"))

#z1e
print(flatten([1, [2, 3], [[4, 5], 6]]))






