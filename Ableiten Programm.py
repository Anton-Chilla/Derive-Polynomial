def parse_multiplication(term):
    return term.split('*')

def differentiate_multiple_factors(term):
    factors = parse_multiplication(term)
    n = len(factors)

    if n < 2:
        return differentiate(term)
    
    differentiated_terms = []

    for i in range(n):
        differentiated_factors = factors[:]
        differentiated_factors[i] = differentiate(factors[i])
        differentiated_terms.append('*'.join(differentiated_factors))

    return f"({' + '.join(differentiated_terms)})"

def differentiate(term):
    if '*' in term:
        return differentiate_multiple_factors(term)
    
    if 'x' not in term:
        return "0"
    
    if term == "x":
        return "1"
    
    parts = term.split('x')
    coefficient = int(parts[0]) if parts[0] not in ("", "+") else 1
    power = int(parts[1][1:]) if len(parts) > 1 and "^" in parts[1] else 1
    
    new_coefficient = coefficient * power
    new_power = power - 1

    if new_power == 0:
        return str(new_coefficient)
    elif new_power == 1:
        return f"{new_coefficient}x"
    else:
        return f"{new_coefficient}x^{new_power}"

def derive_polynomial(expression):
    terms = expression.replace(" ", "").split("+")
    differentiated_terms = []

    for term in terms:
        if '-' in term[1:]:
            subterms = term.split('-')
            differentiated_terms.append(differentiate(subterms[0]))
            for subterm in subterms[1:]:
                differentiated_terms.append("-" + differentiate(subterm))
        else:
            differentiated_terms.append(differentiate(term))
    return " + ".join(filter(lambda t: t != "0", differentiated_terms))

expression = "25x^2*x^225"
result = derive_polynomial(expression)
print(f"The derivative of '{expression}' is: {result}")
