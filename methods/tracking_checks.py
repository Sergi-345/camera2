from methods import match_checks
from methods import player_checks
import cv2
from scipy.optimize import linear_sum_assignment
import math
import numpy as np
import copy
import time
import random


def check_players_hungarian(perm_list, det_list,match_line1,match_line2):
        # CREATE COST MATRIX
        shape=[len(det_list),len(perm_list)]
        cost_matrix=[]
        if shape==[2,2]:
            cost_matrix = np.empty([])
            cost_matrix=create_cost_matrix(perm_list,det_list,cost_matrix)

            fill_cost_matrix(perm_list,det_list,cost_matrix)

            # APPLY HUNGARIAN ASSIGNMENT
            [detected_player_ind , perm_player_ind, opt_cost]=hungarian_assignment(cost_matrix)

            # FILL COST MATRIX FOR HUNGARIAN ASSIGNMENT
            player1=perm_list[perm_player_ind[0]]
            player2=det_list[detected_player_ind[0]]
            # match_line1[0]=player1.pos.posXY
            # match_line1[1]=player2.pos.posXY
            player3=perm_list[perm_player_ind[1]]
            player4=det_list[detected_player_ind[1]]
            # match_line2[0]=player3.pos.posXY
            # match_line2[1]=player4.pos.posXY

        elif shape==[1,2]:
            # return
            detected_player_ind=0
            perm_player_ind=0
            det_player=det_list[0]
            distance=10000
            cnt=-1
            # match_line1=[]
            # match_line1[1]=[ det_player.pos.lowerMidX, det_player.pos.lowerMidY]
            for perm_player in perm_list:
                cnt+=1
                dist=math.sqrt(pow(det_player.pos.lowerMidX-perm_player.pos.lowerMidX,2)+pow(det_player.pos.lowerMidY-perm_player.pos.lowerMidY,2))
                # dist=math.sqrt(pow(det_player.RealMidPointX-perm_player.RealMidPointX,2)+pow(det_player.RealMidPointY-perm_player.RealMidPointY,2))
                if dist<distance:
                    distance=dist
                    # match_line1[0]=[ perm_player.pos.lowerMidX, perm_player.pos.lowerMidY]
                    opt_cost=round(dist,2)
                    perm_player_ind=cnt



        elif shape==[2,1]:
            perm_player_ind=0
            detected_player_ind=0
            perm_player=perm_list[0]
            # match_line1[1]=[perm_player.pos.lowerMidX,perm_player.pos.lowerMidY]
            distance=10000
            cnt=-1
            for det_player in det_list:
                cnt+=1
                dist=math.sqrt(pow(det_player.pos.lowerMidX-perm_player.pos.lowerMidX,2)+pow(det_player.pos.lowerMidY-perm_player.pos.lowerMidY,2))
                # dist=math.sqrt(pow(det_player.RealMidPointX-perm_player.RealMidPointX,2)+pow(det_player.RealMidPointY-perm_player.RealMidPointY,2))
                if dist<distance:
                    distance=dist
                    # match_line1[0]=[det_player.pos.lowerMidX,det_player.pos.lowerMidY]
                    opt_cost=round(dist,2)
                    detected_player_ind=cnt


        elif shape==[1,1]:
            perm_player_ind=0
            detected_player_ind=0
            opt_cost=0
            perm_player=perm_list[0]
            det_player=det_list[0]
            dist=math.sqrt(pow(det_player.pos.lowerMidX-perm_player.pos.lowerMidX,2)+pow(det_player.pos.lowerMidY-perm_player.pos.lowerMidY,2))
            if dist>15:
                return

        else:
            return

        # STORE NEW POSITION IN PERM PLAYERS
        store_new_perm_players_position(perm_player_ind,detected_player_ind,perm_list,opt_cost,det_list)

