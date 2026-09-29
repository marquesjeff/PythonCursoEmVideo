import pygame

pygame.mixer.init()
pygame.mixer.music.load("rain.mp3")
pygame.mixer.music.play()

input("Pressione Enter para parar...")
pygame.mixer.music.stop()