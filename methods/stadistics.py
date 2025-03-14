from methods import yolo_data

def process(perm_team, results,params,model):

    yolo_data.convertData(params,results,model,perm_team)

    