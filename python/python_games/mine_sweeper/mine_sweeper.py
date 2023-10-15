import sys
from math import floor
from random import randint
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

WIDTH = 20
HEIGHT = 15
SIZE = 50
NUM_OF_BOMBS = 20
EMPTY = 0
BOMB = 1
OPENED = 2
OPEN_COUNT = 0
FLAG = 3
CHECKED = [
    [0 for _ in range(WIDTH)] 
    for _ in range(HEIGHT)
]

pygame.init()
SURFACE = pygame.display.set_mode([WIDTH * SIZE, HEIGHT * SIZE])
FPSCLOCK = pygame.time.Clock()

def num_of_bomb(field, x_pos, y_pos):
    """
    특정 칸 주위에 있는 8개의 칸에서 총 몇개의 BOMB 가 있는지
    확인해주는 함수
    """
    count = 0
    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and \
               field[ypos][xpos]["state"] == BOMB:
                count += 1

    return count

def open_tile(field, x_pos, y_pos):
    global OPEN_COUNT

    # 확인이 이전에 됐었다면 함수 종료
    if CHECKED[y_pos][x_pos]:
        return

    # 확인을 하게 될 타일을 마킹
    CHECKED[y_pos][x_pos] = True

    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and field[ypos][xpos]["state"] == EMPTY: 
                field[ypos][xpos]["state"] = OPENED
                OPEN_COUNT += 1
                count = num_of_bomb(field, xpos, ypos)
                # count, 즉 주위 폭탄이 없고 확인하는 타일이 
                # 기존 함수에 넘겨진 타일이 아니라면, 타일 열기
                if count == 0 and not (xpos == x_pos and ypos == y_pos):
                    # 재귀로 타일 반복 확인하며 주위에 폭탄이 없는 타일을 열기
                    open_tile(field, xpos, ypos)


def main():
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)
    message_clear = largefont.render("!!CLEARED!!",
                                     True,
                                     (0, 255, 255))
    message_over = largefont.render("GAME OVER",
                                    True,
                                    (0, 255, 255))
    message_rect = message_clear.get_rect()
    message_rect.center = (WIDTH * SIZE / 2, HEIGHT * SIZE / 2)
    game_over = False

    # 필드를 준비, matrix 로 0 으로 일단 채움 (EMPTY = 0)
    field = [[{"state":EMPTY, "flag":False} for xpos in range(WIDTH)]
             for ypos in range(HEIGHT)]

    # 폭탄 뿌리기
    count = 0
    while count < NUM_OF_BOMBS:
        xpos, ypos = randint(0, WIDTH - 1), randint(0, HEIGHT - 1)

        if field[ypos][xpos]["state"] == EMPTY:
            field[ypos][xpos]["state"] = BOMB
            count += 1

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # mouse left click 일 경우 (event.button == 1 은 왼쪽 마우스
            # 클릭임)
            if event.type == MOUSEBUTTONDOWN:
                xpos, ypos = floor(event.pos[0] / SIZE),\
                        floor(event.pos[1] / SIZE)
                if event.button == 1:
                    if field[ypos][xpos]["state"] == BOMB:
                        game_over = True
                    else:
                        open_tile(field, xpos, ypos)
                elif event.button == 3:
                    field[ypos][xpos]["flag"] = not field[ypos][xpos]["flag"]

        SURFACE.fill((0, 0, 0))
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                tile = field[ypos][xpos]
                tile_state = tile["state"]
                rect = (xpos * SIZE, ypos * SIZE, SIZE, SIZE)

                if tile_state in (EMPTY, BOMB, OPENED):
                    # print(f"{tile_state=}")
                    pygame.draw.rect(SURFACE,
                                     (192, 192, 192), rect)
                    if game_over and tile_state == BOMB:
                        pygame.draw.ellipse(SURFACE,
                                            (225, 225, 0), rect)
                    elif tile_state == OPENED:
                        # add square if tile has been opened
                        pygame.draw.rect(SURFACE,
                                         (0, 0, 0), rect)
                        count = num_of_bomb(field, xpos, ypos)
                        # add number to tile if there is a bomb near it
                        if count > 0:
                            num_image = smallfont.render(
                                "{}".format(count), True, (225, 225, 0))
                            # print(f"{count=}")
                            SURFACE.blit(num_image,
                                         (xpos*SIZE+10, ypos*SIZE+10))
                    elif tile["flag"]:
                        pygame.draw.ellipse(SURFACE,
                                            (225, 0, 225), rect)

        # 게임 그리기
        for index in range(0, WIDTH*SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96),
                             (index, 0), (index, HEIGHT*SIZE))
        for index in range(0, HEIGHT*SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96),
                             (0, index), (WIDTH*SIZE, index))


        if OPEN_COUNT == WIDTH*HEIGHT - NUM_OF_BOMBS:
            SURFACE.blit(message_clear, message_rect.topleft)
        elif game_over:
            SURFACE.blit(message_over, message_rect.topleft)

        pygame.display.update()
        FPSCLOCK.tick(15)


if __name__ == "__main__":
    main()


