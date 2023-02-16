import pygame #paygame é uma biblioteca(modulo) utilizado para jogos
pygame.init() # esse comando é importante para iniciar o paygame
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
x = input('digite algo para parar...')
