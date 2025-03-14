from methods import overlap
from methods import match_checks
from shapely.geometry import Point, Polygon
from methods import ball_checks2
import random

def playerInDef_ballInTransition(player_list,newBall,params):
    for player in player_list:
        if player.id == newBall.inPlayerId:
            if match_checks.check_player_in_defense_quadrant(player,params):
                if match_checks.check_ball_in_transition_quadrant(newBall,params):
                    if match_checks.check_ball_lower_than_threshold(newBall,params):

                        return True
    return False

def check_only_one_ball_in_closer_quadrants(perm_team,new_ball_list):
    if perm_team.reception_quadrant_ball==7 or perm_team.reception_quadrant_ball==10:
        if len(new_ball_list)<2:
            return True
    return False

def check_correct_ball_direction(perm_team,params):
    # 1rst DISCARD BOUNCE THAT APPEARS IN BOTH SIDES
    sides=[0,0]
    for ball in perm_team.ball_bounce_list:
        for side in range(len(sides)):
            if ball.side == side:
                sides[side]=1
    if sum(sides[:])==2:
        return True
    
    if len(perm_team.ball_bounce_list)<4:
        return True
    
    # 2nd CHECK BOUNCE SIDE
    ball1=perm_team.ball_bounce_list[0]
    ball2=perm_team.ball_bounce_list[-1]
    direction=ball2.pos.midPointX-ball1.pos.midPointX 
    # direction negative, ball moving left
    # direction positive, ball moving right
    if sides[0]==1 and direction>0:
        return False
    if sides[1]==1 and direction<0:
        return False
    return True
    
    
                    
def check_lower_ball(ball_bounce_list):
    y=0
    newKickBall=0
    for ball in ball_bounce_list:
        if ball.pos.lowerMidY>y:
            y=ball.pos.lowerMidY
            newKickBall=ball

    return newKickBall

def check_ball_overlapping(perm_team,newBall):
    for perv_ball in perm_team.prev_ball_list:
        overlaping = overlap.overlap_percentage(newBall,perv_ball)
        if overlaping > perm_team.th_overlaping:
            return True
        
def check_initiate_bounce(perm_team,new_ball_list):
    if len(new_ball_list)>0:
        perm_team.ball_bounce_init=1
    else:
        if perm_team.ball_bounce_init==1:
            perm_team.ball_noDet_counter+=1

def check_bounce_finished(perm_team):
    if perm_team.ball_noDet_counter>4:
        perm_team.ball_bounce_init=0  
        perm_team.ball_noDet_counter=0
        return True
    return False

def check_ball_half_upper_reception_quadrant(perm_team,params,ball):

    q=perm_team.reception_quadrant_ball
    if q==1: # Up Left
        x_q=params.points_image[11][0]
        if ball.pos.lowerMidX< x_q:
            return True
    elif q==4: # Up Right
        x_q=params.points_image[9][0]
        if ball.pos.lowerMidX> x_q:
            return True
    else:
        return True
    return False


def check_ball_inside_quadrant(perm_team,params,ball):
    # Check if ball is in reception quadrant
    px=ball.pos.lowerMidX
    py=ball.pos.lowerMidY
    point1=Point([px,py])
    point2= Point([ball.pos.x0,ball.pos.yEnd])
    point3= Point([ball.pos.xEnd,ball.pos.yEnd])
    points_vect=[]
    points_vect.append(point1)
    points_vect.append(point2)
    points_vect.append(point3)

    ballInsideQuadrant=False
    q=perm_team.reception_quadrant_ball
    for point in points_vect:

        if q==1: # Up Left
            if point.within(params.poly_vect[q]):
                return True
            # if ball.from_background==1 and point.within(params.poly_vect[0]): # Defense quadrant
            #     return True
        if q==4: # Up Right
            if point.within(params.poly_vect[q]):
                return True
            # if ball.from_background==1 and point.within(params.poly_vect[3]): # Defense quadrant
            #     return True
        if q==7: # Up Right
            if point.within(params.poly_vect[q]):
                return True
        if q==10: # Up Right
            if point.within(params.poly_vect[q]):
                return True
    return False


def check_ball_in_attack(perm_team,params,ball):
        # Check if ball is in reception quadrant
    px=ball.pos.lowerMidX
    py=ball.pos.lowerMidY
    point=Point([px,py])

    ballInsideQuadrant=False
    # q=perm_team.reception_quadrant_ball
    attack_q_vect=[2,8,5,11]
    for q in attack_q_vect:
        if point.within(params.poly_vect[q])==True:
            ballInsideQuadrant = point.within(params.poly_vect[q])
            return ballInsideQuadrant
    return ballInsideQuadrant

