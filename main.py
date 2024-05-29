import pygame
pygame.init() #inicia a biblioteca "pygame"
tamanho = (800, 600) #tamanho da tela
clock = pygame.time.Clock() #define o fps 
tela = pygame.display.set_mode(tamanho) #cria o display da tela
pygame.display.set_caption('IronMan GG') #cria o título da tela
branco = (255, 255, 255)
while True: #mantém a tela aberta até que a tela seja fechada
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()



    tela.fill(branco) #diz qual é a cor de background
    pygame.display.update() #diz pra atualizar a tela
    clock.tick(60) #diz que a tela vai ter 60 fps

pygame.quit()