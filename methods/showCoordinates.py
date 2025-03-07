# importing the module 
import cv2 
import json
import math


class CLICK_DETECTOR():
    
    # def __init__(self,params):
    # # function to display the coordinates of 
    # # of the points clicked on the image 
    
    ui=[] 
    
    cnt_points=0
    
    cnt=0

    points_vector=[]
    points_vector_L=[]
    ball_area=[0,0,0,0]
    img=[]
    
    def load_data(self,jsonFile):

        f = open(jsonFile)
        data = json.load(f)
        self.points_vector_L=data['image pointsL']
        self.points_vector_R=data['image pointsR']
            
    
    def save_points(self,file):
            data = {}
            data['image pointsL'] = self.points_vector_L
            data['image pointsR'] = self.points_vector_R
            data['links'] = "test"
            
            with open(file, 'w') as f:
                json.dump(data, f)
                
    def draw_circles(self,side):
            font = cv2.FONT_HERSHEY_SIMPLEX 
            radius = 2
            color = (0, 0, 255) 
            thickness = 2
            if side=="L":
                for i in range(len(self.points_vector_L)):
                    cv2.putText(self.img, str(i), self.points_vector_L[i], font, 
                            0.6, (0, 0, 255), 1) 
                    # Line thickness of 2 px 
                    # Using cv2.circle() method 
                    # Draw a circle with blue line borders of thickness of 2 px 
                    self.img = cv2.circle(self.img, self.points_vector_L[i], radius, color, thickness) 
                cv2.imshow('image', self.img)

            if side=="R":
                for i in range(len(self.points_vector_R)):
                    cv2.putText(self.img, str(i), self.points_vector_R[i], font, 
                            0.6, (0, 0, 255), 1) 
                    # Line thickness of 2 px 
                    # Using cv2.circle() method 
                    # Draw a circle with blue line borders of thickness of 2 px 
                    self.img = cv2.circle(self.img, self.points_vector_R[i], radius, color, thickness) 
                cv2.imshow('image', self.img)

    def draw_circles_L(self):
            font = cv2.FONT_HERSHEY_SIMPLEX 
            radius = 2
            color = (0, 0, 255) 
            thickness = 2
            for i in range(len(self.points_vector_L)):
                cv2.putText(self.img, str(i), self.points_vector_L[i], font, 
                        0.6, (0, 0, 255), 1) 
                # Line thickness of 2 px 
                # Using cv2.circle() method 
                # Draw a circle with blue line borders of thickness of 2 px 
                self.img = cv2.circle(self.img, self.points_vector_L[i], radius, color, thickness) 
            cv2.imshow('image', self.img)

    def draw_circles_R(self):
            font = cv2.FONT_HERSHEY_SIMPLEX 
            radius = 2
            color = (0, 0, 255) 
            thickness = 2
            for i in range(len(self.points_vector_R)):
                cv2.putText(self.img, str(i), self.points_vector_R[i], font, 
                        0.6, (0, 0, 255), 1) 
                # Line thickness of 2 px 
                # Using cv2.circle() method 
                # Draw a circle with blue line borders of thickness of 2 px 
                self.img = cv2.circle(self.img, self.points_vector_R[i], radius, color, thickness) 
            cv2.imshow('image', self.img)


    def click_event_L(self,event, x, y, flags, params): 
        # checking for left mouse clicks 
        if event == cv2.EVENT_LBUTTONDOWN: 

            deleted_point=0
            deleted_index=0
            # Check if there is a zero point
            for i in range(len(self.points_vector_L)):
                p=self.points_vector_L[i]
                if p[0]==0 and p[1]==0:
                    deleted_point=1
                    deleted_index=i


            if deleted_point==0:
                
                self.cnt_points+=1
                self.cnt+=1
                # displaying the coordinates 
                # on the Shell 
                print(x, ' ', y) 
                
                p=[x,y]
                self.points_vector_L.append(p)
                

            if deleted_point==1:
                p=[x,y]
                self.points_vector_L[deleted_index]=p


            self.draw_circles_L()
    
        # checking for right mouse clicks      
        if event==cv2.EVENT_RBUTTONDOWN: 
            # print(x, ' ', y) 
            #  Plot all stored pints
            dist_vect=[]
            for i in range(len(self.points_vector_L)):
                p=self.points_vector_L[i]
                dist=math.sqrt(pow(p[0]-x,2)+pow(p[1]-y,2))
                dist_vect.append(round(dist,3))

                
            # Delete point with min distance
            min_dist= min(dist_vect)
            closest_index = dist_vect.index(min_dist)

            self.points_vector_L[closest_index]=[0,0]
            
            self.draw_circles_L()

    def click_event_R(self,event, x, y, flags, params): 

        
        # checking for left mouse clicks 
        if event == cv2.EVENT_LBUTTONDOWN: 

            deleted_point=0
            deleted_index=0
            # Check if there is a zero point
            for i in range(len(self.points_vector_R)):
                p=self.points_vector_R[i]
                if p[0]==0 and p[1]==0:
                    deleted_point=1
                    deleted_index=i


            if deleted_point==0:
                
                self.cnt_points+=1
                self.cnt+=1
                # displaying the coordinates 
                # on the Shell 
                print(x, ' ', y) 
                
                p=[x,y]
                self.points_vector_R.append(p)
                

            if deleted_point==1:
                p=[x,y]
                self.points_vector_R[deleted_index]=p


            self.draw_circles_R()
    
        # checking for right mouse clicks      
        if event==cv2.EVENT_RBUTTONDOWN: 
            # print(x, ' ', y) 
            #  Plot all stored pints
            dist_vect=[]
            for i in range(len(self.points_vector_R)):
                p=self.points_vector_R[i]
                dist=math.sqrt(pow(p[0]-x,2)+pow(p[1]-y,2))
                dist_vect.append(round(dist,3))

                
            # Delete point with min distance
            min_dist= min(dist_vect)
            closest_index = dist_vect.index(min_dist)

            self.points_vector_R[closest_index]=[0,0]
            
            self.draw_circles_R()
    
            
  
# driver function 
if __name__=="__main__": 
    cnt=0
  
    # reading the image 
    
    # displaying the image 
    img = cv2.imread('C:\\Users\\Sergi\\OneDrive\\Escritorio\\AITECH\\VideosRaw\\datasets\\pista\\frame13.jpg', 1) 
    cv2.imshow('image', img) 
    
    test=CLICK_DETECTOR()
    
    # test.img=img
  
    # setting mouse handler for the image 
    # and calling the click_event() function 
        
    cv2.setMouseCallback('image', test.click_event) 
    while True:
        img=[]
        img = cv2.imread('C:\\Users\\Sergi\\OneDrive\\Escritorio\\AITECH\\VideosRaw\\datasets\\pista\\frame13.jpg', 1) 
        
        cv2.waitKey(500) 
        
        
  
    # wait for a key to be pressed to exit 
    
    # if k == ord('q') & 0xFF :
    #     break
  
    # close the window 
    cv2.destroyAllWindows() 