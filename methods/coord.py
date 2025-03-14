from shapely.geometry import Point, Polygon
import scipy.interpolate
import numpy as np
import math
import cv2


def findRWCoordMatrix(pos, params): # It will work for elevated camera position
    
    # Find initial point
    
    img_ball=[pos.x0+(pos.xEnd-pos.x0)/2,pos.yEnd]
    
    point=Point(img_ball)
    
    x=[]
    R_x=[]
    y=[]
    R_y=[]

    img_quadrant=[]
    real_quadrant=[]

    
    
    # FIND CURRENT QUADRANT
    for i in range(len(params.poly_vect)):
        a = point.within(params.poly_vect[i])
        if a:
            # Quadrant in image coordinates
            img_quadrant= params.squares_list[i]
            # Quadrant in real coordinates
            real_quadrant = params.Rpoints_vect[i]

    if img_quadrant==[]:
        return [50,50] # Out of the map
     

    ##########################################################################

    # print("params.squares_list : ", params.squares_list)

    # Coordenadas de los landmarks en el plano perspectiva
    perspectiva = np.array([img_quadrant], dtype=np.float32)

    # Coordenadas correspondientes en el plano planta
    planta = np.array([real_quadrant], dtype=np.float32)

    # Calcular la matriz de homografía
    H, _ = cv2.findHomography(perspectiva, planta)

    # Transformar un punto (x, y) en perspectiva
    punto_perspectiva = np.array([img_ball], dtype=np.float32)
    punto_planta = cv2.perspectiveTransform(np.array([punto_perspectiva]), H)

    # print("punto planta : ", punto_planta[0][0])

    if punto_planta[0][0][1]>10:
        punto_planta[0][0][1]=10

    return punto_planta[0][0]