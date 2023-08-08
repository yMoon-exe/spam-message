import time
import pyautogui
import keyboard

# Defina um intervalo de pausa entre ações do pyautogui (em segundos)
pyautogui.PAUSE = 0.5  # Pausa de 0.5 segundos

def enviar_template(numero):
    template = f"Faz o template {numero}"
    return template

def main():
    print('Simbora corno, faz os templates')

    # Aguarde para abrir onde quer as mensagems
    time.sleep(2)

    for numero in range(1, 241):
        if keyboard.is_pressed('ctrl'):
            print("Pressionou Ctrl, parando...")
            break
        
        template = enviar_template(numero)
        print(template)
        
        # Digite as mensagens
        pyautogui.write(template)
        pyautogui.press('enter')

    input("Pressione Enter para fechar o Bloco de Notas...")

if __name__ == "__main__":
    main()
