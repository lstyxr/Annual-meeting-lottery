import pygame
pygame.init()

screen = pygame.display.set_mode([800, 600])
screen.fill([255,255,255])


def box_text(surface, font, x_start, x_end, y_start, words, colour):
    x = x_start
    y = y_start

    for word in words:
        word_t = font.render(word + "、", True, colour)
        if word_t.get_width() + x <= x_end:
            surface.blit(word_t, (x, y))
            x += word_t.get_width() + 2
        else:
            y += word_t.get_height() + 4
            x = x_start
            surface.blit(word_t, (x, y))
            x += word_t.get_width() + 2

flag = False

def main():
    count = 0
    font = pygame.font.Font('simhei.ttf', 64)
    while True:
        flag = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    count += 1
                    print(flag)
                    flag = True
                    print(flag)
                    print("OK!" + str(count))
        

        words = ['刘笑宇', '陈文', '罗正恩', '张善琪', '周启维', '唐显祥', '李勇', '邓正好', '曾祥洪', '刘洲', '郑世彬', '王亮', '巩玲', '张翀', '林云月', '李彦秋', '曾令云', '李勇祥', '查小峰', '张兴建', '张兴明', '曹先红', '杨晓红', '钟亮', '曾祥春', '罗潇', '肖淞尹', '陈德明', '赵忠伟', '张洪程', '付永波', '陈禾蕤', '何大平', '张兴荣', '徐宗兵', '张进', '陈涛', '黄金鹏']
        box_text(screen, font, 10, 650, 10, words, (255,0,0,0))
        pygame.display.update()

if __name__ == "__main__":
    main()
