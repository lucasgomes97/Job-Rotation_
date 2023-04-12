#Abaixo está a resposta da segunda questão

"""Classe onde foi instanciado  à sequência de Fibonacci'"""
class Sequencia_Fibonacci:
    def Fibonacci(numero):
        numero_inicial = 0 
        numero_adicional = 1 

        if numero == numero_inicial or numero == numero_adicional:
            return f'{numero} pertence à sequência de Fibonacci'
        
        while numero_inicial + numero_adicional <= numero:
            proximo_numero = numero_inicial + numero_adicional
        
        if proximo_numero == numero:
            return f'{numero} pertence à sequência de Fibonacci'
        
        numero_inicial = numero_adicional
        numero_adicional = proximo_numero

        return f'{numero} não pertence à sequência de Fibonacci'
    
    def main():
        numero_informado = int(input("Informe um némero: "))
        resultado = Sequencia_Fibonacci.Fibonacci(numero_informado)
        print(resultado)

if __name__ == '__main__':
    Sequencia_Fibonacci.main()
    