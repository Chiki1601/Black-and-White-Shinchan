#black and whitre shinchan

import turtle as tu 
class sketch:
    def __init__(self, x_offset=300,y_offset=300):     
        self.x_offset = x_offset
        self.y_offset = y_offset
    def move_to(self,x ,y):
        self.pen.up()
        self.pen.goto(x, y)
        self.pen.down()

    def draw(self,retain=True):
        coordinates = [([(9, -295), (-11, -289), (-28, -276), (-48, -268), (-66, -257), (-83, -243), (-101, -248), (-123, -254), (-144, -252), (-165, -245), (-184, -235), (-201, -220), (-214, -203), (-223, -184), (-228, -162), (-227, -141), (-220, -120), (-209, -102), (-194, -85), (-182, -70), (-191, -53), (-195, -26), (-199, -9), (-188, 7), (-167, 3), (-160, -18), (-152, -22), (-148, -3), (-142, 28), (-136, 57), (-132, 74), (-130, 88), (-131, 112), (-134, 135), (-139, 158), (-141, 178), (-136, 193), (-138, 219), (-136, 244), (-149, 254), (-155, 271), (-178, 286), (-191, 300), (-174, 310), (-153, 310), (-130, 305), (-105, 299), (-91, 289), (-101, 270), (-96, 250), (-88, 232), (-70, 213), (-52, 202), (-33, 205), (-11, 206), (3, 190), (18, 202), (38, 206), (59, 206), (81, 207), (97, 218), (112, 235), (127, 252), (128, 273), (131, 296), (148, 306), (170, 308), (191, 305), (193, 288),
(177, 267), (166, 255), (157, 232), (151, 209), (145, 190), (157, 172), (159, 153), (154, 131), (153, 112), (176, 112), (196, 104), (215, 99), (233, 86), (242, 66), (244, 44), (236, 25), (232, 11), (241, -9), (244, -31), (238, -51), (223, -66), (203, -72), (181, -73), (173, -92), (171, -112), (168, -135), (163, -155), (155, -176), (145, -196), (132, -216), (120, -230), (102, -245), (85, -258), (64, -268), (44, -276), (24, -280), (9, -295)], (0.0, 0.0, 0.0)), ([(-17, -270), (-11, -252), (-14, -242), (-36, -245), (-54, -241), (-72, -230), (-60, -232), (-42, -239), (-23, -239), (-8, -229), (-3, -211), (-9, -191), (1, -202), (14, -203), (22, -220), (23, -240), (23, -256), (37, -248), (55, -237), (73, -224), (86, -215), (77, -210), (56, -208), (40, -203), (35, -186), (21, -170), (31, -172), (48, -179), (64, -176), (90, -172), (106, -167), (113, -152), (116, -132),
(115, -111), (122, -121), (121, -141), (115, -160), (119, -169), (132, -162), (131, -147), (126, -117), (121, -95), (115, -85), (114, -78), (133, -88), (153, -88), (167, -79), (170, -64), (154, -55), (138, -42), (126,
-26), (120, -9), (110, 0), (95, -12), (86, -14), (71, -13), (42, -15), (20, -17), (3, -19), (-11, -22), (-31, -26), (-51, -30), (-71, -36), (-89, -41), (-108, -47), (-124, -53), (-118, -60), (-103, -70), (-100, -88), (-110, -104), (-127, -115), (-145, -117), (-165, -114), (-179, -103), (-187, -90), (-199, -103), (-210, -120), (-217, -137), (-219, -156), (-217, -175), (-210, -193), (-199, -209), (-185, -223), (-169, -234), (-153, -241), (-135, -245), (-115, -244), (-96, -237), (-82, -233), (-67, -245), (-51, -257), (-34, -266), (-17, -270)], (1.0, 0.9803921568627451, 0.9803921568627451)), ([(-50, -208), (-66, -205), (-79, -192), (-85, -179), (-81, -163), (-70, -151), (-55, -143), (-38, -140), (-24, -142), (-10, -155), (-6, -170), (-9, -186), (-19, -199), (-33, -206), (-50, -208)], (0.0, 0.0, 0.0)), ([(-35, -180), (-31, -176), (-29, -171), (-31, -166), (-36, -162), (-41, -161), (-46, -164), (-51, -168), (-54, -174), (-52, -177), (-46, -180), (-41, -182), (-35, -180)],
(1.0, 0.9803921568627451, 0.9803921568627451)), ([(60, -153), (45, -150), (34, -141), (27, -129), (26, -113), (31, -102), (44, -89), (56, -82), (71, -80), (86, -82), (97, -89), (103, -104), (104, -119), (98, -132), (88, -143), (75, -151), (60, -153)], (0.0, 0.0, 0.0)), ([(65, -129), (71, -126), (76, -121), (79, -115), (77, -108), (72, -105), (66, -106), (59, -110), (55, -115), (55, -121), (59, -126), (65, -129)], (1.0, 0.9803921568627451, 0.9803921568627451)), ([(204, -64), (218, -60), (228, -49), (233, -37), (234, -20), (231, -7), (223, 6), (213, 17), (201, 25), (187, 30), (171, 30), (164, 27), (185, 26), (181, 22), (163, 25), (150, 25), (141, 24), (156, 34), (163, 38), (149, 43), (135, 51), (123, 58), (133, 64), (146, 72), (151, 84), (149, 99), (137,
104), (123, 98), (108, 93), (93, 88), (83, 81), (86, 66), (89, 51), (90, 37), (93, 23), (104, 14), (106, 26), (115, 12), (124, 7), (126, -9), (130, -22), (139, -35), (150, -46), (162, -54), (176, -61), (189, -64), (204, -64)], (1.0, 0.9803921568627451, 0.9803921568627451)), ([(225, -28), (225, -24), (224, -15), (224, -8), (224, -1), (225, -3), (228, -10), (230, -17), (229, -22), (225, -28)], (0.0, 0.0, 0.0)), ([(161, -25), (155, -21), (152, -15), (148, -7), (146, 2), (145, 10), (147, 16), (152, 20), (156, 15), (155, 6), (153, 2), (154, -8), (157, -16), (162, -18), (161, -25)], (0.0, 0.0, 0.0)), ([(-179, -12), (-174, -10), (-172, -6), (-173, -1),
(-177, -6), (-181, -9), (-186, -7), (-183, -3), (-183, 1), (-187, 0), (-191, -5), (-189, -9), (-185, -12), (-179, -12)], (1.0, 0.9803921568627451, 0.9803921568627451)), ([(218, 5), (215, 6), (209, 8), (205, 11), (201,
13), (198, 16), (198, 19), (202, 20), (206, 18), (208, 14), (208, 11), (213, 11), (217, 9), (218, 5)], (0.0,
0.0, 0.0)), ([(224, 28), (233, 34), (236, 47), (235, 60), (231, 72), (224, 83), (213, 91), (202, 92), (206, 82), (211, 70), (214, 56), (214, 43), (211, 42), (207, 60), (204, 74), (200, 84), (191, 93), (179, 93), (177,
85), (182, 75), (185, 62), (187, 49), (188, 36), (200, 32), (213, 31), (224, 28)], (1.0, 0.9803921568627451,
0.9803921568627451)), ([(177, 38), (181, 42), (180, 55), (178, 65), (176, 74), (172, 84), (165, 91), (158, 90), (157, 81), (151, 72), (144, 64), (137, 57), (144, 50), (146, 53), (147, 61), (152, 53), (159, 46), (169, 41), (177, 38)], (1.0, 0.9803921568627451, 0.9803921568627451)), ([(-120, 84), (-102, 94), (-79, 106), (-56, 116), (-33, 123), (-8, 128), (15, 130), (39, 128), (63, 123), (86, 117), (108, 107), (129, 107), (143, 123), (149, 147), (149, 169), (132, 183), (109, 195), (85, 198), (58, 199), (33, 198), (19, 191), (0, 168), (-16, 151), (-16, 158), (3, 176), (-13, 195), (-29, 198), (-54, 193), (-86, 186), (-113, 180), (-131, 176), (-131, 159), (-124, 130), (-122, 106), (-120, 84)], (1.0, 0.9803921568627451, 0.9803921568627451)), ([(170, 98), (181, 99), (185, 101), (180, 103), (170, 103), (159, 102), (155, 100), (159, 99), (170, 98)], (1.0, 0.9803921568627451, 0.9803921568627451)), ([(-121, 185), (-112, 186), (-95, 189), (-77, 193), (-68, 196), (-73, 203), (-87, 218), (-98, 226), (-108, 229), (-121, 229), (-129, 222), (-129, 208), (-128, 194), (-121, 185)], (1.0, 0.9803921568627451, 0.9803921568627451)), ([(132, 190), (137, 197), (142, 209), (144, 217), (136, 223), (126, 225), (118, 223), (109, 217), (101, 209), (94, 202), (103, 200), (114, 198), (123, 194), (132, 190)], (1.0, 0.9803921568627451, 0.9803921568627451)), ([(145, 226), (149, 230), (151, 239), (149, 245), (143, 248), (139, 254), (135, 251), (131, 245), (127, 240), (123, 234), (123, 230), (130, 228), (139, 227), (145, 226)], (1.0, 0.9803921568627451, 0.9803921568627451)), ([(-114, 234), (-105, 234), (-102, 239), (-105, 248), (-108, 258), (-113, 267), (-119, 272), (-124, 268), (-127, 258), (-129, 248), (-129, 239), (-124, 234), (-114, 234)], (1.0, 0.9803921568627451, 0.9803921568627451)), ([(150, 251), (154, 256), (165, 267), (177, 280), (185, 291), (186, 296), (176, 298), (157, 298), (145, 296), (138, 292), (136, 280), (138, 265), (144, 260), (150, 251)], (1.0, 0.9803921568627451, 0.9803921568627451)), ([(-136, 255), (-130, 265), (-123, 275), (-111, 276), (-103, 284), (-105, 289), (-118, 294), (-129, 296), (-142, 298), (-156, 299), (-171, 300), (-179, 299), (-177, 294), (-163, 287), (-152, 282), (-146, 274), (-144, 261), (-136, 255)], (1.0, 0.9803921568627451, 0.9803921568627451))]
        self.pen = tu.Turtle()
        self.pen.speed(0)
        for path_col in coordinates:
            #choosing color
            f = 1
            self.pen.color
            ('black')
            path = path_col[0]
            col = path_col[1]
            self.pen.color(col)
            self.pen.begin_fill()
            next = 0
            for coord in path:
                #for coord in path_col
                x,y = coord
                y *= -1
                #print(x,y)
                if f:
                    self.move_to(x, y)
                    f=0
                else:
                    self.pen.goto(x, y)

            self.pen.end_fill()
        
        if retain == True:
            tu.done()

pen= sketch()
pen.draw()
