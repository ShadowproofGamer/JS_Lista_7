

# z1 a
def acronim(lista):
    def acronim_rec(remaining, result):
        return result if len(remaining)==0 else acronim_rec(remaining[1::], result+remaining[0][0])
    return acronim_rec(lista, "")

def acronim_v2(lista):
    def acronim_rec(remaining, result):
        try:
            return acronim_rec(remaining[1::], result+remaining[0][0])
        except:
            return result
    return acronim_rec(lista, "")

# z1 b
def median(lista):
    def median_rec(remaining, result):
        return result if len(remaining)==0 else median_rec(remaining[1:-1:], result=float(remaining[0]+remaining[-1])/2)
    return median_rec(lista, 0)

def median_v2(lista):
    def median_rec(remaining, result):
        try:
            return median_rec(remaining[1:-1:], result=float(remaining[0]+remaining[-1])/2)
        except:
            return result
    return median_rec(lista, 0)


# z1 c
def sqrt_newt(num:float, epsilon):
    def sqrt_newt_rec(num1, num2):
        return num1 if abs(num1*num1 - num)<epsilon else sqrt_newt_rec((num1+num2)/2, num/((num1+num2)/2))
    return sqrt_newt_rec(float(num/2), float(num)/float(num/2))

# z1 d
def make_alpha_dict(text:str):
    def make_alpha_dict_rec(remaining, result:dict):
        {result[x].append(remaining[0]) for x in result if remaining[0].__contains__(x)}
        return result if len(remaining)==1 else make_alpha_dict_rec(remaining[1::], result)
    return make_alpha_dict_rec(text.split(), dict([(x,[]) for x in text if x!=' ']))

# z1 e
def flatten(origin):
    result = []
    def flatten_rec(elem):
        return result.append(elem) if type(elem) is not list and type(elem) is not tuple else [flatten_rec(e) for e in elem]
    [flatten_rec(x) for x in origin]
    return result


# z2 a
def forall(pred, iterable):
    counter = 0
    for i in iterable:
        if pred(i): counter+=1
    return (counter/len(iterable))==1

# z2 b
def exists(pred, iterable):
    counter = 0
    for i in iterable:
        if pred(i): counter+=1
    return counter>0

# z2 c
def atleast(n, pred, iterable):
    counter = 0
    for i in iterable:
        if pred(i): counter+=1
    return counter>=n

# z2 d
def atmost(n, pred, iterable):
    counter = 0
    for i in iterable:
        if pred(i): counter+=1
    return counter<=n


# z3
import string, random
class PasswordGenerator():
    def __init__(self, length:int, count:int, charset:str =(string.ascii_letters+string.digits)):
        self.length = length
        self.count = count
        self.charset = charset
        
    def __iter__(self):
        return self
    def __next__(self):
        if self.count<=0:
            raise StopIteration()
        else:
            result=""
            i=0
            while i<=self.length:
                result += self.charset[random.randrange(0, len(self.charset))]
                i+=1
            self.count-=1
            return result



# z4
def make_generator(f):
    def generator():
        i=1
        while True:
            yield f(i)
            i+=1
    return generator

def fibonacci(n):
    a, b = 0, 1
    i = 1
    while i<=n:
        a, b = b, a+b
        i+=1
    return b

z4_geometric_progression = lambda n: n*n



# z5 - TODO
from functools import cache
def make_generator_mem(f):
    @cache
    def memoized_f(n):
        return f(n)
    def generator():
        i=1
        while True:
            yield memoized_f(i)
            i+=1
    return generator





# z6
import logging, time
def log(func, level="ERROR"):
    logger = logging.getLogger()
    level_dict = {
        "INFO": logging.INFO,
        "DEBUG": logging.DEBUG,
        "ERROR": logging.ERROR,
        "WARNING": logging.WARNING,
        "CRITICAL": logging.CRITICAL
    }
    if level_dict.get(level) :
        logger.setLevel(level_dict[level])
    #default level in case of wrong input
    else:
        logger.setLevel(logging.DEBUG)

    def wrapper(*args, **kwargs):
        name = func.__qualname__
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        try:
            issubclass(func, object)
            logger.log(level=logger.getEffectiveLevel(), msg="Class {} initialized".format(name))
        except:
            logger.log(level=logger.getEffectiveLevel(), msg="start: {}, stop: {}, name: {}, returned: {}, args: {}, kwargs: {}".format(start, end, name, result, [ *args ], {**kwargs}))
        return result
    return wrapper






#testy:
#z1a
print("\nakronim:")
print(acronim(["Zakład", "Ubezpieczeń", "Społecznych"]))

