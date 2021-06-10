import pygame

def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    # 흰색으로 동그라미를 그리는데 중심좌표는 start_button 의 중심좌표를 따라가고, 반지름은 60, 두께는 5
    

#초기화
pygame.init()
screen_width = 1280 #가로크기
screen_height = 720 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brain Game") #게임 이름

#시작 버튼
start_button = pygame.Rect(0, 0, 120, 120) #버튼 생성
start_button.center = (120, screen_height-120) # 버튼의 중심위치 설정

#화면색깔
BLACK = (0, 0, 0) #RGB
WHITE = (255, 255, 255)

#게임 루프
running = True # 게임이 실행중인가?
while running:
    #이벤트루프
    for event in pygame.event.get(): #어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트인가?
            running = False #게임이 더 이상 실행중이 아니다.

    #화면 전체를 까맣게 색칠
    screen.fill(BLACK)

    # 시작 화면 표시
    display_start_screen()

    # 화면 업데이트
    pygame.display.update()


#게임 종료
pygame.quit()


