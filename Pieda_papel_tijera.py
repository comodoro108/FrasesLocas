#toca importar alguna libreria de aleatoriedad
import random


#definimos escogencias entre usuario y computadora
def pipati():

    human = input("Escoge una opcion, piedra, papel o tijera: \n").lower()
    computer = random.choice(['piedra', 'papel', 'tijera'])

#comparativa entre user y pc

    if human == computer:
        return 'Es un Empate!'
    
    if win_human(human, computer):
        return 'YOU WIN'

    return 'YOU ARE LOSER, GAME OVER'

def win_human(jugador, pc):

#piedra>tijera
#tijera>papel
#papel>piedra

#true si gano jugador

#false si pierde  
    if ((jugador == 'piedra' and pc == 'tijera')
        or (jugador == 'tijera' and pc == 'papel') 
        or (jugador == 'papel' and pc == 'piedra')):
        return True
    else:
        return False

#impresion de resultado, OJO, FUNCION PRINCIPAL
print(pipati())

