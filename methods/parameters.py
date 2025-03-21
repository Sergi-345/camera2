import cv2
import os
from shapely.geometry import Point, Polygon
import json
import matplotlib.pyplot as plt
import numpy as np
import copy


class PARAMS():
    def __init__(self):
        self.pL_real = []
        ## create self.PL_real
        for p in self.pR_real:
            new_p = copy.deepcopy(p)
            new_p[0]=-new_p[0]
            self.pL_real.append(new_p)

        self.p_map=[]
        self.p_map.append(self.pL_real)
        self.p_map.append(self.pR_real)
        print("self.p_map : ", self.p_map)

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

    
