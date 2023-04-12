

"""Função para inverter uma string"""
def inverter_string(string):
    lista_caracteres = list(string)
    tamanho = len(lista_caracteres)
    for i in range(tamanho // 2):
        lista_caracteres[i], lista_caracteres[tamanho - i - 1] = lista_caracteres[tamanho - i - 1], lista_caracteres[i]
    string_invertida = ''.join(lista_caracteres)
    return string_invertida

"""Teste da função"""
string_original = "Obrigado pela oportunidade de realizar este teste."
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)