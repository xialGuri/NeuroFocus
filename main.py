import pygame
from pygame.locals import *
import ctypes

# hz 설정
hz1 = 1;
hz2 = 10;
hz3 = 10;
hz4 = 10;

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



# 4. 메인 이벤트
def main():

    # 전역 변수 셋팅 (아래의 변수들을 전역변수로 다른 함수에 사용 가능)
    global screen, infoObject, WINDOWWIDTH, WINDOWHEIGHT, YELLOWRECT, BLUERECT, REDRECT, GREENRECT, buttonsize, buttongapsize

    #  게임 초기화
    pygame.init()

    #창 크기 (전체 게임 화면)
    infoObject = pygame.display.Info()
    WINDOWWIDTH = infoObject.current_w
    WINDOWHEIGHT = infoObject.current_h

    # 각 이미지의 크기 설정
    buttonsize = 200
    buttongapsize = 20

    XMARGIN = int((infoObject.current_w - (2 * buttonsize) - buttongapsize) / 2)
    YMARGIN = int((infoObject.current_h - (2 * buttonsize) - buttongapsize) / 2)

    # Rect objects for each of the four buttons
    YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, buttonsize, buttonsize)
    BLUERECT = pygame.Rect(XMARGIN + buttonsize + buttongapsize, YMARGIN, buttonsize, buttonsize)
    REDRECT = pygame.Rect(XMARGIN, YMARGIN + buttonsize + buttongapsize, buttonsize, buttonsize)
    GREENRECT = pygame.Rect(XMARGIN + buttonsize + buttongapsize, YMARGIN + buttonsize + buttongapsize, buttonsize, buttonsize)



    # 게임 사이즈
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    # 게임 이름 셋팅
    pygame.display.set_caption("NeruoFocus")

    # Loop until the user clicks the close button.
    done = False

    # 실제 게임 시작
    while not done:

        # 각종 입력 감지
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(WHITE)
        drawButtons()
        loadImag()
        # flashButtonAnimation()
        pygame.display.flip()

    # 게임 종료
    pygame.quit()


def loadImag():
    # 가운데 이미지 불러오기
    img = pygame.image.load("image/plus.png")
    img = pygame.transform.scale(img, (25, 25))
    screen.blit(img, (WINDOWWIDTH/2, WINDOWHEIGHT/2))
    pygame.display.update()
    
    
def drawButtons():
    pygame.draw.rect(screen, YELLOW, YELLOWRECT)
    pygame.draw.rect(screen, BLUE,   BLUERECT)
    pygame.draw.rect(screen, RED,    REDRECT)
    pygame.draw.rect(screen, GREEN,  GREENRECT)

def flashButtonAnimation(animationSpeed=50):
    origSurf = screen.copy()
    flashSurf = pygame.Surface((buttonsize,buttonsize))
    flashSurf = flashSurf.convert_alpha()
    r1, g1, b1 = BRIGHTYELLOW
    r2, g2, b2 = BRIGHTBLUE
    r3, g3, b3 = BRIGHTRED
    r4, g4, b4 = BRIGHTGREEN
    rectangle = GREENRECT
    screen.blit(origSurf, (0, 0))
    flashSurf.fill((r1, g1, b1))
    screen.blit(flashSurf, rectangle.topleft)
    pygame.display.update()
    clock.tick(1)
    screen.blit(origSurf, (0, 0))
    # for start, end, step in ((0,255,1),(255,0,-1)): #애니메이션 루프
    #     for alpha in range(start, end, animationSpeed*step):
    #         screen.blit(origSurf,(0,0))
    #         flashSurf.fill((r1,g1,b1,alpha))
    #         # flashSurf.fill((r2, g2, b2, alpha))
    #         # flashSurf.fill((r3, g3, b3, alpha))
    #         # flashSurf.fill((r4, g4, b4, alpha))
    #         screen.blit(flashSurf,rectangle.topleft)
    #         pygame.display.update()
    #         clock.tick(1)
    # screen.blit(origSurf,(0,0))

if __name__ == "__main__":
    main()
