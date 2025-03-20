from methods import player_class
from methods import ball_class
from methods import coord
from methods import ball_checks
from methods import player_checks
from shapely.geometry import Point, Polygon

def convertData(params,results,model,team):
    team.player_list=[]
    team.ball_list=[]
    
    count=0
    count2=0
    count3=0


    cnt_side=-1
    for result in results:
        cnt_side+=1
        for box in result.boxes:
            if model.names[int(box.cls)] == "player" :
                count+=1
                player=player_class.PLAYER(count,team.id)
                player.pos.x0=int(box.xyxy[0][0])
                player.pos.y0=int(box.xyxy[0][1])
                player.pos.xEnd=int(box.xyxy[0][2])
                player.pos.yEnd=int(box.xyxy[0][3])
                player.pos.posXY=[player.pos.x0+(player.pos.xEnd-player.pos.x0)/2,player.pos.yEnd]
                player.pos.lowerMidX =player.pos.x0+(player.pos.xEnd-player.pos.x0)/2
                player.pos.lowerMidY =player.pos.yEnd
                player.pos.midPointX=player.pos.x0+(player.pos.xEnd-player.pos.x0)/2
                player.pos.midPointY=player.pos.y0+(player.pos.yEnd-player.pos.y0)/2
                player.side=cnt_side

                player_checks.check_player_quadrant(player, params)

                ## DISCARD PLAYERS OUTSIDE THE COURT
                if player.quadrant>6:
                    continue

                player.RealMidPointX,player.RealMidPointY= coord.findRWCoordMatrix(player,params)

                player.RealMidPointX = round(player.RealMidPointX,2)
                player.RealMidPointY = round(player.RealMidPointY,2)

                player.conf=round(float(box.conf[0]),2)
                player.id=count
                team.player_list.append(player)
                team.nPlayers=count


            if model.names[int(box.cls)] == "ball" :
                count3+=1
                ball=[]
                ball=ball_class.BALL(count3)
                ball.pos.x0=int(box.xyxy[0][0])
                ball.pos.y0=int(box.xyxy[0][1])
                ball.pos.xEnd=int(box.xyxy[0][2])
                ball.pos.yEnd=int(box.xyxy[0][3])
                ball.conf=round(float(box.conf[0]),2)

                ball.pos.midPoint[0]=ball.pos.x0+(ball.pos.xEnd-ball.pos.x0)/2
                ball.pos.midPoint[1]=ball.pos.y0+(ball.pos.yEnd-ball.pos.y0)/2
                ball.pos.midPointX=ball.pos.x0+(ball.pos.xEnd-ball.pos.x0)/2
                ball.pos.midPointY=ball.pos.y0+(ball.pos.yEnd-ball.pos.y0)/2

                ball.pos.lowerMidX =ball.pos.x0+(ball.pos.xEnd-ball.pos.x0)/2
                ball.pos.lowerMidY =ball.pos.yEnd

                ball_checks.check_ball_quadrant(ball, params)
                ball_checks.check_ball_height(ball, params)
                ball.side = cnt_side

                team.ball_list.append(ball)

            # if model.names[int(box.cls)] == "racket" :
            #     count2+=1
            #     racket=parameters.RACKET(count2)
            #     racket.x0=int(box.xyxy[0][0])
            #     racket.y0=int(box.xyxy[0][1])
            #     racket.xEnd=int(box.xyxy[0][2])
            #     racket.yEnd=int(box.xyxy[0][3])
            #     racket.conf=round(float(box.conf[0]),2)
            #     team.racket_list.append(racket)