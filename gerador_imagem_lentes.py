#========================================================#
##### FUNÇÃO GERADORA DE IMAGEM PARA LENTES DELGADAS #####
#========================================================#
######### AUTOR: ANTÔNIO HENRIQUE CARLAN JÚNIOR ##########
#========================================================#
######### CANAL DO YOUTUBE: FÍSICA - O PROMETEU ##########
#========================================================#
############ FAÇA BOM USO, PROFESSOR OU ALUNO ############
#========================================================#
from math import *
import numpy as np
import matplotlib.pyplot as plt
def ger_lente():
    
    
    y = [0,0,0]
    print("Para gerar uma imagem de lentes dealgadas, escolha o valor para dois dos três pedidos a seguir")
    print("e exatamente um dos valores para ser declarado como indefinido. No máximo um valor como infinito é permitido" + '\n')
    y[0] = input('\n'+"Insira a posição do objeto (pode ser ind para indeterminado e inf para infinito)")
    y[1] = input('\n'+"Insira a posição da imagem (pode ser ind para indeterminado e inf para infinito, caso a lente seja convergente) ")
    y[2] = input('\n'+"Insira a posição do foco (pode ser ind para indeterminado e inf para infinito)")
    
    
    def lente(entrada):
        
        p_objeto =0
        p_imagem = 0
        foco = 0
        aumento_linear = 0
    
    
        if(entrada[0] == "ind"):       # Caso o valor de p não seja dado
            if (entrada[1] == "inf"):
            
                p_objeto = entrada[2]
                foco = entrada[2]
                p_imagem = "inf"
            
            if (entrada[2] == "inf"):
            
                foco = "inf"
                p_imagem = -abs(float(entrada[1]))
                p_objeto = - p_imagem
            
            if(entrada[1] == entrada[2]):
            
                p_imagem = float(entrada[1])
                foco = float(entrada[2])
                p_objeto = "inf"
            
            if(entrada[1] != entrada[2] and entrada[1] != "inf" and entrada[2] != "inf"):
        
                p_imagem = float(entrada[1])
                foco = float(entrada[2])
                p_objeto = (p_imagem*foco)/(p_imagem - foco)
        
        if(entrada[1] == 'ind'):       # Caso o valor de p' não seja dado
        
            if (entrada[0] == "inf"):
            
                p_imagem = entrada[2]
                foco = entrada[2]
                p_objeto = "inf"
            
            if (entrada[2] == "inf"):
            
                foco = "inf"
                p_imagem = float(entrada[0])
                p_objeto = - float(p_imagem)
            
            if(entrada[0] == entrada[2]):
            
                p_objeto = float(entrada[0])
                foco = float(entrada[2])
                p_imagem = "inf"
            
            if(entrada[0] != entrada[2] and entrada[0] != "inf" and entrada[2] != "inf"):
            
                p_objeto = float(entrada[0])
                foco = float(entrada[2])
                p_imagem = (p_objeto*foco)/(p_objeto - foco)
            
        if(entrada[2] == 'ind'):       # Caso o valor de f não seja dado
        
            if (entrada[0] == "inf"):
            
                p_imagem = entrada[1]
                foco = entrada[1]
                p_objeto = "inf"
            
            if (entrada[1] == "inf"):
            
                foco = entrada[0]
                p_objeto = entrada[0]
                p_imagem = "inf"
            
            if(entrada[0] == -float(entrada[1])):
            
                p_objeto = float(entrada[1])
                foco = float(entrada[2])
                p_imagem = "inf"
            
            if(entrada[0] != -float(entrada[1]) and entrada[0] != "inf" and entrada[1] != "inf"):
            
                p_objeto = float(entrada[0])
                p_imagem = float(entrada[1])
                foco = (p_objeto*p_imagem)/(p_objeto + p_imagem)
        
        if (p_objeto != "inf" and p_imagem != "inf" and foco != "inf"):
        
            aumento_linear = -(float(p_imagem)/float(p_objeto))    # Calcula o aumento linear para a formação da imagem
        
        else:
            aumento_linear = 1
    
        if(float(p_imagem)>0):
            if(float(foco)<0):
                print("")
                print("ERRO, Lente divergente possui imagem com posição negativa")
                print("")
                p_objeto = "erro"
                p_imagem = 'erro'
                foco = 'erro'
                aumento_linear = 'erro'
            
        if(float(foco)<0):
            if(p_imagem == inf):
                print("")
                print("ERRO, lentes divergentes não geram imagem no infinito")
                print("")
                p_objeto = "erro"
                p_imagem = 'erro'
                foco = 'erro'
                aumento_linear = 'erro'
    
    
        return p_objeto, p_imagem, foco, aumento_linear #retorna um array da forma [ p, p', f, i/o]
        
    a,b,f,aum = lente(y)
    ajuste_x = 0
    h_len = 0

    
    
    if( a!= 'inf' and float(a)<0):  # o objeto sempre está em posição positiva, por isso pode ser feita a inversão
        a = -float(a)
        if(b != 'inf'):
            b = -float(b)
        
