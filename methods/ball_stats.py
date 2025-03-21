import cv2
import numpy as np
import copy
from methods import ball_checks
from methods import coord

def ball_bounce_detection(perm_team,params):

    det_ball_list=perm_team.ball_list
    new_prev_ball_list=[]
    new_ball_list=[]

    for newBall in det_ball_list:
        ## CHECK BALL IN PLAYER
        if ball_checks.check_ball_inPlayer(perm_team.player_list,newBall): #Check ball not inside player
            continue
        new_prev_ball_list.append(newBall)        
        ## CHECK BALL OVELAPING
        if ball_checks.check_ball_overlapping(perm_team,newBall):
            continue
        ## CHECK BALL IS IN THE ATTACK QUADRANT
        if ball_checks.check_ball_in_attack(perm_team,params,newBall):
            continue
        ## CHECK BALL IS IN THE DEFENSIVE QUADRANTS OF THE SERVING SIDE
        if ball_checks.check_ball_defensive_quadrants_of_serve_side(perm_team,params,newBall):
            continue
        ## DISCARD BALLS OUTSIDE THE QUADRANTS
        if ball_checks.check_ball_outside_quadrants(perm_team,params,newBall):
            continue
        
        ## ADD BALL TO LISTS
        new_ball_list.append(newBall)
        perm_team.ball_bounce_list.append(newBall)

    # RESET STATES
    perm_team.prev_ball_list=new_prev_ball_list

    # INITIATE BOUNCE
    ball_checks.check_initiate_bounce(perm_team,new_ball_list)

    # BALL BOUNCE FINISHED
    if ball_checks.check_bounce_finished(perm_team):

        ## CHECK IF SERVE IS INITATED
        if perm_team.kick_init==0:
            perm_team.ball_bounce_list=[]
            perm_team.kick_init=0
            perm_team.kick_update=0
            perm_team.kick_position_count=0
            return
        
        # CHECK BALL DIRECTION AND DISCARD IF NOT CORRECT DIRECTION
        if not ball_checks.check_correct_ball_direction(perm_team,params):
            perm_team.ball_bounce_list=[]
            perm_team.kick_init=0
            perm_team.kick_update=0
            perm_team.kick_position_count=5
            return
            
        # CHECK IF BALL IN CLOSEST QUADRANTS THEN MORE THAN ONE BALL DETECTED
        if ball_checks.check_only_one_ball_in_closer_quadrants(perm_team,perm_team.ball_bounce_list):
            perm_team.ball_bounce_list=[]
            return

        ## CHECK IF ANY BALL OF THE BOUNCE IS INSIDE QUADRANT. IN FIRST BOUNCE AFTER SERVE
        ballInsideQuadrant = False
        for ball in perm_team.ball_bounce_list:
             if ball_checks.check_ball_inside_quadrant(perm_team,params,ball):
                ballInsideQuadrant = True

        ## CHECK WHICH IS THE LOWER BALL
        if ballInsideQuadrant:
            newServeBall = ball_checks.check_lower_ball(perm_team.ball_bounce_list)
            if newServeBall!=0:
                ## CHECK IF THE LOWER BALL IS INSIDE THE RECEPTION QUADRANT
                if ball_checks.check_ball_inside_quadrant(perm_team,params,newServeBall):
                    newServeBall.kickplayerId=perm_team.curr_player_kick_id
                    newServeBall.RealMidPointX,newServeBall.RealMidPointY= coord.findRWCoordMatrix(newServeBall,params)

                    perm_team.ballBounceAfterKick_list.append(newServeBall)
                    # if perm_team.quadrant_change_during_ball_bounce==0:
                    #     perm_team.new_serve_allowed=0 

        # FINISH KICK START
        perm_team.ball_bounce_list=[]
        perm_team.kick_init=0
        perm_team.kick_update=0
        perm_team.kick_position_count=0
        