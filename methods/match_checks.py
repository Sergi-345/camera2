


def check_player_change_side(perm_team):
    cnt=0
    for player in perm_team.player_list:
        if player.side_old<50:
            if player.side!=player.side_old:
                perm_team.player_missing_vector[cnt]=1
            player.side_old=player.side
        cnt+=1


def check_player_leaving_court(perm_team,params):
    cnt=0
    for player in perm_team.player_list:
        if check_player_in_attack_quadrant(player,params):
            if player.active==0:
                perm_team.player_missing_vector[cnt]=1
        cnt+=1

def check_player_in_attack_quadrant(player,params):
    for side in range(len(params.full_quadr_matrix)):
        for height in range(len(params.full_quadr_matrix[side])):
            if player.quadrant==params.full_quadr_matrix[side][height][2]:
                return True
    return False

def check_player_in_transition_quadrant(player,params):
    for height in range(len(params.quadr_matrix)):
        if player.quadrant==params.quadr_matrix[height][1]:
            return True
    return False

def check_player_in_defense_quadrant(player,params):
    for height in range(len(params.quadr_matrix)):
        if player.quadrant==params.quadr_matrix[height][0]:
            return True
    return False

def modify_player_quadrant(player,params):
    player.quadrant=params.quadr_matrix[0][0]
    if player.quadrant_old%3!=0:
        player.quadrant_old=player.quadrant

def check_ball_in_transition_quadrant(ball,params):
    for side in range(len(params.full_quadr_matrix)):
        for height in range(len(params.full_quadr_matrix[side])):
            if ball.quadrant==params.full_quadr_matrix[side][height][1]:
                return True
    return False

def check_ball_lower_than_threshold(ball,params):
    threholdY=303
    px = ball.pos.lowerMidY
    if px > threholdY:
        return True
    return False



def check_change_side(perm_team):
    if sum(perm_team.player_missing_vector[:])>=3 and perm_team.change_side==0:
        perm_team.change_side=1
        perm_team.player_missing_vector = [0,0,0,0]
        print("CHANGE SIDE ACTIVATED")

    if perm_team.kick_init==0:
        perm_team.player_missing_vector = [0,0,0,0]

    
def check_new_distribution_of_players(perm_team):

    #check al players active
    active_players=0
    if perm_team.change_side==1:
        for player in perm_team.player_list:
            if player.active==1:
                active_players+=1

    if active_players==4 and perm_team.change_side==1:
        #Check a new serve
        perm_team.player_missing_vector = [0,0,0,0]
        # repla

def check_each_player_in_different_height(perm_team):

    height_ocupied=[[0,0],[0,0]]

    for player in perm_team.player_list:
        side=player.side
        height=player.height
        height_ocupied[side][height]=1

    total_heights_occupied=0

    for side in height_ocupied:
        for height in side:
            total_heights_occupied+=height

    if total_heights_occupied==4:
        return True
    return False

def check_ball_size(perm_team):
    size_list=[]
    cnt=-1
    for ball in perm_team.ballBounceAfterKick_list:
        cnt+=1
        width = abs(ball.pos.x0-ball.pos.xEnd)
        height = abs(ball.pos.y0-ball.pos.yEnd)
        size = width*height
        if size >400:
            perm_team.ballBounceAfterKick_list.pop(cnt)

        # size_list.append(width*height)
        # print("size_list : ", size_list)



    




    
    
            