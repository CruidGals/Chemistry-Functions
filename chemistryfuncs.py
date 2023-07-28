import math

def round_half_up(n, decimals=0):
    multiplier = 10**decimals
    return math.floor(n * multiplier + 0.5) / multiplier

#Returns integer, and how many spaces it takes up
#String must start with a number
def split_elm_num_pair(pair: str):
    element = ''
    occurences = ''

    for char in pair:
        if char.isnumeric():
            occurences = occurences + char
        else:
            element = element + char

    return element, (int(occurences) if occurences != '' else 1)

def formula_decipherer(formula: str) -> dict:
    element_dict = {}
    skip = 0
    prev_elm = ''
    formula = formula + 'A' #Placeholder, so the function doesnt end early

    for idx, char in enumerate(formula):
        if skip > 0:
            skip -= 1
            prev_elm = prev_elm + char
            continue

        if char==')':
            scale = 1
            temp_dict = formula_decipherer(prev_elm) #Recursion
            
            #Check if there is a scale
            if (idx != len(formula)-1):
                num_str = ''
                for let in formula[idx+1]:
                    if let.isnumeric():
                        num_str = num_str + let
                        skip += 1
                    else:
                        break
                scale = int(num_str) if num_str != '' else 1

            element_dict.update((element, occurences * scale + element_dict.get(element, 0)) for element, occurences in temp_dict.items())
            prev_elm = ''
        elif char=='(':
            skip = formula.rfind(')') - idx - 1
            
            element, occurences = split_elm_num_pair(prev_elm)
            if element != '':
                element_dict.update({element: occurences + element_dict.get(element, 0)})
            prev_elm = ''
        elif char.isupper():
            element, occurences = split_elm_num_pair(prev_elm)
            if element != '':
                element_dict.update({element: occurences + element_dict.get(element, 0)})
            prev_elm = char
        else:
            prev_elm = prev_elm + char

    print(element_dict)
    return element_dict  

def molar_mass_calc(formula: str, mass_dict: dict) -> float:
    element_dict = formula_decipherer(formula)
    total_mass = 0.0

    for element, occurences in element_dict.items():
        total_mass += mass_dict[element] * float(occurences)

    return round_half_up(total_mass, 2)
