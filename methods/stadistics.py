from methods import yolo_data
from methods import tracking
from methods import tracking_checks
from methods import team_class

def process(perm_team, results,params,model):

    det_team= team_class.TEAM(1)
    yolo_data.convertData(params,results,model,det_team)

    # perm_team.player_list = det_team.player_list
    perm_team.ball_list = det_team.ball_list
    perm_team.racket_list = det_team.racket_list
    
    # if not tracking_checks.check_minimum_detected_players(det_team,perm_team):
    #     return

    if not tracking.start_tracking(perm_team, det_team, params):
        return
    
    # ASSIGN PLAYERS
    tracking.tracking_management(params,det_team,perm_team,det_team.frame)

