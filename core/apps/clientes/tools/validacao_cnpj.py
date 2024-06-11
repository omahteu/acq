def cnpj(cnpj):
    numeros = [int(digito) for digito in cnpj if digito.isdigit()]

    if len(numeros) != 14:
        return False
    
    codigo = numeros[-6:-2]
    
    if codigo != [0, 0, 0, 1] and codigo != [0, 0, 0, 2]:
        return False

    return True
