from UI import VarUI
from methods import myApp_class
from methods import showCoordinates
from methods import template_
from methods import checkboxes_
from methods import worker2_detections
from methods import worker3_stadistics
from methods import worker4_redisData
from methods import team_class
from methods import worker_save_video
from methods import parameters
import methods.worker_from_file as worker_from_file
import methods.worker_from_camera as worker_from_camera
import save_image
import redis
import threading
import queue as q
import time
import os
from ultralytics import YOLO
# from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal, pyqtSlot, Qt)
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog

# Evento para detener el hilo
stop_event = threading.Event()

def open_folder():
    # file_dialog = QFileDialog()
    folder_path = QFileDialog.getExistingDirectory(MainWindow, "Select Folder", "")
    # print("folder")
    ui.folder_name_textEdit.setText(folder_path)
    MainWindow.params["folder_name"]=folder_path
    MainWindow.start=0
    

def start():

    perm_team = team_class.TEAM(0)
    params = parameters.PARAMS()
    folder = MainWindow.params["folder_name"]
    MainWindow.curr_width = MainWindow.params["width"]
    MainWindow.curr_height = MainWindow.params["height"]

    ### INITIALISE REDIS CLIENT
    redis_client = redis.Redis(host='localhost', port=6379, db=0)  # Assuming no password
    
    HOME = os.getcwd()
    # local_model = YOLO(f'{HOME}/models/best.pt').to("cuda")
    model1 = YOLO(f'{HOME}/models/best.engine')
    model2 = YOLO(f'{HOME}/models/best.engine')

    q1_detectL=q.Queue() # Detections1
    q1_detectR=q.Queue() # Detections1
    q3_stad=q.Queue() # Stadistics
    q_saveL = q.Queue()
    q_saveR = q.Queue()
    
    if MainWindow.params["from_file"]== 0:
        MainWindow.params["start"]=1

        ## THREADS TO SAVE VIDEO
        threading.Thread(target=worker_save_video.save_video,  args=(stop_event,ui,MainWindow,"L",q_saveL), daemon=True).start()
        threading.Thread(target=worker_save_video.save_video,  args=(stop_event,ui,MainWindow,"R",q_saveR), daemon=True).start()
        time.sleep(1)
        ## THREADS TO DETECTIONS
        threading.Thread(target=worker2_detections.worker,  args=(stop_event,ui,MainWindow,q1_detectL,q3_stad,model1,"L"), daemon=True).start()
        time.sleep(2)
        threading.Thread(target=worker2_detections.worker,  args=(stop_event,ui,MainWindow,q1_detectR,q3_stad,model2,"R"), daemon=True).start()
        time.sleep(5)
        ## THREADS TO VIDEO SOURCE
        params.load_data(folder,MainWindow)
        threading.Thread(target=worker_from_camera.worker,  args=(stop_event,ui,MainWindow,"L",q_saveL,q1_detectL), daemon=True).start()
        threading.Thread(target=worker_from_camera.worker,  args=(stop_event,ui,MainWindow,"R",q_saveR,q1_detectR), daemon=True).start()
        time.sleep(3)
        ## THREAD TO STATISTICS
        params.load_data(folder,MainWindow)
        threading.Thread(target=worker3_stadistics.worker,  args=(stop_event,ui,MainWindow,q3_stad,perm_team,q_saveL,q_saveR,params, model1), daemon=True).start()
        ## THREAD TO REDIS
        time.sleep(3)
        threading.Thread(target=worker4_redisData.worker,  args=(stop_event,perm_team,redis_client), daemon=True).start()

    else:
        
        MainWindow.params["start_file"]=1
        
        ## THREADS TO SAVE VIDEO
        threading.Thread(target=worker_save_video.save_video_processed,  args=(stop_event,ui,MainWindow,params,"L",q_saveL), daemon=True).start()
        threading.Thread(target=worker_save_video.save_video_processed,  args=(stop_event,ui,MainWindow,params,"R",q_saveR), daemon=True).start()
        time.sleep(1)
        ## THREADS TO DETECTIONS
        threading.Thread(target=worker2_detections.worker,  args=(stop_event,ui,MainWindow,q1_detectL,q3_stad,model1,"L"), daemon=True).start()
        threading.Thread(target=worker2_detections.worker,  args=(stop_event,ui,MainWindow,q1_detectR,q3_stad,model2,"R"), daemon=True).start()
        time.sleep(5)
        ## THREADS TO VIDEO SOURCE
        threading.Thread(target=worker_from_file.worker,  args=(stop_event,ui,MainWindow,"L",q1_detectL), daemon=True).start()
        threading.Thread(target=worker_from_file.worker,  args=(stop_event,ui,MainWindow,"R",q1_detectR), daemon=True).start()
        time.sleep(3)
        ## THREAD TO STATISTICS
        params.load_data(folder,MainWindow)
        threading.Thread(target=worker3_stadistics.worker,  args=(stop_event,ui,MainWindow,q3_stad,perm_team,q_saveL,q_saveR,params, model1), daemon=True).start()
        ## THREAD TO REDIS
        time.sleep(3)
        threading.Thread(target=worker4_redisData.worker,  args=(stop_event,perm_team,redis_client), daemon=True).start()

