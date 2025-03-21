from methods import match_checks


def check_allow_serve(perm_team):
    
    if perm_team.new_serve_allowed==0:
        for player in perm_team.player_list:
            if player.height!=player.height_old:
                # print("new serve allowed!")
                # print("id : ", player.id, ", height : ",player.height)
                # print("id : ", player.id, ", height_old : ",player.height_old)
                perm_team.new_serve_allowed=1
    if perm_team.new_serve_allowed==0:
        perm_team.kick_init=0
        perm_team.kick_position_count=0
    

def check_kick_detected(perm_team,kick_position_array):
    #Check how many player are in the defense quadrant
    cnt_player=0
    for perm_player in perm_team.player_list:
        if perm_player.quadrant%3==0:
            kick_position_array[cnt_player]=1
        cnt_player+=1

    # print("kick_position_array : ", kick_position_array)
    if sum(kick_position_array)==3:
        perm_team.kick_position_count+=1
        # print("perm_team.kick_position_count : ", perm_team.kick_position_count)
    else:
        perm_team.kick_position_count=0

    # Initiate kick start
    if perm_team.kick_position_count>8 and perm_team.initial_id==1 :
        perm_team.kick_init=1
        perm_team.kick_update=1
        perm_team.quadrant_change_during_ball_bounce=0
        # print("new serve detected!")

def check_quadrant_change_during_kick(perm_team):
    for player in perm_team.player_list:
        if player.quadrant != player.quadrant_old:
            # if player.id==perm_team.curr_player_kick_id:
            perm_team.kick_position_count=5
            perm_team.kick_update=0
            perm_team.quadrant_change_during_ball_bounce=1

def check_disbale_update_if_serve_player_movement(perm_team):
    for player in perm_team.player_list:
        if player.id==perm_team.curr_player_kick_id:
            if player.dist_done >10:
                print("player.id : ",player.id, ", dist : ",player.dist_done)
                perm_team.kick_position_count=5
                perm_team.kick_update=0


def check_player_velocities(perm_team):
    for player in perm_team.player_list:
        if player.velocity>4:
            # perm_team.kick_position_count-=1
            perm_team.kick_position_count=0
            perm_team.kick_update=0
        # else:
            # perm_team.kick_update=1

def check_player_roles_in_serve(perm_team,params,kick_position_array):

    # Check which player is going to the net
    for i in range(len(kick_position_array)):
        if kick_position_array[i]==0:
            perm_team.net_player_id=perm_team.player_list[i].id
            perm_team.kick_side = perm_team.player_list[i].side
            perm_team.reception_side =  (perm_team.kick_side + 1) % 2 

    # Find player that is making the kick
    perm_team.curr_player_kick_id=perm_team.partners_vector[perm_team.net_player_id-1]
    cnt=0
    for player in perm_team.player_list:
        if player.id == perm_team.curr_player_kick_id:
            perm_team.curr_player_kick_index = cnt
        cnt+=1

    # Find reception height
    for height in range(len(params.quadr_matrix)):
        for quadrant in params.quadr_matrix[height]:
            if quadrant == perm_team.player_list[perm_team.curr_player_kick_index].quadrant:

                perm_team.kick_height=height
                perm_team.reception_height =  (height + 1) % 2 

    # Find reception quadrant
    perm_team.reception_quadrant_player = params.quadr_matrix[perm_team.reception_height][0] # Defense quadrant
    perm_team.reception_quadrant_ball = params.quadr_matrix[perm_team.reception_height][1] # Transition quadrant

    # Find reception player
    cnt=0
    for player in perm_team.player_list:
        if player.quadrant==perm_team.reception_quadrant_player:
            perm_team.reception_player_id = player.id
            perm_team.reception_player_index = cnt
        cnt+=1
