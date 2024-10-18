#Toms Liniņš 18/10/2024
correct_password = ("python123") #pareiza parole
parole = input("Ievadi paroli: ") # jauta tev ievadit paroli


while parole != correct_password: # ja parole nav pareiza jauta velreiz
    print ("Piekļuve liegta")
    parole = input("Ievadi paroli: ")

if parole == correct_password: #ja parole ir pareiza tad beidzas
    print ("Piekļuve atļauta!")
    

 
    
