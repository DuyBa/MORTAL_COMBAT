import pygame
from fighter import Fighter
from pygame import mixer

from fighting import Fighting

#cac icon co het trong file 'icon to link'


# [[231, 190], 2.3, [112, 63], [6, 8, 2, 8, 8, 4, 7], "assets/Wizard Pack/aa.png"]

# [[250, 250], 3, [112, 107], [8, 8, 1, 8, 8, 3, 7], "assets/muontam/images/wizard/Sprites/wizard.png"]

# [[162, 162], 4, [72, 56], [10, 8, 1, 7 ,7, 3, 7], "assets/muontam/images/warrior/Sprites/warrior.png"]

# [[64, 44], 4.9, [15, 7], [6, 8, 3, 12 ,10, 4, 10], "assets/Warrior-V1.3/aaa.png"]

# 4 thang o tren se link vao 4 bieu tuong nhan vat luc chon nhan vat
#bro lam thao tac truyen du lieu vao 2 thang hero1 va hero 2 duoi day
#vi du:
# hero1= [[231, 190], 2.3, [112, 63], [6, 8, 2, 8, 8, 4, 7], "assets/Wizard Pack/aa.png"]
# hero2= [[250, 250], 3, [112, 107], [8, 8, 1, 8, 8, 3, 7], "assets/muontam/images/wizard/Sprites/wizard.png"]

#cac dia chi nhac:
		#"assets/audio/lop13.mp3"    "assets/audio/flo.mp3"
#cac dia chi background:
		#"assets/Flat Night 2 BG/Flat Night 2 BG.png" "assets/Background/Demo.png"

#tuong tu bro link cac dia chi vao bieu tuong nhac, bieu tuong background de no truyen du lieu vao 2 thang bien take_bg va take_music
#vi du:
# take_bg= "assets/Background/Demo.png"

# take_music= "assets/audio/lop13.mp3"


#khoi tao class
dau_vao= Fighting(hero1, hero2, take_bg, take_music)

#choi game
dau_vao.play_immediately()