import pygame
from pygame.locals import *
import ctypes

clock = pygame.time.Clock()

# 색깔지정 변수
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


BackCard = pygame.image.load("image/BackOfCard.jpeg")
CheckerBoard = pygame.image.load("image/CheckerBoard.jpeg")

BackCard = pygame.transform.scale(BackCard, (300, 300))
CheckerBoard = pygame.transform.scale(BackCard, (300, 300))
BackCard_RCT = BackCard.get_rect()

# 4. 메인 이벤트
def main():
    # 전역 변수 셋팅 (아래의 변수들을 다른 함수에 사용 가능)
    global screen, infoObject, WINDOWWIDTH, \
        WINDOWHEIGHT, buttonsize, buttongapsize, XMARGIN, \
        YMARGIN, FirstRECT, SecondRECT, ThirdRECT, FourthRECT, DISPLAYSURF \
        CheckerBoard, BackCard

    # 게임 초기화
    pygame.init()

    # 창 크기 (전체 게임 화면)
    infoObject = pygame.display.Info()
    WINDOWWIDTH = infoObject.current_w
    WINDOWHEIGHT = infoObject.current_h

    # 각 이미지의 크기 설정
    buttonsize = 300
    buttongapsize = 200

    XMARGIN = int((infoObject.current_w - (2 * buttonsize) - buttongapsize) / 2)
    YMARGIN = int((infoObject.current_h - (2 * buttonsize) - buttongapsize) / 2)

    FirstRECT = pygame.Rect(XMARGIN, YMARGIN, buttonsize, buttonsize)
    SecondRECT = pygame.Rect(XMARGIN + buttonsize + buttongapsize, YMARGIN, buttonsize, buttonsize)
    ThirdRECT = pygame.Rect(XMARGIN, YMARGIN + buttonsize + buttongapsize, buttonsize, buttonsize)
    FourthRECT = pygame.Rect(XMARGIN + buttonsize + buttongapsize, YMARGIN + buttonsize + buttongapsize, buttonsize, buttonsize)

    # 게임 사이즈
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    # 게임 이름 셋팅
    pygame.display.set_caption("NeruoFocus")

    # While 루프를 돌기위해 사용된 변수
    done = False

    # 실제 게임 시작
    while not done:
        # 각종 입력 감지
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(WHITE)
        # drawBackCards()
        loadCenterImg()
        #flashButtonAnimation()

        img_names = [BackCard, CheckerBoard]
        all_imgs = {}
        for img in img_names:
            all_imgs[img] = pygame.image.load(img)
        # flashButtonAnimation2()
        # flashButtonAnimation3()
        # flashButtonAnimation4()
        pygame.display.flip()

    # 게임 종료
    pygame.quit()

# 시선 집중 덧셈 기호 생성 함수
def loadCenterImg():
    # 가운데 이미지 불러오기
    img = pygame.image.load("image/plus.png")
    img = pygame.transform.scale(img, (25, 25))
    screen.blit(img, (WINDOWWIDTH / 2 - 13, WINDOWHEIGHT / 2 - 13))
    pygame.display.update()

# 그림 뒷면
def drawBackCards():
    #  사진 띄우기
    screen.blit(BackCard, (XMARGIN - 180, YMARGIN - 40))
    screen.blit(BackCard, (XMARGIN + 180 + buttonsize + buttongapsize, YMARGIN - 40))
    screen.blit(BackCard, (XMARGIN - 180, YMARGIN + buttonsize + buttongapsize - 53))
    screen.blit(BackCard, (XMARGIN + 180 + buttonsize + buttongapsize, YMARGIN + buttonsize + buttongapsize - 53))

# 깜빡임 조정 함수
def flashButtonAnimation(animationSpeed=1000):
    origSurf = screen.copy()
    screen.blit(BackCard, (XMARGIN - 180, YMARGIN - 40))
    pygame.display.update()
    clock.tick(1)
    screen.blit(origSurf, (0, 0))

def flashButtonAnimation2(animationSpeed=1000):
    origSurf = screen.copy()
    screen.blit(BackCard, (XMARGIN + 180 + buttonsize + buttongapsize, YMARGIN - 40))
    pygame.display.update()
    clock.tick(1)
    screen.blit(origSurf, (0, 0))

def flashButtonAnimation3(animationSpeed=1000):
    origSurf = screen.copy()
    screen.blit(BackCard, (XMARGIN - 180, YMARGIN + buttonsize + buttongapsize - 53))
    pygame.display.update()
    clock.tick(1)
    screen.blit(origSurf, (0, 0))

def flashButtonAnimation4(animationSpeed=1000):
    origSurf = screen.copy()
    screen.blit(BackCard, (XMARGIN + 180 + buttonsize + buttongapsize, YMARGIN + buttonsize + buttongapsize - 53))
    pygame.display.update()
    clock.tick(3)
    screen.blit(origSurf, (0, 0))

if __name__ == "__main__":
    main()