def check_one_player_missing_and_change_quadrant(perm_list, det_list,params,perm_list_missing, side):

    if len(perm_list_missing)==1 and len(perm_list)==1 and len(det_list): 
        det_player=det_list[0]
        perm_player=perm_list[0]
        perm_player_missing=perm_list_missing[0]
        if match_checks.check_player_in_transition_quadrant(det_player,params):
            perm_trans = match_checks.check_player_in_transition_quadrant(perm_player,params)
            perm_defense = match_checks.check_player_in_defense_quadrant(perm_player,params)
            if perm_trans or perm_defense:
                match_checks.modify_player_quadrant(perm_player_missing,params)
                perm_player_missing.RealMidPointY=5.6+random.uniform(-0.4, 0.4)
                if side==0:
                    perm_player_missing.RealMidPointX=-8.2+random.uniform(-0.3, 0.3)
                if side==1:
                    perm_player_missing.RealMidPointX=8.2+random.uniform(-0.3, 0.3)

def make_side_players_lists(perm_list,det_list,params,perm_team,det_player_list,side,perm_list_missing):
    for det_player in det_player_list:
        if det_player.side==side:
            det_list.append(det_player)

    perm_list_all=[]
    for perm_player in perm_team.player_list:
        if perm_player.side==side:
            perm_list_all.append(perm_player)
            if perm_player.active==1:
                perm_list.append(perm_player)
            else:
                perm_list_missing.append(perm_player)

    #Activate player that is not active, for next iteration
    for perm_player in perm_list_all:
        if len(det_list)==2 and perm_player.active==0:
            perm_player.active=1


# Función para calcular el histograma de una imagen
def calcular_histograma(imagen_rgb):
    # Convertir la imagen de BGR a RGB (si es necesario)
    # imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

    # print("imagen_rgb : ", imagen_rgb)
    # print(type(imagen_rgb))  # Should be <class 'numpy.ndarray'>
    # print(imagen_rgb.dtype) 
    
    # Calcular el histograma para los tres canales de color (R, G, B)
    histograma = []
    for i in range(3):  # Canales: 0 = Red, 1 = Green, 2 = Blue
        hist = cv2.calcHist([imagen_rgb], [i], None, [256], [0, 256])
        histograma.append(hist)
    return histograma

# def check_crossings(perm_list,det_list,params,perm_team,side,frame):

#     if check_is_appearing_after_blocking_view_partner(perm_list,det_list,perm_team,side,params,frame):
        
#         # COMPARAR LAS RESPECTIVAS Ys. CREAR COST MATRIX
#         cost_matrix = np.empty([])
#         cost_matrix=create_cost_matrix(perm_list,det_list,cost_matrix,2)
#         fill_cost_matrix_crossing(perm_list,det_list,cost_matrix)

#         # APPLY HUNGARIAN ASSIGNMENT
#         perm_team.match_line1=[]
#         perm_team.match_line2=[]
#         [detected_player_ind , perm_player_ind, opt_cost]=hungarian_assignment(cost_matrix)
#         for i in range(len(perm_player_ind)):
#             perm_index=perm_player_ind[i]
#             det_index=detected_player_ind[i]            
#             if perm_index==0:
#                 perm_team.match_line1.append(perm_list[perm_index].pos.posXY)
#                 perm_team.match_line1.append(det_list[det_index].pos.posXY)
#             if perm_index==1:  
#                 perm_team.match_line2.append(perm_list[perm_index].pos.posXY)
#                 perm_team.match_line2.append(det_list[det_index].pos.posXY)   

#             perm_list[perm_index].pos = det_list[det_index].pos   

    


