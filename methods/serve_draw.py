import cv2
import numpy as np

def draw_reception_quadrant_and_player(cFrame,params,side):

    cnt=-1
    for result in cFrame.results:
        cnt+=1

        if cFrame.kick_side_list[cnt]==side: # WE NEED TO BE IN THE RESEPTION QUADRANT
            return
        
        kick_init=cFrame.kick_init_list[cnt]
        reception_player_index=cFrame.reception_player_index_list[cnt]
        reception_quadrant_ball=cFrame.reception_quadrant_ball_list[cnt]
        player_list = cFrame.player_list[cnt]
        player_id = cFrame.reception_player_id_list[cnt]

        if kick_init==0:
            return
        if reception_player_index> 4:
            return 0
        
        points=params.sq_img_list[side][reception_quadrant_ball]
        pts = np.array([points[:]],np.int32)
        pts = pts.reshape((-1, 1, 2))
        
        result.orig_img = cv2.polylines(result.orig_img, [pts], True, (255, 255, 0), 2)
        
        player=[]
        for player_obj in player_list:
            if player_obj.id==player_id:
                player=player_obj
        if player!=[]:
            cv2.rectangle(result.orig_img, (player.pos.x0, player.pos.y0), (player.pos.xEnd, player.pos.yEnd), (255, 0, 255), 2)

def draw_kick_start(cFrame):

    thickness=2
    color = (255, 255, 0) 
    font = cv2.FONT_HERSHEY_SIMPLEX            
    fontScale = 1

    org = [480, 143]
    if perm_team.kick_init==1 and perm_team.curr_player_kick_index<5:

        text=perm_team.curr_player_kick_id
        for player in perm_team.player_list:
            if player.id==perm_team.curr_player_kick_id:
                org1 = [player.pos.x0, player.pos.y0]
                # fontScale = 1
                cv2.putText(frame,str(text), org1, font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.rectangle(frame, (player.pos.x0, player.pos.y0), (player.pos.xEnd, player.pos.yEnd), color, 2)

                cv2.putText(frame,"SERVE", org, font, fontScale, color, thickness, cv2.LINE_AA)

    for ball in ball_detected_list:
        if ball.type=="cancel":
            cv2.putText(frame,"SERVE", org, font, fontScale, (0,0,255), thickness, cv2.LINE_AA)