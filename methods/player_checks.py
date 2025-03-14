
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

def check_player_side(player,params):
    # Find reception side, reception height
    for side in range(len(params.full_quadr_matrix)):
        for height in range(len(params.full_quadr_matrix[side])):
            for quadrant in params.full_quadr_matrix[side][height]:
                if quadrant == player.quadrant:
                    player.side=side
                    player.height= height
    