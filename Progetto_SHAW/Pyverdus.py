import pygame
import random
pygame.init()

sfondo_menu= pygame.image.load('Giochi\\Progetto_SHAW\\Sfondo.png')
sfondo_menu = pygame.transform.scale_by(sfondo_menu, 0.7)
larghezzaSfondo = sfondo_menu.get_width()
altezzaSfondo = sfondo_menu.get_height()
sfondo_preparazione= pygame.image.load('Giochi\\Progetto_SHAW\\Preparazione.jpg')
sfondo_preparazione = pygame.transform.scale(sfondo_preparazione, (larghezzaSfondo, altezzaSfondo))
schermo = pygame.display.set_mode((larghezzaSfondo, altezzaSfondo))
pygame.display.set_caption('Schermo di gioco')
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("Arial", 30)
testo = font.render("Pyverse", True, (255, 255, 0))
testo = pygame.transform.scale_by(testo, 3)
larghezza_testo = testo.get_width()

# Pulsante: Gioca
larghezza_rett = 200
altezza_rett = 80
x = (larghezzaSfondo - larghezza_rett) / 2
y = 300
pulsante_rect = pygame.Rect(x, y, larghezza_rett, altezza_rett)
testo_pul = font.render("GIOCA", True, (255, 255, 255))

# Pulsante: Esci
x2 = (larghezzaSfondo - larghezza_rett) / 2
y2 = 400
pulsante_rect2 = pygame.Rect(x2, y2, larghezza_rett, altezza_rett)
testo_pul2 = font.render("ESCI", True, (255, 255, 255))

#pulsante: avanti
x_avanti = (larghezzaSfondo - larghezza_rett) / 2
y_avanti = 700
pulsante_rect_avanti = pygame.Rect(x_avanti, y_avanti, larghezza_rett, altezza_rett)
testo_pul_avanti = font.render("AVANTI", True, (255, 255, 255))


pokemon=[
        "Charizard",
        "Greninja",
        "Torterra",
        "Crokodile",
        "Hornet",
        "Thor"  
]
squadra_player = [

] 

for i in range (3):
    random_pokemon = random.choice(pokemon)
    pokemon.remove(random_pokemon)
    squadra_player.append(random_pokemon)    

# Stato iniziale
stato = "menu"
gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if stato == "menu":
                if pulsante_rect.collidepoint(event.pos):
                    stato = "Preparazione"   # CAMBIO SCHERMATA
                elif pulsante_rect2.collidepoint(event.pos):
                    gameOver = True
                elif stato == "Preparazione":
                    stato="gioco"
                elif stato == "gioco":
                    pass  

    # Disegno in base allo stato
    if stato == "menu":
        schermo.blit(sfondo_menu, (0, 0))

        # Pulsante Gioca
        pygame.draw.rect(schermo, (116, 234, 62), pulsante_rect, border_radius=20)
        schermo.blit(
            testo_pul,
            (pulsante_rect.x + (pulsante_rect.width - testo_pul.get_width()) // 2,
             pulsante_rect.y + (pulsante_rect.height - testo_pul.get_height()) // 2)
        )

        # Pulsante Esci
        pygame.draw.rect(schermo, (205, 0, 0), pulsante_rect2, border_radius=20)
        schermo.blit(
            testo_pul2,
            (pulsante_rect2.x + (pulsante_rect2.width - testo_pul2.get_width()) // 2,
             pulsante_rect2.y + (pulsante_rect2.height - testo_pul2.get_height()) // 2)
        )

        # Titolo
        schermo.blit(testo, ((larghezzaSfondo - larghezza_testo) / 2, 100))

    elif stato == "Preparazione":
        schermo.blit(sfondo_preparazione, (0, 0))
        messaggio = font.render("LA TUA SQUADRA E' COMPOSTA DA: ", True, (255, 255, 255))
        larghezza_messaggio = messaggio.get_width()
        schermo.blit(messaggio, ((larghezzaSfondo - larghezza_messaggio) / 2, 50))

        # Pulsante Avanti
        pygame.draw.rect(schermo, (0, 128, 255), pulsante_rect_avanti, border_radius=20)
        schermo.blit(
            testo_pul_avanti,
            (pulsante_rect_avanti.x + (pulsante_rect_avanti.width - testo_pul_avanti.get_width()) // 2,
             pulsante_rect_avanti.y + (pulsante_rect_avanti.height - testo_pul_avanti.get_height()) // 2)
        )

    pygame.display.update()
    clock.tick(60)

pygame.quit()