# Función para comparar histogramas utilizando diferentes métodos
def comparar_histogramas(hist1, hist2):
    metodos = {
        'Correlación': cv2.HISTCMP_CORREL,
        'Chi-cuadrado': cv2.HISTCMP_CHISQR,
        'Intersección': cv2.HISTCMP_INTERSECT,
        'Distancia Bhattacharyya': cv2.HISTCMP_BHATTACHARYYA
    }

    # 'Correlación': 1: Muy similares, 0: Ninguna relación, valores negativos: Relación inversa.
    # 'Chi-cuadrado' -> 0: Histogramas idénticos, valores grandes: Gran diferencia.
    # 'Intersección' -> 0: Sin superposición, valor alto: Alta superposición (similitud).
    # 'Distancia Bhattacharyya'-> 0: Histogramas idénticos, valores grandes: Gran diferencia.

    # resultados = {}
    # for nombre, metodo in metodos.items():
    #     comparacion = 0
    #     # Comparar cada canal por separado y calcular el promedio
    #     for i in range(3):
    #         comparacion += cv2.compareHist(hist1[i], hist2[i], metodo)
    #     comparacion /= 3  # Promedio de los tres canales
    #     resultados[nombre] = comparacion
    comparacion=0
    for i in range(3):
        comparacion += cv2.compareHist(hist1[i], hist2[i], cv2.HISTCMP_BHATTACHARYYA)
        comparacion /= 3  # Promedio de los tres canales
    
    return comparacion

