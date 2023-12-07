import tkinter as tk
from tkinter import messagebox

def countdown(seconds):
    if seconds <= 0:
        messagebox.showinfo("倒计时结束", "时间到！")
    else:
        messagebox.showinfo("倒计时", "还剩下{}秒".format(seconds))
        root.after(1000, countdown, seconds-1)

root = tk.Tk()
root.withdraw()
countdown(10)
root.mainloop()

import pygame
import time

def countdown(seconds):
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    while seconds >= 0:
        screen.fill((255, 255, 255))
        text = font.render("倒计时: {}秒".format(seconds), True, (0, 0, 0))
        screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        seconds -= 1
        time.sleep(1)
        clock.tick(1)

countdown(10)

import time

def countdown(seconds):
    while seconds >= 0:
        if seconds == 0:
            print("倒计时结束")
        else:
            print("倒计时: {}秒".format(seconds))
        seconds -= 1
        time.sleep(1)

countdown(10)
