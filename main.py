import pygame, assets
pygame.init() #inicia a biblioteca "pygame"
tamanho = (800, 600) #tamanho da tela
clock = pygame.time.Clock() #define o fps 
tela = pygame.display.set_mode(tamanho) #cria o display da tela
pygame.display.set_caption('IronMan GG') #cria o título da tela
fonte = pygame.font.SysFont('comicsans', 14)
branco = (255, 255, 255)
preto = (0, 0, 0)
posXPers = 400
posYPers = 300
movimentoXPers = 0
movimentoYPers = 0
while True: #mantém a tela aberta até que a tela seja fechada
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            movimentoXPers = 5
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            movimentoXPers = -5
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
            movimentoXPers = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            movimentoXPers = 0

        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            movimentoYPers = -5
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            movimentoYPers = 5
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
            movimentoYPers = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            movimentoYPers = 0
    
    posXPers = posXPers + movimentoXPers
    if posXPers < 40:
        posXPers = 50
    elif posXPers > 760:
        posXPers = 750

    posYPers = posYPers + movimentoYPers
    if posYPers < 40:
        posYPers = 50
    elif posYPers > 560:
        posYPers = 550

    tela.fill(branco) #diz qual é a cor de background
    
    pygame.draw.circle(tela, preto, (posXPers, posYPers), 40, 0)
    texto = fonte.render(str(posXPers) + '-' + str(posYPers), True, branco)
    tela.blit(texto, (posXPers-30, posYPers-10))

    pygame.display.update() #diz pra atualizar a tela
    clock.tick() #diz que a tela vai ter 60 fps

pygame.quit()