def check_is_appearing_after_blocking_view_partner(perm_list,det_list,perm_team,side,params,frame):

    if len(perm_list)!=2 :
        return False

    if len(det_list)<2:
        perm_team.missing[side]=1
        return False

    if len(det_list)==2 and perm_team.missing[side]==1:
        perm_team.missing[side]=0
        # Calculate histogram of the detceted objects
        for player in det_list:

            new_frame = frame[player.pos.y0:player.pos.yEnd,player.pos.x0:player.pos.xEnd]
            hist = calcular_histograma(new_frame)
            # Normalizar el histograma
            if not isinstance(hist, np.ndarray):
                hist = np.array(hist, dtype=np.float32)
            player.hist = cv2.normalize(hist, hist, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
            # player.hist=hist
            # cv2.rectangle(frame, (player.pos.x0, player.pos.y0), (player.pos.xEnd, player.pos.yEnd), (0, 255, 0), 2)
            # cv2.imshow("frame2 ",new_frame)

        return True
    
    # # Update Histogram
    # time_init=time.time()
    for player in perm_list:
        new_frame = frame[player.pos.x0:player.pos.xEnd,player.pos.y0:player.pos.yEnd]
        hist = calcular_histograma(new_frame)
        if not isinstance(hist, np.ndarray):
            hist = np.array(hist, dtype=np.float32)
        player.hist = cv2.normalize(hist, hist, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    # print("hist time : ", time.time()-time_init)
    
    return False


def hungarian_assignment(cost_matrix):

    # Perform the Hungarian algorithm (linear sum assignment)
    row_ind, col_ind = linear_sum_assignment(cost_matrix)

    # # Print results
    # print("Optimal assignment:")
    # for i, j in zip(row_ind, col_ind):
    #     print(f"Tracking {i+1} -> Agent {j+1}")

    # print("\nTotal optimal cost:", cost_matrix[row_ind, col_ind].sum())

    cnt=0
    opt_cost=[]
    for row in row_ind:
            col=col_ind[cnt]
            cnt+=1
            # print("cost_matrix element ",cnt," : ", cost_matrix[row, col])
            opt_cost.append(cost_matrix[row, col])
    return [row_ind, col_ind, opt_cost]

def create_cost_matrix(permPlayerList,detPlayerList,cost_matrix):
    cost_matrix = np.empty([])

    for i in range(len(detPlayerList)):
        cost_array=np.array([])
        new_data= np.array([5000])
        for j in range(len(permPlayerList)):
            cost_array = np.concatenate((cost_array, new_data))
        if i==0: 
            cost_matrix=cost_array
        else:
            cost_matrix = np.vstack((cost_matrix, cost_array))

    return cost_matrix

def fill_cost_matrix(permPlayerList,detPlayerList,cost_matrix):
        cnt_detected=0
        for det_player in detPlayerList:
            cnt_perm=0
            for perm_player in permPlayerList:
                # Calculate distance between players
                distance=math.sqrt(pow(det_player.pos.lowerMidX-perm_player.pos.lowerMidX,2)+pow(det_player.pos.lowerMidY-perm_player.pos.lowerMidY,2))
                # dist=math.sqrt(pow(det_player.RealMidPointX-perm_player.RealMidPointX,2)+pow(det_player.RealMidPointY-perm_player.RealMidPointY,2))
                cost_matrix[cnt_detected][cnt_perm]=distance
                cnt_perm+=1
            cnt_detected+=1

# def fill_cost_matrix_crossing(perm_list,detPlayerList,cost_matrix):
#     cnt_detected=0

#     cost_matrix2=[[0,0],[0,0]]
#     for detected_player in detPlayerList:
#         cnt_perm=0
#         for perm_player in perm_list:
#             if perm_player.active==1:
#                 # Calculate distance between players
#                 distance=round(math.sqrt(pow(detected_player.RealMidPointX-perm_player.RealMidPointX,2)+pow(detected_player.RealMidPointY-perm_player.RealMidPointY,2)),2)
#                 cost_matrix[cnt_detected][cnt_perm]=distance

#             cnt_perm+=1
#         cnt_detected+=1

def ensure_iterable(data):
    if isinstance(data, (int, float)):  # If it's an integer, wrap it in a list
        return [data]
    return data  # If it's already a list, return it as is

def store_new_perm_players_position(perm_player_ind,detected_player_ind,permPlayerList,opt_cost,detPlayerList):
    player_active_vector=[0] * len(permPlayerList)

    it_perm_player_ind = ensure_iterable(perm_player_ind)
    it_opt_cost= ensure_iterable(opt_cost)
    it_detected_player_ind = ensure_iterable(detected_player_ind)
    
    for i in range(len(it_perm_player_ind)):
        perm_index=it_perm_player_ind[i]
        det_index=it_detected_player_ind[i]
        perm_player=permPlayerList[perm_index]
        player_active_vector[perm_index]=1

        threshold=perm_player.th_opt_cost
        if perm_player.quadrant==6 or perm_player.quadrant==9:
            threshold=150

        if it_opt_cost[i]<threshold:

            perm_player.pos_old=perm_player.pos

            perm_player.pos = detPlayerList[det_index].pos
            perm_player.pos.posXY = detPlayerList[det_index].pos.posXY

            perm_player.pos.midPointX=detPlayerList[det_index].pos.midPointX
            perm_player.pos.midPointY=detPlayerList[det_index].pos.midPointY

            perm_player.pos.lowerMidX=detPlayerList[det_index].pos.lowerMidX
            perm_player.pos.lowerMidY=detPlayerList[det_index].pos.lowerMidY
            
            perm_player.RealMidPointX = detPlayerList[det_index].RealMidPointX
            perm_player.RealMidPointY = detPlayerList[det_index].RealMidPointY

            perm_player.th_opt_cost=perm_player.th_opt_cost_init
            perm_player.frame=detPlayerList[det_index].frame
            perm_player.quadrant_old=perm_player.quadrant
            perm_player.quadrant=detPlayerList[det_index].quadrant
            perm_player.height_old=perm_player.height
            perm_player.height=detPlayerList[det_index].height
            perm_player.width_old=perm_player.width
            perm_player.width=detPlayerList[det_index].width

            perm_player.shoe_list=detPlayerList[det_index].shoe_list

            perm_player.distance_vect.append(it_opt_cost[i])
            if len(perm_player.distance_vect)>3:
                del perm_player.distance_vect[0]

            perm_player.posX_vect.append(perm_player.pos.midPointX)
            perm_player.posY_vect.append(perm_player.pos.midPointY)
            if len(perm_player.posX_vect)>3:
                del perm_player.posX_vect[0]
                del perm_player.posY_vect[0]

            Xmax = max(perm_player.posX_vect)
            Xmin = min(perm_player.posX_vect)
            Ymax = max(perm_player.posY_vect)
            Ymin = min(perm_player.posY_vect)
            perm_player.dist_done=round(math.sqrt(pow(Xmax-Xmin,2)+pow(Ymax-Ymin,2)),2)


        # perm_player.active=1
        else:
            perm_player.active=0
            perm_player.th_opt_cost+=10

    # print("player_active_vector : ", player_active_vector, "  len : ", len(permPlayerList))
    for i in range(len(permPlayerList)):
        if player_active_vector[i]==0: #Player not active
            permPlayerList[i].active=0


def CheckInitialPartners(perm_team,params):
    for player in perm_team.player_list:
        if player.quadrant_line==1:
            player.partner=3
        if player.quadrant_line==3:
            player.partner=1
        if player.quadrant_line==2:
            player.partner=4
        if player.quadrant_line==4:
            player.partner=2

def check_initial_id(perm_team,params):

    if perm_team.initial_id==0: # Initiate player in each position
        playerInPos_vect = [0,0,0,0]
        for player in perm_team.player_list:
            if player.side==0:
                for quadrant in params.quadr_matrix[0]: #Upper Left
                    if player.quadrant==quadrant:
                        line=1
                        player.quadrant_line=line
                        playerInPos_vect[line-1]=1
                        perm_team.player_height[0][0]=line
                for quadrant in params.quadr_matrix[1]: #Down Left
                    if player.quadrant==quadrant:
                        line=3
                        player.quadrant_line=line
                        playerInPos_vect[line-1]=1
                        perm_team.player_height[0][1]=line
            if player.side==1:
                for quadrant in params.quadr_matrix[0]: #Upper Right
                    if player.quadrant==quadrant:
                        line=2
                        player.quadrant_line=line
                        playerInPos_vect[line-1]=1
                        perm_team.player_height[1][0]=line
                for quadrant in params.quadr_matrix[1]: #Down Right
                    if player.quadrant==quadrant:
                        line=4
                        player.quadrant_line=line
                        playerInPos_vect[line-1]=1
                        perm_team.player_height[1][1]=line

        if sum(playerInPos_vect)==4: # 
            for player in perm_team.player_list:
                player.id=player.quadrant_line

            CheckInitialPartners(perm_team,params)

            perm_team.initial_id=1

def check_new_id_after_side_change(perm_team,params):

    if perm_team.change_side==1: 
        # Check players in correct position
        playerInPos_vect = [[0,0],[0,0]]
        for player in perm_team.player_list:
            for side in range(len(params.full_quadr_matrix)):
                    for height in range(len(params.full_quadr_matrix[side])):
                        for quadrant in params.full_quadr_matrix[side][height]: 
                            if player.quadrant==quadrant:
                                playerInPos_vect[side][height]=1

        if sum(playerInPos_vect[0][:])+sum(playerInPos_vect[1][:])==4: 
            print("UPDATE IDS : ")

            # Update previous IDs
            for side in range(len(perm_team.player_height)):
                for height in range(len(perm_team.player_height[side])):
                    perm_team.player_prev_height[side][height]=perm_team.player_height[side][height]

            # Invert players
            perm_team.player_height[0][0]=copy.deepcopy(perm_team.player_prev_height[1][1])
            perm_team.player_height[0][1]=copy.deepcopy(perm_team.player_prev_height[1][0])
            perm_team.player_height[1][0]=copy.deepcopy(perm_team.player_prev_height[0][1])
            perm_team.player_height[1][1]=copy.deepcopy(perm_team.player_prev_height[0][0])

            print("perm_team.player_height : ", perm_team.player_height)

            # Assign players new Id
            for player in perm_team.player_list:
                for side in range(len(params.full_quadr_matrix)):
                    for height in range(len(params.full_quadr_matrix[side])):
                        for quadrant in params.full_quadr_matrix[side][height]:
                            if player.quadrant==quadrant:
                                player.id=copy.deepcopy(perm_team.player_height[side][height])
                                player.side=side
                                player.side_old=player.side_old
            
            # Reset partners
            for player in perm_team.player_list:
                if player.id==1:
                    player.partner=3
                if player.id==2:
                    player.partner=4
                if player.id==3:
                    player.partner=1
                if player.id==4:
                    player.partner=2

            perm_team.change_side=0
            perm_team.player_missing_vector = [0,0,0,0]

def check_minimum_detected_players(det_team,perm_team):

    # Check only players inside quadrants
    cnt=0
    for player in det_team.player_list:
        if player.quadrant<=12:
            cnt+=1

    if cnt<=1:
        return False
    return True