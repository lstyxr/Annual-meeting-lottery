#coding:utf-8

import sys
import pygame
import random
from pygame.locals import *
import pandas as pd
from PIL import ImageGrab
from name_format import name_format
import time

fullScreen = True
tip = "幸运大抽奖"

# 先确定多少组 n, 再平均分配每组多少个人m,返回分组的n个列表
def getData(n):
    df = pd.read_excel("人员列表.xlsx")
    name_list = df["姓名"].tolist()
    total = []

    # 随机排序列表，随机抽奖关键
    random.shuffle(name_list)
    # 随机抽取幸运奖 45 名
    win_list = name_list[:45]
    total.append(win_list)
    result = pd.DataFrame(win_list)
    result.to_excel("幸运大抽奖.xlsx")
    return name_list, total

if __name__ == "__main__":
    # 输入抽奖次数n
    n = 1
    name_list, total = getData(n)
    print(len(total))

    pygame.init()

    bg = 'bg_1920x1080.png'
    screen = pygame.display.set_mode((1920, 1080), 0, 32)

    # 控制起始横纵坐标
    width = 1920
    height = 1080
    x_start = width / 2 - 950
    x_end = width / 2 + 950
    y_start = height / 2 - 380 
    x = x_start
    y = y_start

    pygame.display.set_caption("幸运大抽奖...")

    b = pygame.image.load(bg).convert()
    screen.blit(b, (0, 0))

    pygame.mixer.init()
    pygame.mixer.music.load('9224.wav')
    #pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

    num = 0
    pause_flag = True
    is_done = False
    djs = False
    jp_isdone = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    num += 1
                    print(pause_flag)
                    pause_flag = not pause_flag
                    is_done = False 
                    if num % 2 != 0:
                        djs = True

                    if num % 2 == 0:
                        jp_isdone = False
                    pygame.mixer.music.stop()
                    print("OK!" + str(num))

        if not pause_flag:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()

            if djs:
                font = pygame.font.Font("simhei.ttf", 600)
                Daojs = ["3", "2", "1", "0"]
                for js in Daojs:
                    screen.blit(b, (0, 0))
                    text_djs = font.render(js, True, (255, 255, 255))
                    #screen.blit(text_djs, (width/2 - 250, height/2 - 300))
                    text_obj_pos = text_djs.get_rect()
                    text_obj_pos.center = (width/2, height/2)
                    screen.blit(text_djs, text_obj_pos)
                    time.sleep(1)
                    djs = False
                    pygame.display.update()
            # 前排滚动显示
            text_context = '%s %s %s %s %s %s' % (
                    name_list[random.randint(0, len(name_list)-1)],
                    name_list[random.randint(0, len(name_list)-1)], 
                    name_list[random.randint(0, len(name_list)-1)], 
                    name_list[random.randint(0, len(name_list)-1)], 
                    name_list[random.randint(0, len(name_list)-1)], 
                    name_list[random.randint(0, len(name_list)-1)]
            )
            font = pygame.font.Font("simhei.ttf", 80)
            text_obj = font.render(text_context, True, (255, 255, 255), (255, 0, 0))

            # 清屏
            screen.blit(b, (0, 0))
            screen.blit(text_obj, (300, 180))

        if num > 0 and num % 2 == 0 and num <= n*2 and pause_flag and not is_done:
            screen.blit(b, (0, 0))
            sub_list = total.pop() 
            print(sub_list)
            print("第{}次".format(num / 2))
            font = pygame.font.Font("simhei.ttf", 66)

            l = len(sub_list)
            for i, word in enumerate(sub_list):
                word = name_format(word)
                if i == l - 1:
                    word_t = font.render(word, True, (255,255,255))
                else:
                    word_t = font.render(word + f"{chr(12288)}", True, (255,255,255))
                if word_t.get_width() + x <= x_end:
                    screen.blit(word_t, (x, y))
                    x += word_t.get_width() + 2
                else:
                    y += word_t.get_height() + 22
                    x = x_start
                    screen.blit(word_t, (x, y))
                    x += word_t.get_width() + 2

            # 初始化坐标x y
            x = x_start
            y = y_start

            is_done = not is_done
        
        if num > 0 and num % 2 == 0 and num <= n*2 and pause_flag:
            pic = ImageGrab.grab()
            pic.save(tip + "{}.jpg".format(num))

        font = pygame.font.Font("simhei.ttf", 78)

        # 顶部提示
        text_obj_2 = font.render('幸运大抽奖', True, (255, 255, 255))
        text_obj_2_pos = text_obj_2.get_rect()
        text_obj_2_pos.center = (width/2, 100)
        screen.blit(text_obj_2, text_obj_2_pos)

        # 底部提示
        text_obj = font.render('祝公司蓬勃发展，祝同事万事如意!', True, (255, 255, 255))
        text_obj_pos = text_obj.get_rect()
        text_obj_pos.center = (width/2, 980)
        screen.blit(text_obj, text_obj_pos)

        pygame.display.update()
        if num > 0 and num % 2 == 0 and num <= n*2 and pause_flag and not jp_isdone:
            pic = ImageGrab.grab()
            pic.save(tip + "{}.jpg".format(num))
            jp_isdone = True
