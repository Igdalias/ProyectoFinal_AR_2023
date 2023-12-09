import pygame
import sys

pygame.init()

width, height = 1000, 500
window = pygame.display.set_mode((width, height))
white = (255, 255, 255)

image_path = "final.png"
background = pygame.image.load(image_path)

car_x, car_y = width // 2, height // 2

carro = pygame.Surface((25,25), pygame.SRCALPHA)
pygame.draw.rect(carro,( 0,0,255), (0,0, 25,25))

brazo = pygame.Surface((15, 150), pygame.SRCALPHA)
pygame.draw.rect(brazo, (0, 128, 255), (0, 0, 30, 80))

garra = pygame.Surface((15, 180), pygame.SRCALPHA)
pygame.draw.rect(garra, (0, 128, 0), (0, 0, 30, 90))

ancho_garra = 2

centro_garra = pygame.Surface((ancho_garra, 181), pygame.SRCALPHA)
pygame.draw.rect(centro_garra, (255, 255, 255), (0, 0, 8, 90))

objeto1 = pygame.Surface((180, 40), pygame.SRCALPHA)
pygame.draw.rect(objeto1, (255, 0, 0), (0, 0, 180, 40))


speed = 2
angulo_brazo = 0
angulo_carro = 90
speed_ang = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #angulo_brazo = abs(angulo_brazo)
    #angulo_carro = abs(angulo_carro)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        """if angulo_carro<180:
            angulo_carro+=speed_ang
            angulo_brazo+=speed_ang
        else:
            angulo_carro -= speed_ang
            angulo_brazo -= speed_ang"""
        if car_x > 10:
            car_x -= speed
    if keys[pygame.K_RIGHT]:
        """if angulo_carro<0:
            angulo_carro+=speed_ang
            angulo_brazo+=speed_ang
        else:
            angulo_carro -= speed_ang
            angulo_brazo -= speed_ang"""
        if car_x < 990:
            car_x += speed
    if keys[pygame.K_UP]:
        """if angulo_carro<90:
            angulo_carro+=speed_ang
            angulo_brazo+=speed_ang
        else:
            angulo_carro -= speed_ang
            angulo_brazo -= speed_ang"""
        if car_y > 10:
            car_y -= speed
    if keys[pygame.K_DOWN]:
        """if angulo_carro<270:
            angulo_carro+=speed_ang
            angulo_brazo+=speed_ang
        else:
            angulo_carro -= speed_ang
            angulo_brazo -= speed_ang"""
        if car_y < 490:
            car_y += speed
    if keys[pygame.K_w]:
        if ancho_garra > 0:
            ancho_garra -= .2
    if keys[pygame.K_s]:
        if ancho_garra < 10:
            ancho_garra += .2
    if keys[pygame.K_d]:
        angulo_brazo -= speed_ang
    if keys[pygame.K_a]:
        angulo_brazo += speed_ang
    #angulo_brazo = abs(angulo_brazo)%360
    #angulo_carro = abs(angulo_carro)%360
    #print(angulo_carro, angulo_brazo)


    window.fill(white)
    window.blit(background, (0, 0))
    #pygame.draw.rect(window, (0, 0, 255), (car_x - 12, car_y - 12, 25, 25))

    rotated_objeto1 = pygame.transform.rotate(objeto1, 0)
    rotated_rect = rotated_objeto1.get_rect(center=(300, 25))
    window.blit(rotated_objeto1, rotated_rect.topleft)

    rotated_carro = pygame.transform.rotate(carro, angulo_carro)
    rotated_rect_carro = rotated_carro.get_rect(center=(car_x, car_y))
    window.blit(rotated_carro, rotated_rect_carro.topleft)

    centro_garra = pygame.Surface((ancho_garra, 180), pygame.SRCALPHA)
    pygame.draw.rect(centro_garra, (255, 255, 255), (0, 0, 10, 90))

    rotated_garra = pygame.transform.rotate(garra, angulo_brazo)
    rotated_rect_garra = rotated_garra.get_rect(center=(car_x, car_y))
    window.blit(rotated_garra, rotated_rect_garra.topleft)

    rotated_centro_garra = pygame.transform.rotate(centro_garra, angulo_brazo)
    rotated_rect_centro_garra = rotated_centro_garra.get_rect(center=(car_x, car_y))
    window.blit(rotated_centro_garra, rotated_rect_centro_garra.topleft)

    rotated_brazo = pygame.transform.rotate(brazo, angulo_brazo)
    rotated_rect = rotated_brazo.get_rect(center=(car_x, car_y))
    window.blit(rotated_brazo, rotated_rect.topleft)

    pygame.display.flip()
