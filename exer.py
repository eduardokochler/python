nome = input("Insira seu nome: ")
sexo = input("Insira seu sexo(M/F): ")
idade = int(input("Insira sua idade: "))
altura = float(input("Insira sua altura: "))
peso = float(input("Insira seu peso: "))

import json

PIF = (62.1 * altura) - 44.7
PIM = (72.7 * altura) - 58

pesoIdealAMaisM = (PIM * 0.05) + PIM
pesoIdealAMenosM = (PIM * 0.05) - PIM

pesoIdealAMaisF = (PIF * 0.05) + PIF
pesoIdealAMenosF = (PIF * 0.05) - PIF

emagrecerM = peso - pesoIdealAMaisM
engordarM = pesoIdealAMenosM - peso
emagrecerF = peso - pesoIdealAMaisF
engordarF = pesoIdealAMenosF - peso
 
vintePcIF = PIF * 0.2
vintePcIM = PIM * 0.2

porcentoAmaisF = (peso - PIF) / PIF  * 100
porcentoAmaisM = (peso - PIM) / PIM * 100

pessoa = {
    'Nome:': nome,
    'Peso atual:': peso,
    'Peso ideal:': round(PIM, 1) if sexo == 'M' else round(PIF, 1)
}


if sexo == "M":
    
    if peso > pesoIdealAMaisM and idade < 65:
      print(json.dumps(pessoa,indent=4))
    
      print(nome, "você deve emagrecer", (round(emagrecerM, 1)), "Kg.")
    
    elif peso < pesoIdealAMenosM :
        print(json.dumps(pessoa,indent=4))
       
        print(nome, "você pode engordar", (round(engordarM, 1)), "Kg.")

    elif peso > pesoIdealAMenosM and peso < pesoIdealAMaisM:
        print(json.dumps(pessoa,indent=4))
       
        print(nome, "você está no seu peso ideal.")
    
    elif porcentoAmaisM >= vintePcIM and idade >= 65:
        print(json.dumps(pessoa,indent=4))
       
        print(nome, "você deve emagrecer", (round(emagrecerM, 1)), "Kg.")
        print("Cuidado! Você deve procurar um médico,","pois está",(round(porcentoAmaisM,1)) ,"%", " acima do seu peso ideal.")  

if sexo == "F":
    
    if peso > pesoIdealAMaisF and idade < 65:
      print(json.dumps(pessoa,indent=4))

      print(nome, "você deve emagrecer", (round(emagrecerF, 1)), "Kg.")
         
    elif peso < pesoIdealAMenosF :
        print(json.dumps(pessoa,indent=4))
        
        print(nome, "você pode engordar", (round(engordarF, 1)), "Kg.")

    elif peso > pesoIdealAMenosF and peso < pesoIdealAMaisF :
        print(json.dumps(pessoa,indent=4))
       
        print(nome,"você está no seu peso ideal.")
    
    elif porcentoAmaisF >= vintePcIF and idade >= 65:
        print(json.dumps(pessoa,indent=4))
       
        print(nome, "você deve emagrecer", (round(emagrecerF, 1)), "Kg.")
        print("Cuidado! Você deve procurar um médico,","pois está",(round(porcentoAmaisF,1)) ,"%", " acima do seu peso ideal.")  
       
        

   

      

 
 