from methods import yolo_data
from methods import tracking
from methods import tracking_checks
from methods import team_class
from methods import match_stats

def process(perm_team, results,params,model,cnt):

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

    tracking.ids_management(perm_team,params)

    # match_stats.check_serveTeam(perm_team,params,cnt)

    # player_stats.estimate_velocity(perm_team)
    serve.serve_detection(perm_team,params)
    # serve.serve_cancel(perm_team,params,ball_detected_list)
    # ball_stats.ball_bounce_detection(perm_team,ball_detected_list,params)
    tracking.stadistic_position_state(perm_team)

    # if cnt%30==0:
    #     player_stats.coordinates_vector(perm_team,params)

    # if cnt%30==0:
    #     player_stats.stadistic_km_done(perm_team,cnt_w3)

    # if cnt%30==0:
    #     match_checks.check_ball_size(perm_team)

    # if cnt%120==0:
        # SEND DATA TO READIS
