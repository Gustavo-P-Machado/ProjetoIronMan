import pygame, random, os
from tkinter import simpledialog
pygame.init() #inicia a biblioteca "pygame"
tamanho = (1080, 720) #tamanho da tela
clock = pygame.time.Clock() #define o fps 
tela = pygame.display.set_mode(tamanho) #cria o display da tela
pygame.display.set_caption('Jogo Do Amongus') #cria o título da tela

fonte = pygame.font.SysFont('comicsans', 20)
fonteMorte = pygame.font.SysFont("arial",120)
fonteStart = pygame.font.SysFont("comicsans",55)

imgicone = pygame.image.load('assets/icon.png')
icone = pygame.transform.scale(imgicone, (32, 32))
pygame.display.set_icon(icone)

imgStart = pygame.image.load("assets/fundoStart.jpg")
fundoStart = pygame.transform.scale(imgStart, (1080, 720))
imgDead = pygame.image.load("assets/fundoDead.jpg")
fundoDead = pygame.transform.scale(imgDead, (1080, 720))


morteSound = pygame.mixer.Sound("assets/deadSound.mp3")

nome = ''

branco = (255, 255, 255)
preto = (0, 0, 0)
verdeEscuro = (0, 26, 39)

def jogar(nome):

    pygame.mixer.music.stop()

    pygame.mixer.music.load('assets/jogoSound.mp3')
    pygame.mixer.music.play(-1)

    facaSound = pygame.mixer.Sound('assets/facaSound.mp3')
    pygame.mixer.Sound.play(facaSound)

    imgamogus = pygame.image.load('assets/amogus.webp')
    amogus = pygame.transform.scale(imgamogus, (100, 127))

    picture = pygame.image.load('assets/fundo.png')
    bg = pygame.transform.scale(picture, (1080, 720))

    imgfaca = pygame.image.load('assets/faca.png')
    faca = pygame.transform.scale(imgfaca, (75, 150))



    tela.set_alpha

    posXPers = 540
    posYPers = 460
    movimentoXPers = 0
    movimentoYPers = 0

    posXmissile = 400
    posYmissile = -150
    velmissile = 10

    pontos = 0
    larguraPersona = 100
    alturaPersona = 127
    larguaMissel  = 50
    alturaMissel  = 100
    dificuldade  = 0

    while True: #mantém a tela aberta até que a tela seja fechada
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
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
        elif posXPers > 980: 
            posXPers = 970

        posYPers = posYPers + movimentoYPers
        if posYPers < 0:
            posYPers = 10
        elif posYPers > 593:
            posYPers = 583

        tela.fill(branco) #diz qual é a cor de background
        tela.blit(bg, (0, 0))
        tela.blit(amogus, (posXPers, posYPers))
        
        posYmissile = posYmissile + velmissile
        if posYmissile > 720:
            posYmissile = -150
            pontos = pontos + 1
            velmissile = velmissile + 1
            posXmissile = random.randint(0, 1080)
            pygame.mixer.Sound.play(facaSound)

        tela.blit(faca, (posXmissile, posYmissile))

        pixelsPersonaX = list(range(posXPers, posXPers+larguraPersona))
        pixelsPersonaY = list(range(posYPers, posYPers+alturaPersona))
        pixelsMisselX = list(range(posXmissile, posXmissile + larguaMissel))
        pixelsMisselY = list(range(posYmissile, posYmissile + alturaMissel))
        

        if  len( list( set(pixelsMisselY).intersection(set(pixelsPersonaY))) ) > dificuldade:
            if len( list( set(pixelsMisselX).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                dead(nome, pontos)


        #pygame.draw.circle(tela, preto, (posXPers, posYPers), 40, 0)
        #texto = fonte.render(str(posXPers) + '-' + str(posYPers), True, branco)
        txtpnts = fonte.render(nome + 'Pontos: ' + str(pontos), True, branco)
        tela.blit(txtpnts, (20, 20))
        #tela.blit(texto, (posXPers-30, posYPers-10))

        pygame.display.update() #diz pra atualizar a tela
        clock.tick(60) #diz que a tela vai ter 60 fps

def dead(nome, pontos):

    jogadas  = {}
    try:
         arquivo = open("historico.txt","r",encoding="utf-8")
         jogadas = eval(arquivo.read())
         arquivo.close()
    except:
        arquivo = open("historico.txt","w",encoding="utf-8")
        arquivo.close()
 
    jogadas[nome] = pontos   
    arquivo = open("historico.txt","w",encoding="utf-8") 
    arquivo.write(str(jogadas))
    arquivo.close()

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(morteSound)
    pygame.mixer.music.load('assets/musicaDead.mp3')
    pygame.mixer.music.play(-1)

    while True: #mantém a tela aberta até que a tela seja fechada
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome) 
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_KP_ENTER:
                jogar(nome)
                
        tela.fill(branco)
        tela.blit(fundoDead, (0,0))
        buttonStart = pygame.draw.rect(tela, verdeEscuro, (35,495,750,100), 1)
        textoStart = fonteStart.render("RESTART", True, branco)
        tela.blit(textoStart, (400,510))
        textoEnter = fonte.render("Press enter to continue...", True, branco)
        tela.blit(textoEnter, (60,530))
      
        
        pygame.display.update()
        clock.tick(60)

def start():
    nome = simpledialog.askstring('AMOHGUS', 'Insira seu nome: ')
    pygame.mixer.music.load('assets/musicaStart.mp3')
    pygame.mixer.music.play(-1)
    while True: #mantém a tela aberta até que a tela seja fechada
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)
                elif buttonRanking.collidepoint(evento.pos):
                    ranking()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_KP_ENTER:
                jogar(nome)



        tela.fill(branco)
        tela.blit(fundoStart, (0,0))
        buttonStart = pygame.draw.rect(tela, preto, (110,482,600,100),0)
        buttonRanking = pygame.draw.rect(tela, preto, (35,130,200,50),0,30)
        textoStart = fonteStart.render("START", True, branco)
        textoNome = fonteStart.render('Bem vindo ' + nome, True, branco)
        textoRanking = fonte.render("Ranking", True, branco)
        tela.blit(textoRanking, (90,140))
        tela.blit(textoNome, (0, 60))
        tela.blit(textoStart, (330,482))
        pygame.display.update()
        clock.tick(60)

def ranking():
    estrelas = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8" )
        estrelas = eval(arquivo.read())
        arquivo.close()
    except:
        pass
    
    nomes = sorted(estrelas, key=estrelas.get,reverse=True)
    print(estrelas)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    start()

        tela.fill(preto)
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        textoStart = fonteStart.render("BACK TO START", True, branco)
        tela.blit(textoStart, (330,482))
        
        
        posicaoY = 50
        for key,nome in enumerate(nomes):
            if key == 13:
                break
            textoJogador = fonte.render(nome + " - "+str(estrelas[nome]), True, branco)
            tela.blit(textoJogador, (300,posicaoY))
            posicaoY = posicaoY + 30

            
        
        pygame.display.update()
        clock.tick(60)
start()  
