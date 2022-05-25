
from cv2 import cv2
import pygame

record_time_list = []

電腦拳字串 = []

continu_time = pygame.time.get_ticks()

record_time_list.append(continu_time)  # 2

if record_time_list[0] + 1000 < continu_time:
    cv2.putText(顯示用視窗, "2", (600, 400),
                cv2.QT_FONT_NORMAL, 5, (0, 250, 250), 5)

    record_time_list2.append(continu_time)

    if record_time_list2[0]+300 < continu_time:

        cv2.putText(顯示用視窗, "2", (600, 400),
                    cv2.QT_FONT_NORMAL, 5, (0, 250, 250), 5)

        record_time_list3.append(continu_time)

        if record_time_list3[0]+300 < continu_time:

            cv2.putText("1", (800, 400), cv2.QT_FONT_NORMAL,
                        5, (0, 250, 250), 5)

            record_time_list4.append(continu_time)
            if record_time_list4[0] + 300 < continu_time:

                準備好了嗎 = True
