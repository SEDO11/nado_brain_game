import pygame # 파이게임 라이브러리 사용 설정

def display_start_screen(): # 시작 버튼 표시, 그리기
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5) # 흰색 동그라미를 그리고 중심좌표는 start_button 의 중심좌표를 따라가고, 반지름은 60, 두께는 5
    font = pygame.font.Font(None,30) # 파이썬 기본폰트, 글자 크기는 30으로 설정
    text = font.render('Start',True, WHITE)  #텍스트가 표시되는 표면을 만듬, Start문구, 하얀색
    screen.blit(text,(center_x - 20, center_y - 10)) # 시작 버튼 내에 글자 띄우기

def display_game_screen(): # 게임 화면 표시
    print("Game Start") 

# 마우스를 클릭해서 얻은 좌표값을 position에 저장 
def check_buttons(position): # 들어온 좌표 값 확인
    global start
    if start_button.collidepoint(position): # 마우스로 start_button의 범위에 해당하는 영역을 누른게 확인 될 때, collidepoint 충돌영역
        start = True #시작

#초기화
pygame.init()
screen_width = 1280 #가로크기
screen_height = 720 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height)) # 게임 창 띄우기
pygame.display.set_caption("Brain Game") #게임 이름

#시작 버튼
center_x = 120 # 센터 x축
center_y = screen_height-120 # 센터 y축
start_button = pygame.Rect(0, 0, 120, 120) #버튼 생성
start_button.center = (center_x, center_y) # 버튼의 중심위치 설정

#화면색깔
BLACK = (0, 0, 0) #RGB
WHITE = (255, 255, 255) #RGB

# 게임 시작 여부
start = False # 초기에 게임을 시작하지 않았다고 설정


#게임 루프
running = True # 게임이 실행중인가?
while running:
    click_pos = None # null값 설정, 파이썬은 None으로 표현

    #이벤트루프
    for event in pygame.event.get(): #어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트인가?
            running = False #게임이 더 이상 실행중이 아니다.
        elif event.type == pygame.MOUSEBUTTONUP: # 사용자가 마우스를 클릭했을때
            click_pos = pygame.mouse.get_pos() #마우스 좌표값 변수 설정
            print(click_pos) # 마우스 좌표값 출력

    #화면 전체를 까맣게 색칠
    screen.fill(BLACK) #fill은 채우다라는 뜻이다. 해석하면 검은색으로 스크린을 채워라는 뜻

    if start: # start 버튼을 눌렀으면, True 상태면
        display_game_screen() #게임 화면 표시

    else: # start 버튼을 누르지 않았으면
        display_start_screen()         # 시작 화면 표시

    if click_pos: #사용자가 클릭한 좌표값이 있다면
        check_buttons(click_pos) # 클릭한 좌표의 값을 확인해봄
    
    # 화면 업데이트
    pygame.display.update()

#게임 종료
pygame.quit()