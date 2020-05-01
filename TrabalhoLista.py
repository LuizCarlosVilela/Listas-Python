"""
Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:

O modelo do carro mais econômico;

Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 4,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.


Relatório Final

 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43

 2 - gol             -   10.0 -  100.0 litros - R$ 225.00

 3 - uno             -   12.5 -   80.0 litros - R$ 180.00

 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00

 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17

O menor consumo é do peugeout.


"""

#Obs:Eu Luiz, desenvolvi este programa, qualquer cópia não é culpa minha.
ListaDeCarros=[]
ListaDeConsumo=[]

#Pega os dados dos carros e o consumo de cada um, depois aplica todos os dados nas determinadas listas
for i in range(0,5):
    print(10*"-=-")
#Esse print já vai organizando dizendo que I+1 vai ser o número de determinado carro, e também o seu consumo
    print("Veículo ",i+1)
    Carro=input("Nome:")
    Consumo=float(input("Km por litro:"))
    ListaDeCarros.append(Carro)
    ListaDeConsumo.append(Consumo)
        

print(10*"-=-")
print("Relatório Final")
#o for i in range vai ir organizando os carros correspondendo aos determinados números que é i+1
for i in range (0,5):
#e este print  vai fazer os cálculos, para dizer a quantidade de litros e a quantidade de dinheiro que vai precisar para andar 1000Km
    print(i+1," - ",ListaDeCarros[i]," - ",ListaDeConsumo[i]," km/L - ",1000/ListaDeConsumo[i],"Litros Por 1000Km - ","R$:",(1000/ListaDeConsumo[i])*4.25)
    
    

# Este print vai presuquisar o maior numero que tem na lista de consumo, e o index vai pesquisar a sua localização para dizer a lista de carros, para achar o modelo do carro
print ("O menor consumo é o do carro de modelo: ", ListaDeCarros[ListaDeConsumo.index(max(ListaDeConsumo))] )
print(10*"-=-")
