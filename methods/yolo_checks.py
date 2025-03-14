from methods import match_checks
from methods import player_checks
from shapely.geometry import Point, Polygon

def chose_quadrant_players_position(player, params):
    PlayerImg=[player.pos.x0+(player.pos.xEnd-player.pos.x0)/2,player.pos.yEnd]
    point=Point(PlayerImg)
    
    points=[]
    for i in range(len(params.poly_vect)):
        a = point.within(params.poly_vect[i])
        if a:
            player.quadrant=i
            break
    
    if player.quadrant<=12:
        player_checks.check_player_side(player,params)
        match_checks.check_player_height_width(player,params)

def correct_RW_with_side(player,params):
    if player.side==0 and player.RealMidPointX>0: # player in left side
        player.RealMidPointX=-player.RealMidPointX

    if player.side==1 and player.RealMidPointX<0: # player in right side
        player.RealMidPointX=-player.RealMidPointX