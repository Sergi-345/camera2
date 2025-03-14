from methods import pos_class
from shapely.geometry import Point, Polygon
import scipy.interpolate
import math

class BALL():
    def __init__(self,id):
        # self.x0=x0
        # self.xEnd=xEnd
        # self.y0=y0
        # self.yEnd=yEnd
        self.id=id
        self.pos=pos_class.POS()

    frameId=0
    is_inPlayer=False
    is_overlaping=False
    pos=[]
    posX=0
    posY=0
    diameter=0
    frameList =[] # List of frames where the ball has been detected
    id=0

    quadrant_poly_vector=0
    player=0
    RealMidPoint=[0,0]
    kickplayerId=5
    last_player=0
    poly_img=[]
    poly_real=[]
    RealMidPointX=0
    RealMidPointY=0

    inPlayerId=0
    quadrant=50

    side=0

    from_background=0
    type="NON"

    def findRWCoord(self, params): # It will work for elevated camera position
        
        # Find 2 closest points where x and y are different
        # 1 - Find initial point

        pointImg=[self.pos.midPointX,self.pos.midPointY]
        img_ball=[self.pos.midPointX,self.pos.midPointY]
        x=[]
        R_x=[]
        y=[]
        R_y=[]

        # Vectors
        img_points= self.poly_img
        r_points = self.poly_real

        dist=1000000
        cnt=0
        img_LM1=[]
        r_LM1=[]
        # FIND 1RST LANDMARK: CLOSEST POINT IN IMAGE COORDINATES
        for img_LM in img_points:
            point1 = img_LM 
            point2 = img_ball 
            # Calculate the distance
            distance = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
            if distance<dist:
                dist=distance
                img_LM1=img_LM
                r_LM1 = r_points[cnt]
            cnt+=1

        print("real_LM : ", r_LM1)

        # FIND SECOND LANDMARK (LM_X): CLOSEST POINT TO LANDMARK1 IN REAL COORDINATES
        # find minimum y and diferent X
        distx=10000
        cnt=0
        r_LMX=[]
        img_LMX=[]
        for real_LM in r_points:
            if real_LM[0]!=r_LM1[0]: # diferent X
                distance_x = abs(abs(real_LM[0])-abs(r_LM1[0]))
                if distance_x<distx:
                    distx=distance_x
                    r_LMX=real_LM
                    print("r_LMX : ", r_LMX)
                    img_LMX=img_points[cnt]
            cnt+=1

        # FIND THIRD LANDMARK (LM_Y): CLOSEST POINT TO LANDMARK1 IN REAL COORDINATES
        # find minimum x and diferent y
        disty=10000
        cnt=0
        r_LMY=[]
        img_LMY=[]
        for real_LM in r_points:
            if real_LM[1]!=r_LM1[1]: # diferent Y
                distance_y = abs(abs(real_LM[1])-abs(r_LM1[1]))
                if distance_y<disty:
                    distx=distance_y
                    r_LMY=real_LM
                    img_LMY=img_points[cnt]
            cnt+=1

        x=[img_LM1[0], img_LMX[0]]
        R_x=[r_LM1[0], r_LMX[0]]

        y=[img_LM1[1], img_LMY[1]]
        R_y=[r_LM1[1], r_LMY[1]]

        y_interp = scipy.interpolate.interp1d(x, R_x, fill_value="extrapolate") 
                        
        self.RealMidPoint=[0,0]
        self.RealMidPoint[0]=round(float(y_interp(pointImg[0])),2)
        self.RealMidPointX=self.RealMidPoint[0]

        
        y_interp = scipy.interpolate.interp1d(y, R_y, fill_value="extrapolate") 
        self.RealMidPoint[1]=round(float(y_interp(pointImg[1])),2)
        self.RealMidPointY=self.RealMidPoint[1]

        # CHECK MAX AND MINS to be inside quadrant:
        maxX=0
        maxY=0
        minX=10000
        minY=10000
        for point in r_points:
            if point[0]<minX:
                minX=point[0]
            if point[0]>maxX:
                maxX=point[0]
            if point[1]<minY:
                minY=point[1]
            if point[1]>maxY:
                maxY=point[1]

        if self.RealMidPointX>maxX:
            self.RealMidPointX=maxX

        if self.RealMidPointX<minX:
            self.RealMidPointX=minX

        if self.RealMidPointY>maxY:
            self.RealMidPointY=maxY

        if self.RealMidPointY<minY:
            self.RealMidPointY=minY
