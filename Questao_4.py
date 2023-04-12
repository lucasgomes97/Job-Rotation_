
# Abaixo segue a resposta da Quarta questão 
"""Para resolvermos está questão utilizaremos a linguagem Python.
   Sabe-se que velocidade é igual a distancia/tempo  e que a distancia entre as cidades é de 100km 
   e ambos os veículos estão se aproximando um do outro a partir de cidades opostas, 
   ou seja, estão a uma distância de 50 km cada um de sua respectiva cidade.então temos:"""
#Variáveis Definidas
Velocidade_carro = 110
Velocidade_caminhao = 80 
distancia_carro_caminhao = 50
pedagio_caminhao = 5


Tempo_carro = distancia_carro_caminhao / Velocidade_carro *100
Tempo_caminhao = distancia_carro_caminhao + 2*(pedagio_caminhao) / Velocidade_caminhao

carro = round(Tempo_carro,)
caminhao= round(Tempo_caminhao)

print("Tempo do carro: {} minutos".format(carro))
print("Tempo do caminhão: {} minutos".format(caminhao))

"""Portanto, partindo do principio que iniciaram a viagem ao mesmo tempo, 
   como o carro por ter  velocidade eles estarão mais perto de Franca do que Ribeirão Preto,
   no momento que se cruzarem, mas neste instante ambos estarão a mesma distância de Ribeirão Preto."""




