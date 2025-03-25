import redis
import json
import time

def worker(stop_event,perm_team,redis_client):
    
    while True:
        if stop_event.is_set():
            break

        time.sleep(2)

        cnt=0
        json_global={}
        for player in perm_team.player_list:

            num=player.id-1
            player_pos_vector=[perm_team.counter_in_defense[num],perm_team.counter_in_transition[num],perm_team.counter_in_attack[num]]
            pos_percentage=[]

            for zone in range(len(player_pos_vector)):
                pos_percentage.append(0)
                if sum(player_pos_vector)>0:
                    pos_percentage[zone]=round(round(player_pos_vector[zone]/sum(player_pos_vector),2)*100)

            ## Sent data to Redis Client
            # Create Data box for player
            if player.id==1:
                text= "playerone"
            if player.id==2:
                text= "playertwo"
            if player.id==3:
                text= "playerthree"
            if player.id==4:
                text= "playerfour"
            if player.id==5:
                text= "playerfive"
            json1 = {
                text: {
                    "playerZoneDistro": {
                        "time_in_defense": pos_percentage[0],
                        "time_in_transition": pos_percentage[1],
                        "time_in_attack": pos_percentage[2],
                        },
                    "serveCoordinates": [],
                    "heatMap":[]
                }
            }
            for ball in perm_team.ballBounceAfterKick_list:
                if ball.kickplayerId==player.id:
                    ball_data= {"serve_x": float(ball.RealMidPointX), "serve_y": float(ball.RealMidPointY)}

                    json1[text]["serveCoordinates"].append(ball_data)

            # HEAT MAP
            coord_vector=perm_team.coord_matrix[num]
            for coord in coord_vector:
                pos_data = {"x": float(coord[0]), "y": float(coord[1])}
                json1[text]["heatMap"].append(pos_data)

            # json1[text]["heatMap"]=player.heatMap.tolist()
            # coord_vector = np.array(player.coord_vector, dtype=np.float32)
            # json1[text]["heatMap"]=coord_vector.tolist()
            # ACCUMULATED DISTANCE
            json1[text]["distanceAccum"]= perm_team.dist_acum_matrix[num]

            
            # print(text, " : ",json1[text]["serveCoordinates"])
            # print("len : ",len(json1[text]["serveCoordinates"]))

            
            json_global = {**json_global, **json1}
            cnt+=1

        # print("json_global : ")
        # Convert the dictionary to a JSON string
        json_global_str = json.dumps(json_global)

        # Set the JSON string in Redis
        redis_client.hset('gameData:101', mapping={'data': json_global_str})

        # Printing data in order to verify that the data was stored correctly
        # stored_data = redis_client.hgetall('gameData:101')

