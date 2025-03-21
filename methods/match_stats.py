from methods import match_checks
from methods import match_write

def point_finish_detection(perm_team):
    
    if perm_team.kick_init==1:
        perm_team.point_playing=1


    # Check maximum of frames without detecting ball
    if perm_team.ball_bounce_init==0:
        perm_team.count_frames_no_bounce+=1

    elif perm_team.count_frames_no_bounce>0:
        if perm_team.count_frames_no_bounce>50:
            perm_team.point_playing=0
        # print(perm_team.count_frames_no_bounce)
        perm_team.count_frames_no_bounce=0

    # Check ball in ground to stop point

def check_serveTeam(perm_team,params,cnt):

    if perm_team.kick_init==1:
        #CHECK PLAYERS SIDE
        if match_checks.check_each_player_in_different_height(perm_team):
            match_write.write_players_ids(perm_team)
            # WRITE PLAYES IDs

    # player 1 and 3 are team 0
    # player 2 and 4 are team 1

    if len(perm_team.serve_team_sequence_vector)<len(perm_team.ballBounceAfterKick_list):
        # for ball in perm_team.ballBounceAfterKick_list:
        ball=perm_team.ballBounceAfterKick_list[-1]
        # serve_player_sequence_vector.append(ball.kickplayerId)
        if ball.kickplayerId==1 or ball.kickplayerId==3:
            perm_team.serve_team_sequence_vector.append(0)
        if ball.kickplayerId==2 or ball.kickplayerId==4:
            perm_team.serve_team_sequence_vector.append(1)
        if perm_team.serve_change==1:
            perm_team.serve_change=0
            # print("serve change deactivated")
            if len(perm_team.serve_team_sequence_vector)>3:
                if perm_team.serve_team_sequence_vector[-1]== perm_team.serve_team_sequence_vector[-2]:
                    # print("perm_team.serve_team_sequence_vector : ", perm_team.serve_team_sequence_vector)
                    match_write.change_players_side(perm_team)




def change_side(perm_team,det_team,params):

    ##CHECK ONE SIDE WITHOUT PLAYERS
    
    ## CHECK PLAYER CHANGING SIDE AVOBE NET
    match_checks.check_player_change_side(perm_team)

    ## CHECK PLAYER GOING OUT OF COURT
    match_checks.check_player_leaving_court(perm_team,params)

    # CHECK CHANGE SIDE HAPPENING
    match_checks.check_change_side(perm_team)


    


    