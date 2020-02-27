#!/usr/bin/python3

from math import *
from random import *
import os
import contextlib
with contextlib.redirect_stdout(None):
	import pygame
	import pygame.gfxdraw
	from pygame import *

def displayText(window, text, pos, color, size, aa=True, alpha=255, bolt=False):
	myfont = pygame.font.SysFont("test", size, bolt)
	#myfont = pygame.font.Font("./assets/SupersonicRocketship.ttf", size)
	display = myfont.render(text, aa, color)
	display.set_alpha(alpha)

	window.blit(display, (pos[0] - display.get_rect().width / 2, pos[1] - display.get_rect().height / 2))