def check_ball_inPlayer(player_list,ball):
    inPlayer=False
    pxUpR=ball.pos.x0
    pyUpR=ball.pos.y0

    pxUpL=ball.pos.x0
    pyUpL=ball.pos.yEnd

    pxLowerL=ball.pos.xEnd
    pyLowerL=ball.pos.y0

    pxLowerR=ball.pos.xEnd
    pyLowerR=ball.pos.yEnd

    for player in player_list:
        x0=player.pos.x0
        y0=player.pos.y0
        xEnd=player.pos.xEnd
        yEnd=player.pos.yEnd

        # Check al 4 corners of the ball
        if is_point_in_rectangle(x0,y0,xEnd,yEnd,pxUpR,pyUpR)==True: # Up_Right
            inPlayer=True
            ball.inPlayerId=player.id
        if is_point_in_rectangle(x0,y0,xEnd,yEnd,pxUpL,pyUpL)==True: # Up_left
            inPlayer=True
            ball.inPlayerId=player.id
        if is_point_in_rectangle(x0,y0,xEnd,yEnd,pxLowerR,pyLowerR)==True: # Lower_Right
            inPlayer=True
            ball.inPlayerId=player.id
        if is_point_in_rectangle(x0,y0,xEnd,yEnd,pxLowerL,pyLowerL)==True: # Lower_left
            inPlayer=True
            ball.inPlayerId=player.id
        
        
    return inPlayer

# Function to check if a point is inside a rectangle
def is_point_in_rectangle(x1, y1, x2, y2, px, py):
    # Check if the point (px, py) lies within the rectangle's bounds
    if min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2):
        return True
    return False

def check_ball_defensive_quadrants_of_serve_side(perm_team,params,newBall):
    # Check if ball is in reception quadrant
    px=newBall.pos.lowerMidX
    py=newBall.pos.lowerMidY
    point=Point([px,py])

    ballInsideQuadrant=False

    for height in params.full_quadr_matrix[perm_team.kick_side]:
        q= height[0]
        # print("q : ", q)
        if point.within(params.poly_vect[q])==True:
            ballInsideQuadrant = True
            return ballInsideQuadrant
    return ballInsideQuadrant

def check_ball_outside_quadrants(perm_team,params,newBall):

    px=newBall.pos.lowerMidX
    py=newBall.pos.lowerMidY
    point=Point([px,py])

    ballOutsideQuadrants=True

    for side in range(len(params.full_quadr_matrix)):
        for height in range(len(params.full_quadr_matrix[side])):
            for q in params.full_quadr_matrix[side][height]:
                if point.within(params.poly_vect[q])==True:
                    ballOutsideQuadrants = False
                    return ballOutsideQuadrants 
    return ballOutsideQuadrants

def check_ball_in_forbid_triangle(perm_team,params,newBall):
    px=newBall.pos.lowerMidX
    py=newBall.pos.lowerMidY
    point=Point([px,py])

    ballInsideTriangle=False
    for poly in params.for_triangle_matrix:
        if point.within(poly)==True:
            ballInsideTriangle = True
            return ballInsideTriangle
    return ballInsideTriangle



def check_ball_quadrant(ball, params):
        ballImg=[ball.pos.lowerMidX,ball.pos.lowerMidY]
        point=Point(ballImg)
        
        points=[]
        for i in range(len(params.poly_vect)):
            a = point.within(params.poly_vect[i])
            if a:
                ball.quadrant=i

def check_any_ball_in_field(perm_team):

    if len(perm_team.ball_detected_background_list)>0:
        return True
    return False

def check_ball_side(ball,params):
    for side in range(len(params.full_quadr_matrix)):
        for height in range(len(params.full_quadr_matrix[side])):
            for quadrant in params.full_quadr_matrix[side][height]:
                if quadrant == ball.quadrant:
                    ball.side=side
                    ball.height= height

def randomise_serve_ball(perm_team,newServeBall):
    if perm_team.reception_quadrant_ball==7 or perm_team.reception_quadrant_ball==10:
        if newServeBall.RealMidPointY<3.5:
            start=0
            end=2.5
            if newServeBall.side==0:
                newServeBall.RealMidPointX = newServeBall.RealMidPointX+random.uniform(start, end)
            else:
                newServeBall.RealMidPointX = newServeBall.RealMidPointX-random.uniform(start, end)

def check_ball_in_the_upper_area(ball_list,perm_team):
    
    ball_in_top=False
    for ball in ball_list:
        if ball.type=="top":
            perm_team.ball_in_top_list.append(ball)
            ball_in_top=True
    if ball_in_top:
        perm_team.ball_top_counter+=1
    else:
        perm_team.ball_in_top_list=[]

def check_ball_in_top_of_player(ball_list,perm_team):
    for player in perm_team.player_list:
        for ball in perm_team.ball_in_top_list:
            if ball.pos.lowerMidX-10 > player.pos.x0 and ball.pos.lowerMidX < player.pos.xEnd:
                if ball.pos.lowerMidY > player.pos.y0 and ball.pos.lowerMidY < player.pos.y0+30:
                    return True
