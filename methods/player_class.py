from methods import pos_class
from shapely.geometry import Point, Polygon
import scipy.interpolate
import numpy as np

class PLAYER():
    def __init__(self,id, teamId):
        self.id=id
        self.teamId=teamId
        self.pos=pos_class.POS()
        self.new_pos=pos_class.POS()
        self.pos_old=pos_class.POS()
        self.vel_vect=[]
        self.hist=[]
        self.heatMap = np.zeros((self.nRows, self.nColumns))
        self.dist_acum_vect=[]
        self.coord_vector=[]
        self.creatHeatMap()
        self.distance_vect=[]
        self.posX_vect=[]
        self.posY_vect=[]
        self.dist_done=0


    # pos=[] # For detected players
    # new_pos=[] # For permanent players
    # old_pos=[] # For permanent players

    frame=[]
    counter_in_defense=0
    counter_in_transition=0
    counter_in_attack=0
    counter_in_net=0
    position=5
    frame2=[]
    racket_list=[]
    closest_index=0
    closest_point=[0,0]
    closest_point2=[0,0]
    Rclosest_point=[0,0]
    Rclosest_point2= [0,0]
    playerReal=[]
    playerRealY=0
    playerRealX=0
    curr_square_idx=-1
    th_opt_cost=40
    th_opt_cost_init=100
    quadrant=500
    quadrant_old=500
    quadrant_line=10   
    partner=50
    partner_index=50
    velocity=0
    side=50
    side_old=50
    height=50
    height_old=50
    width=50
    width_old=50
    

    fixed=0
    
    init_hist=0

    RealMidPointX=0
    RealMidPointY=0

    RealMidPointX_old=50
    RealMidPointY_old=50

    curr_dist = 0
    dist_acum = 0
    

    nColumns = 40    
    nRows = 20

    heatMap_columns=[]
    heatMap_rows=[]

    blocking_view_to_partner=0
    active=1
    cnt_active=0
    lowerMidX=0
    lowerMidY=0

    shoe_list=[]

    
    def findSquare(self, params):
        PlayerImg=[self.x0+(self.xEnd-self.x0)/2,self.yEnd]
        point=Point(PlayerImg)
        
        for i in range(len(params.poly_vect)):
            a = point.within(params.poly_vect[i])
            if a:
                self.curr_square_idx=i

    def creatHeatMap(self):
            # HEAD MAP

        # Define start, end, and number of points
        start = -10        # Start of the range
        end = 10         # End of the range

        # Create column vector
        self.heatMap_columns = np.linspace(start, end, self.nColumns)
        start = 0        # Start of the range
        end = 10         # End of the range

        # Create column vector
        self.heatMap_rows = np.linspace(start, end, self.nRows)