from methods import player_checks
import math
import cv2
import matplotlib.pyplot as plt
import numpy as np
import copy

def estimate_velocity(perm_team):

    # Velocity of players to know when the kick ends
    vel_vect = []

    if perm_team.reception_player_index> 4:
        return 0
    
    perm_team.vel_vect=[]

    for player in perm_team.player_list:
        x1=player.pos.midPointX
        y1=player.pos.midPointY
        x0=player.pos_old.midPointX
        y0=player.pos_old.midPointY
        player.pos_old = copy.deepcopy(player.pos)
        player.velocity = round(math.sqrt(pow(x1-x0,2)+pow(y1-y0,2)),2)
        if player.pos_old.midPointX==0: # not initiated
            return 
        perm_team.vel_vect.append(player.velocity)

def stadistic_head_map(perm_team,params):

    # Find player RealWorld coordinates
    for player in perm_team.player_list:
        #Find Cell in head map
        player_checks.check_point_in_cell(player)

def coordinates_vector(perm_team,params):

    for player in perm_team.player_list:

        coord=[player.RealMidPointX,player.RealMidPointY]
        id=player.id
        i=id-1
        perm_team.coord_matrix[i].append(coord)
        if len(perm_team.coord_matrix[i])>150:
            del perm_team.coord_matrix[i][0]

        # player.coord_vector.append(coord)
        # if len(player.coord_vector)>150:
        #     del player.coord_vector[0]


def stadistic_km_done(perm_team,cnt):

    for player in perm_team.player_list:
        num=player.id-1
        if cnt%9000==0: ## Every 5 min - 9000 add a new index
            perm_team.dist_acum_matrix[num].append(perm_team.dist_acum_vect[num])

            # player.dist_acum_vect.append(player.dist_acum)
        
        if len(perm_team.dist_acum_matrix[num])==0:
            perm_team.dist_acum_matrix[num].append(perm_team.dist_acum_vect[num])

        # print("player.dist_acum_vect : ", player.dist_acum_vect)

        x1=player.RealMidPointX
        y1=player.RealMidPointY
        x0=player.RealMidPointX_old
        y0=player.RealMidPointY_old

        if player.RealMidPointX_old>10:
            player.RealMidPointX_old=x1
            player.RealMidPointY_old=y1
            return

        player.curr_dist = round(math.sqrt(pow(x1-x0,2)+pow(y1-y0,2)),2)
        perm_team.dist_acum_vect[num] += player.curr_dist

        # print("perm_team.dist_acum_matrix : ",perm_team.dist_acum_matrix)
        perm_team.dist_acum_matrix[num][-1]=round(perm_team.dist_acum_vect[num],2)

        player.RealMidPointX_old=x1
        player.RealMidPointY_old=y1

        

def plot_velocity(perm_team,cnt):
    if cnt%100==0:
        fig, ax = plt.subplots(1,1)    
        fig.suptitle('Position in court', fontsize=10)

        colorList=["red","orange","green", "yellow"]
        ax.plot(perm_team.vel_vect,color=colorList[0])
        ax.plot(perm_team.kick_vect,color="blue")

        #### CONVERT PLOT TO IMAGE
        #  
        fig.canvas.draw()
        img_plot = np.array(fig.canvas.renderer.buffer_rgba())
        plot_frame=cv2.cvtColor(img_plot, cv2.COLOR_RGBA2BGR)
        
        plot_height = 400
        plot_width = 800
        
        plot_frame = cv2.resize(plot_frame, dsize=(int(plot_width), plot_height))

        plt.clf()
        plt.close()

        cv2.imshow("vel_vector", plot_frame)

def draw_velocity(perm_team,frame):
    thickness=2
    color = (255, 0, 0) 
    font = cv2.FONT_HERSHEY_SIMPLEX            
    fontScale = 5
    for player in perm_team.player_list:
        text=str(player.velocity)
        org = [player.pos.xEnd, player.pos.y0]
        fontScale = 1
        cv2.putText(frame,text, org, font, fontScale, color, thickness, cv2.LINE_AA)

