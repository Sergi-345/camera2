from methods import player_class
from methods import ball_class
from methods import coord
from methods import ball_checks
from methods import yolo_checks
from shapely.geometry import Point, Polygon

def convertData(params,results,model,team):
    team.player_list=[]
    
    count=0
    count2=0
    count3=0

    for result in results:
        for box in result.boxes:
            if model.names[int(box.cls)] == "body" or model.names[int(box.cls)] == "player_r" or model.names[int(box.cls)] == "player_r-oEfD":
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

                yolo_checks.chose_quadrant_players_position(player, params)

                player.RealMidPointX,player.RealMidPointY= coord.findRWCoordMatrix(player.pos,params)

                yolo_checks.correct_RW_with_side(player,params)

                player.RealMidPointX = round(player.RealMidPointX,2)
                player.RealMidPointY = round(player.RealMidPointY,2)

                player.conf=round(float(box.conf[0]),2)
                player.id=count
                team.player_list.append(player)
                team.nPlayers=count


            if model.names[int(box.cls)] == "ball" or model.names[int(box.cls)] == "ball_r" or model.names[int(box.cls)] == "ball_s-d8v6":
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
                ball_checks.check_ball_side(ball, params)

                team.ball_list.append(ball)

            #     ball_checks.check_ball_quadrant(ball, params)
            #     team.ball_list_fullRange.append(ball)
                

            # if model.names[int(box.cls)] == "racket" or model.names[int(box.cls)] == "racket_r" or model.names[int(box.cls)] == "raquet_r":
            #     count2+=1
            #     racket=parameters.RACKET(count2)
            #     racket.x0=int(box.xyxy[0][0])
            #     racket.y0=int(box.xyxy[0][1])
            #     racket.xEnd=int(box.xyxy[0][2])
            #     racket.yEnd=int(box.xyxy[0][3])
            #     racket.conf=round(float(box.conf[0]),2)
            #     team.racket_list.append(racket)