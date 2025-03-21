import cv2
import numpy as np
from scipy.optimize import linear_sum_assignment
from methods import serve_checks
from methods import match_checks
from methods import ball_checks

def serve_detection(perm_team,params):
    kick_position_array=[0,0,0,0]

    serve_checks.check_allow_serve(perm_team)

    ## CHECK IF SERVE DETECTED
    serve_checks.check_kick_detected(perm_team,kick_position_array)

    # NO KICK DETCETD
    if perm_team.kick_init==0:
        return
    
    ## CHECK QUADRANT CHANGE DURING KICK
    serve_checks.check_quadrant_change_during_kick(perm_team)

    # cancelar el update si ja hi ha possibles boles de saque a dins del quadrant
    if len(perm_team.ball_bounce_list)>0:
        perm_team.kick_position_count=5
        perm_team.kick_update=0

    # if perm_team.kick_update==0:
    #     serve_checks.check_disbale_update_if_serve_player_movement(perm_team)

    # print("perm_team.kick_update : ", perm_team.kick_update)
    if perm_team.kick_update==1:
        # UPDATE PLAYERS ROLES (NET, SERVE, RECEPTION)
        serve_checks.check_player_roles_in_serve(perm_team,params,kick_position_array)

    ## CHECK VELOCITIES ARE BELOW A THRESHOLD
    # serve_checks.check_player_velocities(perm_team)


def serve_cancel(perm_team,params):


    # Check ball bounce not initiated when serve
    if len(perm_team.ball_bounce_list)>0:
        if perm_team.kick_init==0:
            perm_team.kick_update=0
            perm_team.kick_position_count=0

    if perm_team.kick_init==0:
        return
    
    if len(perm_team.ball_bounce_list)>0:
        return
    # Check reception player in defense quadrant
    for player in perm_team.player_list:
        if player.id==perm_team.reception_player_id:
            if not match_checks.check_player_in_defense_quadrant(player,params):
                perm_team.ball_noDet_counter=6
            partner=player.partner
            if not match_checks.check_player_in_defense_quadrant(player,params):
                perm_team.ball_noDet_counter=6


        
    





    