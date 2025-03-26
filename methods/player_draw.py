import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import cv2

def draw_players_quadrant(cFrame_list,params):
    cnt=-1
    for cFrame in cFrame_list:
        cnt+=1
        
        for player in cFrame.player_list:
            if player.quadrant>6:
                continue
            points = params.sq_img_list[player.side][player.quadrant]
            if points:
                pts = np.array([points[:]],np.int32)
                pts = pts.reshape((-1, 1, 2))
                cFrame.frame = cv2.polylines(cFrame.frame,[pts],True,(255, 0, 0), 2)
                
def draw_player(cFrame_list):
    cnt=-1
    for cFrame in cFrame_list:
        cnt+=1
        for player in cFrame.player_list:
            # print("player.id : ", player.id)
            color=[[0, 255, 0],[0, 255, 255],[255, 0, 0],[0, 0, 255]]
            if player.id>4:
                continue
            cv2.rectangle(cFrame.frame, (player.pos.x0, player.pos.y0), (player.pos.xEnd, player.pos.yEnd), color[player.id-1], 2)
            #Origin
            org=[player.pos.x0, player.pos.y0]
            cv2.putText(cFrame.frame, str(player.id), org, cv2.FONT_HERSHEY_SIMPLEX , 1, color[player.id-1], 2, cv2.LINE_AA)   
        
        # # Center coordinates 
        # center_coordinates = player.closest_point
        # radius = 5
        # thickness = 2
        # image = cv2.circle(frame, center_coordinates, radius, (255, 0, 0) , thickness) 
        # center_coordinates = player.closest_point2
        # image = cv2.circle(frame, center_coordinates, radius, (255, 0, 255), thickness) 

def plot_headMap(perm_team):
    # Generate sample data for the heat map

    # Create the heat map
    fig =plt.figure()       # Set the figure size
    fig.patch.set_facecolor('lightgray')  # Set figure background

    for player in perm_team.player_list:
        if player.id==3:
            sns.heatmap(player.heatMap, annot=False, cmap="viridis")  # Use a color map, with annotations
        # if player.id==1:
        #     sns.heatmap(player.heatMap, annot=False, cmap="viridis")  # Use a color map, with annotations
    # Display the heat map
    plt.title("Sample Heat Map")


    #### CONVERT PLOT TO IMAGE
    fig.canvas.draw()
    img_plot = np.array(fig.canvas.renderer.buffer_rgba())
    plot_frame=cv2.cvtColor(img_plot, cv2.COLOR_RGBA2BGR)
    
    plot_height = 200
    plot_width = 400
    
    plot_frame = cv2.resize(plot_frame, dsize=(int(plot_width), plot_height))

    # plt.show(block=False)

    plt.clf()
    plt.close()

    cv2.imshow("realWorldCoordinates", plot_frame)