#===============================#
## Criando um ajuste de acordo ##
####### com as entradas #########
#===============================#
    if(a !='inf' and b != "inf" and f!="inf"):
                       
        ajuste_x = max(abs(a),abs(b),abs(f))*1.2
        h_len = max(abs(aum),1)*1.4
        a = float(a)
        b = float(b)
        f = float(f)
        
    else:
        h_len = 1.5
        
    if(f =="inf"):
        ajuste_x = max(abs(float(a)),abs(float(b)))*1.2
        a = float(a)
        b = float(b)
        
    if(a =="inf"):
        ajuste_x = max(abs(float(b)),abs(float(f)))*1.2
        b = float(b)
        f = float(f)
        
    if(b =="inf"):
        ajuste_x = max(abs(float(a)),abs(float(f)))*1.2
        a = float(a)
        f = float(f)
    
    
    print('\n' + 'INFORMAÇÕES SOBRE A FORMAÇÃO DA IMAGEM' +'\n')
    print('\n' + 'POSIÇÃO DO OBJETO = '+ str(a) +'\n')
    print('\n' + 'POSIÇÃO DA IMAGEM = '+str(b) +'\n')
    print('\n' + 'DISTÂNCIA FOCAL = ' +str(f)+'\n')
    
    if (f == 'inf'):
        print('\n' + 'DIOPTRO PLANO, O OBJETO E A IMAGEM COINCIDEM' +'\n')
        
    else:
        if (f>0):
            print('\n' + 'LENTE CONVERGENTE' +'\n')
        else:
            print('\n' + 'LENTE DIVERGENTE' +'\n')
            
        if (b=='inf'):
            print('\n' + 'IMAGEM IMPRÓPRIA, SE FORMA NO INFINITO' +'\n')
        
        else:
            if(b>0):
            
                if(aum>0):
                    print('\n' + 'IMAGEM REAL E DIREITA' +'\n')
                
                else:
                    print('\n' + 'IMAGEM REAL E INVERTIDA' +'\n')
            
            else:
                if(aum>0):
                    print('\n' + 'IMAGEM VIRTUAL E DIREITA' +'\n')
                
                else:
                    print('\n' + 'IMAGEM VIRTUAL E INVERTIDA' +'\n')
                
                
        print('\n' + 'AUMENTO LINEAR DA IMAGEM = ' + str(aum)+'\n')
    
    plt.figure(figsize = (15,10))  
    
    
    
    
#=======================================#
######### Plot do eixo horizontal########
#=======================================#

    plt.plot([-ajuste_x,ajuste_x], [0,0], color = "k")
    
#===============================#
######### Plot dos focos ########
#===============================#
    if(f != "inf"):
        plt.scatter([f,-f],[0,0],color = 'indigo', marker = 'o', s = 100)


#================================#
######### Plot da lente  #########
#================================#

    plt.plot([0,0], [-h_len,h_len], color = "turquoise",linewidth = 5)             #Plota uma linha vermelha para representar a lente
    
    if(f == 'inf'):
          k = 0          #não plota nada, equivale a um espelho
    
    else:
        if (f>0):  #lente convergente                                #e faz o teste de convergência/divergência da lente
            plt.scatter([0], [h_len],marker= "^", color = 'turquoise',s = 300)
            plt.scatter([0], [-h_len],marker= "v", color = 'turquoise',s = 300)
    
        else:      #lente divergente
            plt.scatter([0], [h_len],marker= "v", color = 'turquoise',s = 300)
            plt.scatter([0], [-h_len],marker= "^", color = 'turquoise',s = 300)


#===============================#
######### Plot do objeto ########
#===============================#
    if (a =="inf"):
        k = 0             # não é plotado objeto algum
        
    else:
                        # é feito o plot do objeto na posição x= -a
        plt.scatter([-a], [1],marker= "^", color = 'r',s = 100)
        plt.plot([-a,-a], [0,1],color = 'r') 
        
#===============================#
######### Plot da imagem ########
#===============================#
    if(b =="inf"):
         k = 0           # A imagem é imprópria e não se forma
            
    else:
        
        if (a == "inf"):
            k = 0            #se o a está no infinito, o tamanho da imagem vai para zero
                
        else:  
            
            if (aum>0):  # a imagem pode ter altura direita ou invertida
                plt.scatter([b],[aum], marker ='^', color = 'b', s = 100)
            else:
                plt.scatter([b],[aum], marker ='v', color = 'b', s = 100)
            plt.plot([b,b], [0,aum], color = 'b')

