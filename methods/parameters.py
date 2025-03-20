import cv2
import os
from shapely.geometry import Point, Polygon
import json
import matplotlib.pyplot as plt
import numpy as np


class PARAMS():
    def __init__(self):
        self.pL_real = []
        ## create self.PL_real
        for p in self.pR_real:
            new_p = p
            new_p[0]=-new_p[0]
            self.pL_real.append(new_p)

        self.p_map=[]
        self.p_map.append(self.pL_real)
        self.p_map.append(self.pR_real)

    data=[]
    calibration=0

    points_img = []

    offset=[0,0]
    
    # First Line
    p0r=[10,10]
    p1r=[7,10]
    p2r=[4,10]
    p3r=[0,10]
    # Second Line
    p4r=[10,5]
    p5r=[7,5]
    p6r=[4,5]
    p7r=[0,5]
    # Third Line
    p8r=[10,0]
    p9r=[7,0]
    p10r=[4,0]
    p11r=[0,2.5]
    
    pR_real = [p0r,p1r, p2r, p3r, p4r, p5r, p6r, p7r, p8r, p9r, p10r, p11r]
    
        
    def load_data(self,folder,MainWindow):

        # Check if video has parameters:
        jsonFile1=folder+ "/points.json"
        jsonFile2= "points.json"

        if os.path.exists(jsonFile1):
            jsonFile2=jsonFile1

        f = open(jsonFile2)
        # returns JSON object as 
        # a dictionary
        data = json.load(f)
        
        self.points_img.append(data['image pointsL'])
        self.points_img.append(data['image pointsR'])
        
        p=self.points_img

        ## APPLY OFFSET
        self.update_offset(MainWindow,p)
        
        ## COORDINATES FROM IMAGE
        self.sq_img_list=[]
        self.sq_img_list.append(self.fill_squares_list( p[0]))
        self.sq_img_list.append(self.fill_squares_list( p[1]))

        ## COORDINATES FROM REAL MAP
        self.sq_map_list=[]
        self.sq_map_list.append(self.fill_squares_list( self.p_map[0]))
        self.sq_map_list.append(self.fill_squares_list( self.p_map[1]))


        self.Up_quadr_array = [0, 1, 2]
        self.Down_quadr_array = [3, 4, 5]

        self.quadr_matrix= [self.Up_quadr_array, self.Down_quadr_array]

        # 0,3 - Defense
        # 1,4 - Transition
        # 2,5 - Attack

        # Create poly vector
        self.poly_img_list=[]
        for side in range(2):
            poly_list_side=[]
            for i in range(len(self.sq_img_list[side])):
                poly=[]
                poly = Polygon(self.sq_img_list[side][i])
                poly_list_side.append(poly)
            self.poly_img_list.append(poly_list_side)

    def update_offset(self,MainWindow,p):
        current_width = MainWindow.curr_width
        current_height = MainWindow.curr_height

        cut_width = MainWindow.params["cut_width"]
        cut_height = MainWindow.params["cut_height"]

        self.offset[0]= current_width-cut_width
        self.offset[1]= current_height-cut_height

        if self.offset[0]<0:
            self.offset[0]=0
        if self.offset[1]<0:
            self.offset[1]=0

        for side in p:
            for point in side:
                point[0]-= self.offset[0]/2
                point[1]-= self.offset[1]


    def fill_squares_list(self, p):
        # r -> squares list
        # p -> points list
        r=[]
        r.append([p[0], p[1], p[5], p[4]])# 0 - Defense
        r.append([p[1], p[2], p[6], p[5]]) # 1 - Transition
        r.append([p[2], p[3], p[7], p[6]]) # 2 - Attack

        r.append([p[4], p[5], p[9], p[8]]) # 4 - Transition
        r.append([p[5], p[6], p[10], p[9]]) # 3 - Defense
        r.append([p[6], p[7], p[11], p[10]]) # 5 - Attack

        return r


                

    def draw_detected_ball(self,ball_detected_list, frame):
        # Draw ball rectangle
        if self.drawBall==1:
            for ball in ball_detected_list:
                cv2.rectangle(frame, (ball.pos.x0, ball.pos.y0), (ball.pos.xEnd, ball.pos.yEnd), (0, 0, 255), 2)

    def draw_detected_shoes(self,detected_list, frame):
        # Draw ball rectangle
        if self.drawShoes==1:
            for object in detected_list:
                cv2.rectangle(frame, (object.pos.x0, object.pos.y0), (object.pos.xEnd, object.pos.yEnd), (255, 0, 255), 2)
        

    def draw_detections(self,team, frame):
        # Draw raquet rectangle
        if self.drawRacket==1:
            if team.racket_list:
                cnt_racket=0
                for racket in team.racket_list:
                    cnt_racket+=1
                    if racket.conf>0.5:
                        cv2.rectangle(frame, (racket.x0, racket.y0), (racket.xEnd, racket.yEnd), (255, 255, 0), 2)
                    
        # Draw ball rectangle
        if self.drawBall==1:
            cnt_ball=0
            for ball in team.ball_list:
                cnt_ball+=1
                # cv2.imwrite("dataset_items2/item_frame%d.jpg" % cnt_players, pl_frame) 
                # if ball.conf>0.5:
                cv2.rectangle(frame, (ball.pos.x0, ball.pos.y0), (ball.pos.xEnd, ball.pos.yEnd), (0, 255, 0), 2)
            
            cnt_ball_full_range=0
            for ball in team.ball_list_fullRange:
                cnt_ball_full_range+=1
                # cv2.imwrite("dataset_items2/item_frame%d.jpg" % cnt_players, pl_frame) 
                # if ball.conf>0.5:
                cv2.rectangle(frame, (ball.pos.x0, ball.pos.y0), (ball.pos.xEnd, ball.pos.yEnd), (255, 0, 0), 2)
            

            

        # Cut player frame
        if self.drawBody==1:
            cnt_players=0
            for player in team.player_list:
                cnt_players+=1
                # pl_frame=cv2.resize(player.frame,(0,0), fx=1.5, fy=1.5)
                color=[[0, 255, 0],[0, 255, 255],[255, 0, 0],[0, 0, 255]]
                # cv2.imwrite("dataset_items2/item_frame%d.jpg" % cnt_players, pl_frame) 
                # if player.id<=4
                cv2.rectangle(frame, (player.pos.x0, player.pos.y0), (player.pos.xEnd, player.pos.yEnd), color[player.id-1], 2)

                #Origin
                org=[player.pos.x0, player.pos.y0]
                # font 
                font = cv2.FONT_HERSHEY_SIMPLEX            
                # fontScale 
                fontScale = 1
                # Blue color in BGR 
                # color = (0, 0, 255) 
                # Line thickness of 2 px 
                thickness = 2
                cv2.putText(frame, str(player.id), org, font,  
                    fontScale, color[player.id-1], thickness, cv2.LINE_AA)   
                
                # Center coordinates 
                center_coordinates = player.closest_point
                # Radius of circle 
                radius = 5
                # Blue color in BGR 
                color = (255, 0, 0) 
                # Line thickness of 2 px 
                thickness = 2
                # Using cv2.circle() method 
                # Draw a circle with blue line borders of thickness of 2 px 
                image = cv2.circle(frame, center_coordinates, radius, color, thickness) 
                center_coordinates = player.closest_point2
                color = (255, 0, 255) 
                image = cv2.circle(frame, center_coordinates, radius, color, thickness) 





    
