from methods import tracking_checks
from methods import player_checks
from methods import match_checks

import cv2
import numpy as np
import math
import copy




def tracking_management(params,det_team,perm_team,frame):

    if len(det_team.player_list)==0:
        return

    perm_list_left=[]
    perm_list_right=[]
    det_list_left=[]
    det_list_right=[]

    perm_list_missing_left=[]
    perm_list_missing_right=[]

    # side : 0 = LEFT //// side : 1 = RIGHT
    tracking_checks.make_side_players_lists(perm_list_left,det_list_left,params,perm_team,det_team,0,perm_list_missing_left)
    tracking_checks.make_side_players_lists(perm_list_right,det_list_right,params,perm_team,det_team,1,perm_list_missing_right)

    # 1 PLAYER OR MORE IN LEFT SIDE
    if len(det_list_left)>=1 and len(perm_list_left)>=1:
        tracking_checks.check_players_hungarian(perm_list_left, det_list_left,perm_team.match_line3,perm_team.match_line4)

    # 1 PLAYER OR MORE IN RIGHT SIDE
    if len(det_list_right)>=1 and len(perm_list_right)>=1:
        tracking_checks.check_players_hungarian(perm_list_right, det_list_right,perm_team.match_line1,perm_team.match_line2)

    # 1 PLAYER MISSING
    tracking_checks.check_one_player_missing_and_change_quadrant(perm_list_left, det_list_left,params,perm_list_missing_left,0)
    tracking_checks.check_one_player_missing_and_change_quadrant(perm_list_right, det_list_right,params,perm_list_missing_right,1)




def start_tracking(perm_team, det_team, params):

    # Initial detection
    left_list=0
    right_list=0
    if perm_team.init==0:
        if len(det_team.player_list)==4:
            print("AAA")

    return True

def ids_management(perm_team,params):

    # ONLY HAPPENS ONCE AT THE BEGINNING
    tracking_checks.check_initial_id(perm_team,params)
    # HAPPENS AFTER A CHANGE OF SIDE
    # tracking_checks.check_new_id_after_side_change(perm_team,params)
    # HAPPENS DURING THE GAME TO SEE IF SOME TEAM CHANGES PLAYER POSITIONS
    # tracking_checks.check_update_ids(perm_team,params)



# def detect_position_state(perm_team):
def stadistic_position_state(perm_team):

    for player in perm_team.player_list:

        j=player.id-1
        i = player.quadrant
        if i ==0 or i == 3 or i==6 or i==9:
            perm_team.counter_in_defense[j]+=1
        if i ==1 or i == 4 or i==7 or i==10:
            perm_team.counter_in_transition[j]+=1
        if i ==2 or i == 5 or i==8 or i==11:
            perm_team.counter_in_attack[j]+=1

        # 0,3,6,9 - Defense
        # 1,4,7,10 - Transition
        # 2,5,8,11 - Attack



