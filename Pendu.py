import pygame
import random
import string

pygame.init()

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)

largeur, hauteur = 800, 470
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Jeu du Pendu')

with open("mots.txt", "r") as file:
    mots = file.read().splitlines()

mot_a_deviner = random.choice(mots).upper()
lettres_devinées = set()
erreurs = 0
max_erreurs = 6

hangman_images = [
    pygame.image.load('./images/hangman0.png'),
    pygame.image.load('./images/hangman1.png'),
    pygame.image.load('./images/hangman2.png'),
    pygame.image.load('./images/hangman3.png'),
    pygame.image.load('./images/hangman4.png'),
    pygame.image.load('./images/hangman5.png'),
    pygame.image.load('./images/hangman6.png'),
    pygame.image.load('./images/hangman7.png'),
    pygame.image.load('./images/hangman8.png')
]
hangman_display = 0

running = True
while running:
    fenetre.fill(BLANC)

    affichage_mot = ''
    for lettre in mot_a_deviner:
        if lettre in lettres_devinées or lettre == ' ':
            affichage_mot += lettre + ' '
        else:
            affichage_mot += '_ '

    police = pygame.font.SysFont('Arial', 30)
    texte = police.render(affichage_mot, True, NOIR)
    fenetre.blit(texte, (50, 200))

    fenetre.blit(hangman_images[erreurs], (320, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in range(256):
                lettre_choisie = chr(event.key).upper()
                if lettre_choisie in string.ascii_uppercase:
                    if lettre_choisie not in lettres_devinées:
                        lettres_devinées.add(lettre_choisie)
                        if lettre_choisie not in mot_a_deviner:
                            erreurs += 1

    if erreurs >= max_erreurs:
        pass
    elif all(lettre in lettres_devinées or lettre == ' ' for lettre in mot_a_deviner):
        pass

    pygame.display.update()
pygame.quit()