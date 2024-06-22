def uf(uf):
    UFs = ['AC', 'AL', 'AP', 'AM', 
           'BA', 
           'CE', 
           'DF', 
           'ES', 
           'GO', 
           'MA', 'MT', 'MS', 'MG', 
           'PA', 'PB', 'PR', 'PE', 'PI', 
           'RJ', 'RN', 'RS', 'RO', 'RR', 
           'SC', 'SP', 'SE', 
           'TO'
        ]
    if uf.upper() in UFs:
        return True
    else:
        return False