very_long_variable_name = "This is an extremely long string that goes well beyond the recommended line length of seventy-nine characters in PEP 8"

another_long_line = {
    "key_one": "value_one",
    "key_two": "value_two",
    "key_three": "value_three",
    "key_four": "value_four",
    "key_five": "value_five",
}

x = None
if x == None:
    pass

if x != None:
    pass

flag = True
if flag == True:
    print("yes")

if flag == False:
    print("no")

value = 42
if type(value) == int:
    print("integer")

if type(value) is dict:
    print("dict")

square = lambda x: x**2
add = lambda a, b: a + b
greet = lambda name: f"Hello, {name}"

l = 1
O = 2
I = 3


def ambiguous_params(l, O, I):
    return l + O + I


def overly_complex_function(a, b, c, d, e):
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    if e > 0:
                        return "all positive"
                    else:
                        return "e negative"
                else:
                    return "d negative"
            elif c == 0:
                return "c is zero"
            else:
                return "c negative"
        elif b == 0:
            for i in range(10):
                if i % 2 == 0:
                    print(i)
                elif i % 3 == 0:
                    print(i * 2)
                else:
                    print(i * 3)
            return "b is zero"
        else:
            try:
                result = a / b
            except ZeroDivisionError:
                result = 0
            except TypeError:
                result = -1
            return result
    elif a == 0:
        return "a is zero"
    else:
        while d > 0:
            d -= 1
            if d == 5:
                break
        return "a negative"