#========================================#
######### Plot dos raios notáveis ########
#========================================#
    if (a =="inf"):
        
        ### Raios paralelos que chegam até a lente ###
        plt.plot([-ajuste_x,0], [1,1], color = "orange")
        plt.plot([-ajuste_x,0], [0.5,0.5], color = "orange")
        plt.plot([-ajuste_x,0], [0.75,0.75], color = "orange")
        plt.plot([-ajuste_x,0], [0.25,0.25], color = "orange")
        
        ### Raios que desviam em direção ao foco e/ou prolongamentos ###
        
        if(f<0):
            if ((ajuste_x/h_len)>abs(f)):
                #raios diretos
                plt.plot([0, abs(f)*(h_len/1 - 1)], [1,h_len], color = "orange")
                plt.plot([0, abs(f)*(h_len/0.5 - 1)], [0.5,h_len], color = "orange")
                plt.plot([0,abs(f)*(h_len/0.75 - 1)], [0.75,h_len], color = "orange")
                plt.plot([0, abs(f)*(h_len/0.25 - 1)], [0.25,h_len], color = "orange") 
                #prolongamentos
                plt.plot([0, f], [1,0], color = "orange",linestyle = "dashdot")
                plt.plot([0, f], [0.5,0], color = "orange",linestyle = "dashdot")
                plt.plot([0, f], [0.75,0], color = "orange",linestyle = "dashdot")
                plt.plot([0, f], [0.25,0], color = "orange",linestyle = "dashdot") 
            else:
                #raios diretos
                plt.plot([0, ajuste_x], [1,1*(1+ ajuste_x/abs(f))], color = "orange")
                plt.plot([0, ajuste_x], [0.5,0.5*(1+ ajuste_x/abs(f))], color = "orange")
                plt.plot([0, ajuste_x], [0.75,0.75*(1+ ajuste_x/abs(f))], color = "orange")
                plt.plot([0, ajuste_x], [0.25,0.25*(1+ ajuste_x/abs(f))], color = "orange") 
                #prolongamentos
                plt.plot([0, f], [1,0], color = "orange",linestyle = "dashdot")
                plt.plot([0, f], [0.5,0], color = "orange",linestyle = "dashdot")
                plt.plot([0, f], [0.75,0], color = "orange",linestyle = "dashdot")
                plt.plot([0, f], [0.25,0], color = "orange",linestyle = "dashdot") 
            
        else:
            if ((ajuste_x/h_len)>abs(f)):
                #raios diretos
                plt.plot([0, abs(f)*(h_len/1 - 1)], [1,-h_len], color = "orange")
                plt.plot([0, abs(f)*(h_len/0.5 - 1)], [0.5,-h_len], color = "orange")
                plt.plot([0,abs(f)*(h_len/0.75 - 1)], [0.75,-h_len], color = "orange")
                plt.plot([0, abs(f)*(h_len/0.25 - 1)], [0.25,-h_len], color = "orange") 
                
            else:
                #raios diretos
                plt.plot([0, ajuste_x], [1,1*(1- ajuste_x/abs(f))], color = "orange")
                plt.plot([0, ajuste_x], [0.5,0.5*(1- ajuste_x/abs(f))], color = "orange")
                plt.plot([0, ajuste_x], [0.75,0.75*(1- ajuste_x/abs(f))], color = "orange")
                plt.plot([0, ajuste_x], [0.25,0.25*(1- ajuste_x/abs(f))], color = "orange") 
            
                
        
    else:
        #raio paralelo que vai até a lente:
        plt.plot([-a,0], [1,1], color = "orange")
        #raio que vai do objeto ao centro:
        plt.plot([-a,0], [1,0], color = "orange")
        
        #raio que passa pelo centro e segue sem desvio + prolongamento do raio na direção oposta
        plt.plot([0,h_len*a], [0,-h_len], color = "orange")
        
        #raios que chegam paralelos a lente e são desviados para os focos:
        if (f!='inf'):
            if(f>0):
                if ((ajuste_x/h_len)>abs(f)):
                #raios diretos
                    plt.plot([0,abs(f), ajuste_x], [1,0,1- ajuste_x/abs(f)], color = "orange")
                
                else:
                #raios diretos
                    plt.plot([0, ajuste_x], [1,1*(1- ajuste_x/abs(f))], color = "orange")
                
                #prolongamento:
                if(b!='inf'):
                    
                    plt.plot([0, b], [1,aum], color = "orange",linestyle = "dashdot")
                
            else:
                if ((ajuste_x/h_len)>abs(f)):
                #raios diretos
                    plt.plot([0, abs(f)*(h_len/1 - 1)], [1,h_len], color = "orange")
                #prolongamentos
                    if(b!= 'inf'):
                        plt.plot([0, f], [1,0], color = "orange",linestyle = "dashdot")
                else:
                #raios diretos
                    plt.plot([0, ajuste_x], [1,1*(1+ ajuste_x/abs(f))], color = "orange")
                #prolongamentos
                    if(b!= 'inf'):
                        plt.plot([0, f], [1,0], color = "orange",linestyle = "dashdot")
            
        else:
            plt.scatter([-a], [1],marker= "^", color = 'purple',s = 100)  #imagem gerada sobre o objeto em roxo
            plt.plot([-a,-a], [0,1],color = 'purple') 
            plt.plot([0,ajuste_x], [1,1], color = 'orange')
            
    plt.xlim(-ajuste_x-1,ajuste_x + 1)
    plt.ylim(-h_len-0.3, h_len+0.3)
    
    
    print("DESEJA SALVAR A FIGURA? ")
    saver = input('s/n ')
    if(saver == 's'):
        name = input('Escolha no nome da figura da forma: nomedafigura.png')
        plt.savefig(name)
    plt.show()   
    plt.close()
    
    return
    

