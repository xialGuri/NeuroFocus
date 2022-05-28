import pygame;


# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

FLASHSPEED = 500 # in milliseconds
FLASHDELAY = 200 # in milliseconds
BUTTONSIZE = 200
BUTTONGAPSIZE = 20
TIMEOUT = 4 #버튼을 누르지 않으면 4초후 게임 종료

XMARGIN = int((screen_width - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
YMARGIN = int((screen_height - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)

#                R    G    B
WHITE        = (255, 255, 255)
BLACK        = (  0,   0,   0)
BRIGHTRED    = (255,   0,   0)
RED          = (155,   0,   0)
BRIGHTGREEN  = (  0, 255,   0)
GREEN        = (  0, 155,   0)
BRIGHTBLUE   = (  0,   0, 255)
BLUE         = (  0,   0, 155)
BRIGHTYELLOW = (255, 255,   0)
YELLOW       = (155, 155,   0)
DARKGRAY     = ( 40,  40,  40)

# Rect objects for each of the four buttons
YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
BLUERECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
REDRECT = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
GREENRECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
bgColor = BLACK

def main():
    pygame.init()  # 초기화 (반드시 필요)
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BEEP1, BEEP2, BEEP3, BEEP4
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("neuroFocus")  # 게임 이름

    BASICFONT = pygame.font.Font("freesansbold.ttf", 16)
    infoSurf = BASICFONT.render("Match the Patter by Clicking on the button or using the Q,W,A,S keys.", 1, DARKGRAY)
    infoRect = infoSurf.get_rect()
    infoRect.topleft = (10, screen_height - 25)
    pattern = []  # 색깔 패턴을 저장한다.
    currentStep = 0  # 플레이어가 다음에 눌러야 하는 색깔
    lastClickTime = 0  # 플레이어가 이전 버튼을 누른 시간
    score = 0
    # 이 밑에 값이 False면 현재 시뮬레이트가 패턴을 보여주고 있는 상태이다.
    # True 면 버튼 클릭 기다리고 있다.
    waitingForInput = False

    ## pygame 은 while 문에서 게임이 실행된다
    while True:
        clickedButton = None
        DISPLAYSURF.fill(bgColor)
        drawButtons()

def drawSquare():
    pygame.draw.rect(DISPLAYSURF, YELLOW,YELLOWRECT)
    pygame.draw.rect(DISPLAYSURF, BLUE,   BLUERECT)
    pygame.draw.rect(DISPLAYSURF, RED,    REDRECT)
    pygame.draw.rect(DISPLAYSURF, GREEN,  GREENRECT)