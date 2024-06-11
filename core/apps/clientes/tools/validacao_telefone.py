def telefone(numero):
    if len(numero) != 11:
        return False

    ddd = numero[:2]
    if not ddd.isdigit():
        return False

    if numero[2] != '9':
        return False

    telefone = numero[3:]
    if not telefone.isdigit() or len(telefone) != 8:
        return False

    return True