#z1b
print("\nmediana:")
print(median([1,1,19,2,3,4,4,5,1]))
print(median([1,1,19,3,4,4,5,1]))

#z1c
print("\npierwiastek metodą newtona:")
print(sqrt_newt(3, 0.1))

#z1d
print("\nsłownik:")
print(make_alpha_dict("on i ona"))

#z1e
print("\nspłaszczenie:")
print(flatten([1, [2, 3], [[4, 5], 6]]))


#z2
dodatnia = lambda n: n>0

lista_dodatnich = [1, 2, 3, 4, 5]
lista_nieujemnych = [0, 1, 2, 3, 4, 5]
lista_niepelna = [-1, 0, 1, 2]

#z2 a
print("\nforall (dodatnia):")
print(lista_dodatnich, forall(dodatnia, lista_dodatnich))
print(lista_nieujemnych, forall(dodatnia, lista_nieujemnych))

#z2 b
zero = lambda n: n==0
print("\nexists (zero):")
print(lista_dodatnich, exists(zero, lista_dodatnich))
print(lista_nieujemnych, exists(zero, lista_nieujemnych))


#z2 c
print("\natleast (dodatnia):")
print(lista_niepelna, 3, atleast(3, dodatnia, lista_niepelna))
print(lista_niepelna, 2, atleast(2, dodatnia, lista_niepelna))


#z2 d
print("\natmost (dodatnia):")
print(lista_niepelna, 2, atmost(2, dodatnia, lista_niepelna))
print(lista_niepelna, 1, atmost(1, dodatnia, lista_niepelna))



#z3
print("\niterator (metoda next):")
passg = PasswordGenerator(8, 3)
try:
    print(next(passg))
    print(next(passg))
    print(next(passg))
    print(next(passg))
except StopIteration:
    print("koniec iteratora")

print("\niterator (metoda for):")
passg2 = PasswordGenerator(8, 3)
try:
    for i in passg2:
        print(i)
except StopIteration:
    print("koniec iteratora")



#z4 a
print("\niterator (funkcja ciągu fibonacciego):")
gen1 = make_generator(fibonacci)()
z4_i = 1
for w in gen1:
    print(w)
    if z4_i>=10:
        break
    else:
        z4_i+=1


#z4 b
print("\niterator (lambda ciągu geometrycznego):")
gen2 = make_generator(z4_geometric_progression)()
z4_i = 1
for w in gen2:
    print(w)
    if z4_i>=10:
        break
    else:
        z4_i+=1



#z5
print("\niterator (funkcja ciągu fibonacciego):")
gen3 = make_generator_mem(fibonacci)()
z4_i = 1
for w in gen1:
    print(w)
    if z4_i>=10:
        break
    else:
        z4_i+=1



#z6
print("\nlog decorator (function): ")
wrapped1 = log(flatten, "ERROR")
print(wrapped1([1, [2, 3], [[4, 5], 6]]))

print("\nlog decorator (class):")
wrapped2 = log(PasswordGenerator, "ERROR")
print(next(wrapped2(8, 3)))






##dodatkowe testy:
##z6 @log
#print("\nlog decorator (function, @header): ")
#@log
#def forall2(pred, iterable):
#    counter = 0
#    for i in iterable:
#        if pred(i): counter+=1
#    return (counter/len(iterable))==1
#
#forall2(dodatnia, lista_dodatnich)
#
##z5 @cache using time_in
#@cache
#def fibonacci_v2(n):
#    a, b = 0, 1
#    i = 1
#    while i<=n:
#        a, b = b, a+b
#        i+=1
#    return b
#
#def time_in(func):
#    def wrapper(*args, **kwargs):
#        name = func.__qualname__
#        start = time.perf_counter()
#        result = func(*args, **kwargs)
#        end = time.perf_counter()
#        print("{}: elapsed time: {}".format(name, (end-start)))
#        return result
#    return wrapper
#
#
#print("\nlog decorator (function + no @cache): ")
#fib1 = time_in(fibonacci)
#fib1(10000)
#fib1(10000)
#
#print("\nlog decorator (function + @cache): ")
#fib2 = time_in(fibonacci_v2)
#fib2(10000)
#fib2(10000)
#
#print("\ntime_in decorator (generator + @cache): ")
#gen4 = make_generator_mem(fibonacci)()
#@time_in
#def iterating_mem_gen(n, gener):
#    temp = 1
#    
#    for x in iter(gener):
#        x
#        if(temp>=n):break
#        temp+=1
#
#iterating_mem_gen(10000, gen4)
#gen5 = make_generator_mem(fibonacci)()
#iterating_mem_gen(10000, gen5)