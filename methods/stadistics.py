from methods import yolo_data
from methods import tracking
from methods import tracking_checks
from methods import team_class
from methods import match_stats
from methods import serve
from methods import ball_stats
from methods import player_stats
from methods import match_checks

def process(perm_team, cFrame_list2,params,cnt):

    det_player_list=[]
    perm_team.ball_list=[]
    perm_team.racket_list=[]


    for i in range(len(cFrame_list2)):
            for player in cFrame_list2[i].player_list:
                det_player_list.append(player) 
            for ball in cFrame_list2[i].ball_list:
                perm_team.ball_list.append(ball)
            for racket in cFrame_list2[i].racket_list:
                perm_team.racket_list.append(racket)
            
                
    # if not tracking_checks.check_minimum_detected_players(det_team,perm_team):
    #     return

    if not tracking.start_tracking(perm_team, det_player_list, params):
        return
    
    # ASSIGN PLAYERS
    tracking.tracking_management(params,det_player_list,perm_team)
    tracking.ids_management(perm_team,params)

    # match_stats.check_serveTeam(perm_team,params,cnt)

    # SERVE MANAGEMENT
    serve.serve_detection(perm_team,params)
    serve.serve_cancel(perm_team,params)
    ball_stats.ball_bounce_detection(perm_team,params)
    tracking.stadistic_position_state(perm_team)

    if cnt%30==0:
        player_stats.coordinates_vector(perm_team,params)

    if cnt%30==0:
        player_stats.stadistic_km_done(perm_team,cnt)

    if cnt%30==0:
        match_checks.check_ball_size(perm_team)
