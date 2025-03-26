from methods import player_class
from methods import ball_class
from methods import racket_class
from methods import coord
from methods import ball_checks
from methods import player_checks
from shapely.geometry import Point, Polygon
import math

def convertData(params,result,model,team,side):
    team.player_list=[]
    team.ball_list=[]
    team.racket_list=[]
    
    count_p=0
    count_r=0
    count_b=0

    if result:
        for box in result.boxes:
            if math.isnan(box.xyxy[0][0]):
                continue
            if math.isnan(box.xyxy[0][1]):
                continue
            if math.isnan(box.xyxy[0][2]):
                continue
            if math.isnan(box.xyxy[0][3]):
                continue
            if model.names[int(box.cls)] == "player" :
                count_p+=1
                player=player_class.PLAYER(count_p,side)
                player.pos.x0=int(box.xyxy[0][0])
                player.pos.y0=int(box.xyxy[0][1])
                player.pos.xEnd=int(box.xyxy[0][2])
                player.pos.yEnd=int(box.xyxy[0][3])
                player.pos.posXY=[player.pos.x0+(player.pos.xEnd-player.pos.x0)/2,player.pos.yEnd]
                player.pos.lowerMidX =player.pos.x0+(player.pos.xEnd-player.pos.x0)/2
                player.pos.lowerMidY =player.pos.yEnd
                player.pos.midPointX=player.pos.x0+(player.pos.xEnd-player.pos.x0)/2
                player.pos.midPointY=player.pos.y0+(player.pos.yEnd-player.pos.y0)/2
                player.side=side

                player_checks.check_player_quadrant(player, params)

                ## DISCARD PLAYERS OUTSIDE THE COURT
                if player.quadrant>6:
                    continue

                player.RealMidPointX,player.RealMidPointY= coord.findRWCoordMatrix(player,params)

                player.RealMidPointX = round(player.RealMidPointX,2)
                player.RealMidPointY = round(player.RealMidPointY,2)

                player.conf=round(float(box.conf[0]),2)
                player.id=count_p
                team.player_list.append(player)
                team.nPlayers=count_p


            if model.names[int(box.cls)] == "ball" :
                if math.isnan(box.xyxy[0][0]):
                    continue
                if math.isnan(box.xyxy[0][1]):
                    continue
                count_b+=1
                ball=[]
                ball=ball_class.BALL(count_b)
                ball.pos.x0=int(box.xyxy[0][0])
                ball.pos.y0=int(box.xyxy[0][1])
                ball.pos.xEnd=int(box.xyxy[0][2])
                ball.pos.yEnd=int(box.xyxy[0][3])
                ball.conf=round(float(box.conf[0]),2)
                ball.pos.midPointX=ball.pos.x0+(ball.pos.xEnd-ball.pos.x0)/2
                ball.pos.midPointY=ball.pos.y0+(ball.pos.yEnd-ball.pos.y0)/2

                ball.pos.lowerMidX =ball.pos.x0+(ball.pos.xEnd-ball.pos.x0)/2
                ball.pos.lowerMidY =ball.pos.yEnd

                ball_checks.check_ball_quadrant(ball, params)
                ball_checks.check_ball_height(ball, params)
                ball.side = side

                team.ball_list.append(ball)

            if model.names[int(box.cls)] == "racket" :
                count_r+=1
                racket=[]
                racket=racket_class.RACKET(count_r)
                racket.pos.x0=int(box.xyxy[0][0])
                racket.pos.y0=int(box.xyxy[0][1])
                racket.pos.xEnd=int(box.xyxy[0][2])
                racket.pos.yEnd=int(box.xyxy[0][3])
                racket.conf=round(float(box.conf[0]),2)
                racket.pos.midPointX=racket.pos.x0+(racket.pos.xEnd-racket.pos.x0)/2
                racket.pos.midPointY=racket.pos.y0+(racket.pos.yEnd-racket.pos.y0)/2
                racket.side = side
                team.racket_list.append(racket)