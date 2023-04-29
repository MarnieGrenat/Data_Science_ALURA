import pandas as pd
def achar_maior_numero(lista:list):
    dados = pd.Series(lista)
    dados= dados.sort_values()
    value=dados.iloc[-2:]
    return value
                 
print(achar_maior_numero([7,2,8,6,3,345,2,6,7,34,75,7603,9]))

def achar_maior_numero2(lista:list):
    valor_final= lista[1]
    for item in lista:
        if valor_final < item:
            valor_final=item
    return valor_final


#print(achar_maior_numero2([7,2,8,6,3,345,2,6,7,34,7603,8,9]))
