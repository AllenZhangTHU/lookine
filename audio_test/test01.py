#-*- coding: utf-8 -*-

import cv2
import sys
import httplib, urllib, base64
import json
from math import floor
import sys,time
import time, threading
import base64
import requests
import matplotlib.pyplot as plt

import socket
import pygame


# sadnessT = 0
# surpriseT = 0
# fearT = 0
# disgustT = 0
# angerT = 0

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('/Users/steven/Desktop/Lookine/lookine/audio/aus/皱眉.mp3')
pygame.mixer.music.play()
#time.sleep(2)
#pygame.time.delay(1500)
print('扬眉')

while pygame.mixer.music.get_busy():
	time.sleep(1)
pygame.mixer.music.load('sadness.mp3')
pygame.mixer.music.play()
#time.sleep(2)
print('皱眉')

while pygame.mixer.music.get_busy():
	time.sleep(1)

pygame.mixer.music.load('surprise.mp3')
pygame.mixer.music.play()
#time.sleep(2)
print('嘴角上扬')

while pygame.mixer.music.get_busy():
	time.sleep(1)
pygame.mixer.music.load('sadness.mp3')
pygame.mixer.music.play()
#time.sleep(2)
print('皱眉')

while pygame.mixer.music.get_busy():
	time.sleep(1)
pygame.mixer.music.load('surprise.mp3')
pygame.mixer.music.play()
#time.sleep(2)
print('嘴角上扬')

while pygame.mixer.music.get_busy():
	time.sleep(1)

# pygame.mixer.music.load('/Users/steven/Desktop/Lookine/lookine/audio/aus/嘴角下拉.mp3')
# pygame.mixer.music.play()
# time.sleep(2.1)
# print('嘴角下拉')
#pygame.time.delay(1500)#等待5秒让filename.wav播放结束

# while 1:
#     if not pygame.mixer.music.get_busy():
#         pygame.mixer.music.load('/Users/steven/Desktop/Lookine/lookine/audio/aus/皱眉.mp3')
#         pygame.mixer.music.play()
#         print('皱眉')
#         pygame.time.delay(1500)#等待5秒让filename.wav播放结束
#         sys.exit()


# if data[2] == '1':
#     pygame.mixer.music.load('./audio/aus/皱眉.mp3')
#     pygame.mixer.music.play()
#     print('皱眉')
# if data[3] == '1':
#     pygame.mixer.music.load('./audio/aus/嘴角上扬.mp3')
#     pygame.mixer.music.play()
#     print('嘴角上扬')
# if data[4] == '1':
#     pygame.mixer.music.load('./audio/aus/嘴角下拉.mp3')
#     pygame.mixer.music.play()
#     print('嘴角下拉')
# if data[5] == '1':
#     pygame.mixer.music.load('./audio/aus/下巴皱起.mp3')
#     pygame.mixer.music.play()
#     print('下巴皱起')
# if data[6] == '1':
#     pygame.mixer.music.load('./audio/aus/嘴巴收紧.mp3')
#     pygame.mixer.music.play()
#     print('嘴巴收紧')
# if data[7] == '1':
#     pygame.mixer.music.load('./audio/aus/张大嘴.mp3')
#     pygame.mixer.music.play()
#     print('张大嘴')

