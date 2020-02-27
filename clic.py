#!/usr/bin/python3

from math import *
from random import *
import os
import contextlib
with contextlib.redirect_stdout(None):
	import pygame
	import pygame.gfxdraw
	from pygame import *

def wait_mouse_up():
	x = 1

	while (x == 1):
		for event in pygame.event.get():
			if (event.type == MOUSEBUTTONUP):
				x = 0
				break

def wait_key_up():
	x = 1

	while (x == 1):
		for event in pygame.event.get():
			if (event.type == KEYUP):
				x = 0
				break