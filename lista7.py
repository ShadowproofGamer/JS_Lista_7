# z1
def acronim(lista):
    def acronim_rec(remaining, result):
        try:
            return acronim_rec(remaining[1::], result+remaining[0][0])
        except:
            return result
    return acronim_rec(lista, "")

# z2
def median(lista):
    def median_rec(remaining, result):
        try:
            return median_rec(remaining[1:-1:], result=float(remaining[0]+remaining[-1])/2)
        except:
            return result
    return median_rec(lista, 0)


# z3
def sqrt_newt(num:float, epsilon):
    def sqrt_newt_rec(num1, num2):
        return num1 if abs(num1*num1 - num)<epsilon else sqrt_newt_rec((num1+num2)/2, num/((num1+num2)/2))
    return sqrt_newt_rec(float(num/2), float(num)/float(num/2))



#testy:
#z1a
print(acronim(["Zakład", "Ubezpieczeń", "Społecznych"]))

#z1b
print(median([1,1,19,2,3,4,4,5,1]))
print(median([1,1,19,3,4,4,5,1]))

# z1c
print(sqrt_newt(3, 0.1))