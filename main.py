import pygame, random, assets
pygame.init() #inicia a biblioteca "pygame"
tamanho = (1080, 720) #tamanho da tela
clock = pygame.time.Clock() #define o fps 
tela = pygame.display.set_mode(tamanho) #cria o display da tela
pygame.display.set_caption('IronMan GG') #cria o título da tela

fonte = pygame.font.SysFont('comicsans', 14)
pygame.mixer.music.load('assets/ironsound.mp3')
pygame.mixer.music.play(-1)

missileSound = pygame.mixer.Sound('assets/missile.wav')
pygame.mixer.Sound.play(missileSound)


branco = (255, 255, 255)
preto = (0, 0, 0)

ironman = pygame.image.load('assets/iron.png')
picture = pygame.image.load('assets/fundo.png')
bg = pygame.transform.scale(picture, (1080, 720))
missil = pygame.image.load('assets/missile.png')

posXPers = 400
posYPers = 300
movimentoXPers = 0
movimentoYPers = 0

posXmissile = 400
posYmissile = -240
velmissile = 1


while True: #mantém a tela aberta até que a tela seja fechada
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            movimentoXPers = 20
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            movimentoXPers = -20
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
            movimentoXPers = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            movimentoXPers = 0

        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            movimentoYPers = -20
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            movimentoYPers = 20
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
            movimentoYPers = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            movimentoYPers = 0
    
    posXPers = posXPers + movimentoXPers
    if posXPers < 0:
        posXPers = 10
    elif posXPers > 830:
        posXPers = 820

    posYPers = posYPers + movimentoYPers
    if posYPers < 0:
        posYPers = 10
    elif posYPers > 593:
        posYPers = 583

    tela.fill(branco) #diz qual é a cor de background
    tela.blit(bg, (0, 0))
    tela.blit(ironman, (posXPers, posYPers))
    
    posYmissile = posYmissile + velmissile
    if posYmissile > 720:
        posYmissile = -240
        velmissile = velmissile + 1
        posXmissile = random.randint(0, 1080)
        pygame.mixer.Sound.play(missileSound)

    tela.blit(missil, (posXmissile, posYmissile))

    #pygame.draw.circle(tela, preto, (posXPers, posYPers), 40, 0)
    #texto = fonte.render(str(posXPers) + '-' + str(posYPers), True, branco)
    #tela.blit(texto, (posXPers-30, posYPers-10))

    pygame.display.update() #diz pra atualizar a tela
    clock.tick(120) #diz que a tela vai ter 60 fps

pygame.quit()