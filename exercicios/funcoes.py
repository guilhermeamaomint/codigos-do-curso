def abertura(numero):
    if numero == 1:
        return 1
    return numero * abertura(numero - 1)