def stop():
    MainWindow.params["start"]=0
    MainWindow.params["start_file"]=0

def select_file():
    open_folder()

def create_images():
    save_image.save_frame(MainWindow,ui,"L")
    save_image.save_frame(MainWindow,ui,"R")



if __name__ == "__main__":

    actions=showCoordinates.CLICK_DETECTOR()

    # -----------INITIALIZE UI--------------
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = myApp_class.MyApp()
    # ui = VarUI.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    ui=MainWindow.ui

    # print(MainWindow.params)
    ui.start_pushButton.clicked.connect(start)
    ui.stop_pushButton.clicked.connect(stop)
    ui.brightness_pushButton.clicked.connect(lambda: checkboxes_.set_brightness(MainWindow, ui))
    ui.contrast_pushButton.clicked.connect(lambda: checkboxes_.set_contrast(MainWindow, ui))
    ui.saturation_pushButton.clicked.connect(lambda: checkboxes_.set_saturation(MainWindow, ui))
    ui.gamma_pushButton.clicked.connect(lambda: checkboxes_.set_gamma(MainWindow, ui))
    ui.white_balance_pushButton.clicked.connect(lambda: checkboxes_.set_white_balance(MainWindow, ui))
    ui.create_images_pushButton.clicked.connect(create_images)

    ui.contrast_textEdit.setPlainText(str(MainWindow.params["contrast"])) 
    ui.brightness_textEdit.setPlainText(str(MainWindow.params["brightness"]))
    ui.gamma_textEdit.setPlainText(str(MainWindow.params["gamma"])) 
    ui.saturation_textEdit.setPlainText(str(MainWindow.params["saturation"])) 
    ui.white_balance_textEdit.setPlainText(str(MainWindow.params["white_balance_temperature"])) 

    if MainWindow.params["record"]==1:
        ui.checkBox_record_video.setChecked(True)
    else:
        ui.checkBox_record_video.setChecked(False)

    if MainWindow.params["plot"]==1:
        ui.checkBox_plot_video.setChecked(True)
    else:
        ui.checkBox_plot_video.setChecked(False)

    if MainWindow.params["visualise_processed"]==1:
        ui.checkBox_visualise_processed.setChecked(True)
    else:
        ui.checkBox_visualise_processed.setChecked(False)

    if MainWindow.params["visualise_raw"]==1:
        ui.checkBox_visualise_raw.setChecked(True)
    else:
        ui.checkBox_visualise_raw.setChecked(False)

    if MainWindow.params["from_file"]==1:
        ui.checkBox_from_file.setChecked(True)
    else:
        ui.checkBox_from_file.setChecked(False)

    ui.checkBox_record_video.stateChanged.connect(lambda: checkboxes_.on_checkbox_changed(MainWindow, ui)) 
    ui.checkBox_plot_video.stateChanged.connect(lambda: checkboxes_.on_checkbox_changed(MainWindow, ui)) 
    ui.checkBox_visualise_raw.stateChanged.connect(lambda: checkboxes_.on_checkbox_changed(MainWindow, ui))
    ui.checkBox_visualise_processed.stateChanged.connect(lambda: checkboxes_.on_checkbox_changed(MainWindow, ui))
    ui.checkBox_from_file.stateChanged.connect(lambda: checkboxes_.on_checkbox_changed(MainWindow, ui)) 
    ui.file_pushButton.clicked.connect(select_file)
    ui.court_points_L_pushButton.clicked.connect(lambda: template_.draw_points(MainWindow, actions,"L"))
    ui.court_points_R_pushButton.clicked.connect(lambda: template_.draw_points(MainWindow, actions,"R"))
    ui.save_points_pushButton.clicked.connect(lambda: template_.save_points(MainWindow, actions))

    ui.folder_name_textEdit.setText(MainWindow.params["folder_name"])

    ui.img_size_comboBox.addItems(MainWindow.params["image_size"])
    ui.cut_comboBox.addItems(MainWindow.params["image_size_cut"])

    # Set default selection
    ui.img_size_comboBox.setCurrentIndex(MainWindow.params["current_size_index"])
    ui.img_size_comboBox.currentIndexChanged.connect(lambda index: checkboxes_.item_changed(MainWindow, ui, index))

    ui.cut_comboBox.setCurrentIndex(MainWindow.params["cut_index"])
    ui.cut_comboBox.currentIndexChanged.connect(lambda index: checkboxes_.item_changed_cut(MainWindow, ui, index))

    ui.jumps_textEdit.setText(str(MainWindow.params["jumps"]))
    ui.jumps_textEdit.textChanged.connect(lambda: checkboxes_.jumps_changed(MainWindow, ui))

    ui.time_sleep_textEdit.setText(str(MainWindow.params["time_sleep_processed"]))
    ui.time_sleep_textEdit.textChanged.connect(lambda: checkboxes_.time_sleep_changed(MainWindow, ui))

    ui.batch_size_textEdit.setText(str(MainWindow.params["batch_size"]))
    ui.batch_size_textEdit.textChanged.connect(lambda: checkboxes_.batch_size_changed(MainWindow, ui))

    
    MainWindow.show()
    
    sys.exit(app.exec())  # Use exec() instead of exec_()


