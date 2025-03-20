from methods import match_checks
from shapely.geometry import Point, Polygon

def check_point_in_cell(player):

    Xpl=player.RealMidPointX
    Ypl=player.RealMidPointY

    for nx in range(len(player.heatMap_columns)-1):
        if nx<player.nColumns-1:
            x1=player.heatMap_columns[nx]
            x2=player.heatMap_columns[nx+1]

            if Xpl<x1 or Xpl>x2:
                continue

            for ny in range(len(player.heatMap_rows)-1):
                if ny<player.nRows-1:
                    y1=player.heatMap_rows[ny]
                    y2=player.heatMap_rows[ny+1]

                    if Ypl<y1 or Ypl>y2:
                        continue
                    player.heatMap[ny][nx]+=1

def check_player_quadrant(player, params):
    PlayerImg=[player.pos.x0+(player.pos.xEnd-player.pos.x0)/2,player.pos.yEnd]
    point=Point(PlayerImg)
    
    for i in range(len(params.poly_img_list[player.side])):
        a = point.within(params.poly_img_list[player.side][i])
        if a:
            player.quadrant=i
            break
    if player.quadrant<=12:
        check_player_height_width(player,params)

def check_player_height_width(player,params):
    for height in range(len(params.quadr_matrix)):
        for width in range(len(params.quadr_matrix[height])):
            if player.quadrant==width:
                player.height=height
                player.width=width
    