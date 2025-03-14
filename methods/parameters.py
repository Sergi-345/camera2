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

    data=[]
    calibration=0

    perm_teamL=[]
    perm_teamR=[]
    mid_point=[]
    
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

    Rpoints_vect = []
    
    pR_real = [p0r,p1r, p2r, p3r, p4r, p5r, p6r, p7r, p8r, p9r, p10r]
    
    
    poly_vect=[]
    squares_list=[]

    UpLeft_quadr_array = [0, 1, 2]
    DownLeft_quadr_array = [6, 7, 8]
    UpRight_quadr_array = [3, 4, 5]
    DownRight_quadr_array = [9, 10, 11]

    Left_quadr_matrix= []
    Right_quadr_matrix= []

    full_quadr_matrix=[]


    q1Img=[]
    q4Img=[]
    q7Img=[]
    q10Img=[]

        
    def load_data(self,folder):
        # Check if video has parameters:

        jsonFile1=folder+ "/points.json"
        jsonFile2= "points.json"

        jsonFile=""
        if os.path.exists(jsonFile1):
            jsonFile2=jsonFile1

        f = open(jsonFile2)
        # returns JSON object as 
        # a dictionary
        data = json.load(f)
        
        self.points_imageL=data['image pointsL']
        self.points_imageR=data['image pointsR']
        
        pL=self.points_imageL
        pR=self.points_imageR

        ## APPLY OFFSET
        # for point in p:
        #     point[1]+=200

        self.sq_list_L=[]
        self.sq_list_R=[]

        self.fill_squares_list(self.sq_list_L, pL)
        self.fill_squares_list(self.sq_list_R, pR)

        self.sq_real_list_L=[]
        self.sq_real_list_R=[]

        self.fill_squares_list(self.sq_real_list_L, self.pR_real)
        self.fill_squares_list(self.sq_real_list_R, self.pL_real)

        
        for n in range(len(self.sq_real_list_L)):
            self.squares_list.append(self.sq_list_L[n])
            self.Rpoints_vect.append(self.sq_real_list_L[n])

        for n in range(len(self.sq_real_list_R)):
            self.squares_list.append(self.sq_list_R[n])
            self.Rpoints_vect.append(self.sq_real_list_R[n])


        self.UpLeft_quadr_array = [0, 1, 2]
        self.DownLeft_quadr_array = [6, 7, 8]
        self.UpRight_quadr_array = [3, 4, 5]
        self.DownRight_quadr_array = [9, 10, 11]

        self.Left_quadr_matrix= [self.UpLeft_quadr_array, self.DownLeft_quadr_array]
        self.Right_quadr_matrix= [self.UpRight_quadr_array, self.DownRight_quadr_array]

        self.full_quadr_matrix = [self.Left_quadr_matrix, self.Right_quadr_matrix]

        # 0,3,6,9 - Defense
        # 1,4,7,10 - Transition
        # 2,5,8,11 - Attack

        # Create poly vector

        self.poly_vect=[]
        
        for i in range(len(self.squares_list)):
            poly=[]
            poly = Polygon(self.squares_list[i])
            self.poly_vect.append(poly)

    def fill_squares_list(self,r, p):
        # r -> squares Lis
        # p -> points list 
        r.append([p[0], p[1], p[5], p[4]])# 0 - Defense
        r.append([p[1], p[2], p[6], p[5]]) # 1 - Transition
        r.append([p[2], p[3], p[7], p[6]]) # 2 - Attack

        r.append([p[5], p[6], p[10], p[9]]) # 3 - Defense
        r.append([p[4], p[5], p[8], p[9]]) # 4 - Transition
        r.append([p[6], p[7], p[10]]) # 5 - Attack

    def draw_players_position(self, team,frame):
        for player in team.player_list:
            PlayerImg=[player.pos.x0+(player.pos.xEnd-player.pos.x0)/2,player.pos.yEnd]
            point=Point(PlayerImg)
            
            points=[]
            for i in range(len(self.poly_vect)):
                a = point.within(self.poly_vect[i])
                if a:
                    points=self.squares_list[i]
                    break
                
            if points:
                pts = np.array([points[0], points[1], 
                    points[2], points[3]],
                np.int32)

                pts = np.array([points[:]],
                np.int32)
    
                pts = pts.reshape((-1, 1, 2))
                
                isClosed = True
                
                # Blue color in BGR
                color = (255, 0, 0)
                
                # Line thickness of 2 px
                thickness = 2
                
                # Using cv2.polylines() method
                # Draw a Blue polygon with 
                # thickness of 1 px
                
                image = cv2.polylines(frame, [pts], 
                        isClosed, color, thickness)
                

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





    
