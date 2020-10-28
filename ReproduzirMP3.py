'''
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''

import pygame

pygame.mixer.init();
pygame.init();
pygame.mixer.music.load('caveSound.mp3');
pygame.mixer.music.play();
pygame.mixer.music.set_volume(1);
parar = input('Digite algo para parar...');
pygame.event.wait();


'''
from playsound import playsound

playsound('caveSound.mp3')
'''
