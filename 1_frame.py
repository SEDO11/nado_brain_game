import pygame

#초기화
pygame.init()
screen_width = 1280 #가로크기
screen_height = 720 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brain Game") #게임 이름

#게임 루프
running = True # 게임이 실행중인가?
while running:
    #이벤트루프
    for event in pygame.event.get(): #어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트인가?
            running = False #게임이 더 이상 실행중이 아니다.

#게임 종료
pygame.quit()


