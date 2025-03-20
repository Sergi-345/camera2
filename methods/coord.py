from shapely.geometry import Point, Polygon
import scipy.interpolate
import numpy as np
import math
import cv2


def findRWCoordMatrix(player, params): 

    
    pos=player.pos
    # Find initial point
    img_ball=[pos.x0+(pos.xEnd-pos.x0)/2,pos.yEnd]
    
    point=Point(img_ball)

    img_quadrant=[]
    map_quadrant=[]


    # FIND CURRENT QUADRANT
    for i in range(len(params.poly_img_list[player.side])):
        a = point.within(params.poly_img_list[player.side][i])
        if a:
            # Quadrant in image coordinates
            img_quadrant= params.sq_img_list[player.side][i]
            # Quadrant in real coordinates
            map_quadrant = params.sq_map_list[player.side][i]
     
    ##########################################################################

    # Coordenadas de los landmarks en el plano perspectiva
    perspectiva = np.array([img_quadrant], dtype=np.float32)

    # Coordenadas correspondientes en el plano planta
    planta = np.array([map_quadrant], dtype=np.float32)

    # Calcular la matriz de homografía
    H, _ = cv2.findHomography(perspectiva, planta)

    # Transformar un punto (x, y) en perspectiva
    punto_perspectiva = np.array([img_ball], dtype=np.float32)
    punto_planta = cv2.perspectiveTransform(np.array([punto_perspectiva]), H)

    return punto_planta[0][0]