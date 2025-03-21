import cv2
import numpy as np

def draw_ball_bounce_in_kick_start(cFrame):
    cnt=-1
    for result in cFrame.results:
        cnt+=1
        for ball in cFrame.ballBounceAfterKick_list[cnt]:
            cv2.rectangle(result.orig_img, (ball.pos.x0, ball.pos.y0), (ball.pos.xEnd, ball.pos.yEnd), (0, 255, 255), 2)

def draw_ball_bounce(perm_team,frame):
    for ball in perm_team.ball_bounce_list:
        cv2.rectangle(frame, (ball.pos.x0, ball.pos.y0), (ball.pos.xEnd, ball.pos.yEnd), (0, 255, 255), 2)

def draw_ball(cFrame):
    cnt=-1
    for result in cFrame.results:
        cnt+=1
        for ball in cFrame.ball_list[cnt]:           
            cv2.rectangle(result.orig_img, (ball.pos.x0, ball.pos.y0), (ball.pos.xEnd, ball.pos.yEnd), (0, 255, 0), 2)
        
def draw_ball_quadrant(perm_team,frame,q,params):

    if perm_team.kick_init==0:
        return
    if perm_team.reception_player_index> 4:
        return 0
    
    points=params.squares_list[q]

    pts = np.array([points[:]],
    np.int32)

    pts = pts.reshape((-1, 1, 2))
    
    isClosed = True
    color = (255, 0, 255)
    thickness = 2
    
    # Using cv2.polylines() method
    image = cv2.polylines(frame, [pts], 
            isClosed, color, thickness)
        
    player=perm_team.player_list[perm_team.reception_player_index]