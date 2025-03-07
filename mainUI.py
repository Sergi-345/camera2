from varUI import VarUI
from methods import showCoordinates
from methods import template_
from methods import checkboxes_
from methods import worker2_detections
from methods import worker3_stadistics
from methods import team_class
import methods.worker_from_file as worker_from_file
import methods.worker_from_camera as worker_from_camera
import save_image
import repeat
import subprocess
# import main_RT
import threading
import queue as q
import json
import time
import cv2
import os
import torch
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
    
    if MainWindow.params["from_file"]== 0:
        MainWindow.params["start"]=1
            # Iniciar el hilo con la función worker
        threading.Thread(target=worker_from_camera.worker,  args=(stop_event,ui,MainWindow,"L"), daemon=True).start()
        time.sleep(2)
        threading.Thread(target=worker_from_camera.worker,  args=(stop_event,ui,MainWindow,"R"), daemon=True).start()
        time.sleep(2)
    else:
        
        MainWindow.params["start_file"]=1
        perm_team = team_class.TEAM()

        q1=q.Queue() # Detections1
        q2=q.Queue() # Detections1
        q3=q.Queue() # Stadistics
        #### STREAMS
        model1 = HOME = os.getcwd()
    # local_model = YOLO(f'{HOME}/models/best.pt').to("cuda")
        model1 = YOLO(f'{HOME}/models/best.engine')
        model2 = YOLO(f'{HOME}/models/best.engine')

        threading.Thread(target=worker2_detections.worker,  args=(stop_event,ui,MainWindow,q1,q3,model1), daemon=True).start()
        time.sleep(3)
        threading.Thread(target=worker2_detections.worker,  args=(stop_event,ui,MainWindow,q2,q3,model2), daemon=True).start()
        time.sleep(10)
        threading.Thread(target=worker_from_file.worker,  args=(stop_event,ui,MainWindow,"L",q1), daemon=True).start()
        time.sleep(3)
        threading.Thread(target=worker_from_file.worker,  args=(stop_event,ui,MainWindow,"R",q2), daemon=True).start()
        time.sleep(3)
        threading.Thread(target=worker3_stadistics.worker,  args=(stop_event,ui,MainWindow,q3,perm_team), daemon=True).start()

def stop():
    MainWindow.params["start"]=0
    MainWindow.params["start_file"]=0

def select_file():
    open_folder()

def create_images():
    save_image.save_frame(MainWindow,ui,"L")
    save_image.save_frame(MainWindow,ui,"R")

class EmptyClass:
    pass

# empty_instance = EmptyClass()

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("PyQt con Hilo Funcional")
        # self.setGeometry(100, 100, 400, 300)

        # # Iniciar el hilo con la función worker
        
        self.params = vars(EmptyClass())
        self.load_params()  # Update with JSON values if available
        self.cnt_video_frames=0
        self.start=0
        
        # threading.Thread(target=workerVAR1_camera.worker1,  args=(params,stop_event,self), daemon=True).start()

    def closeEvent(self, event):
        """Save parameters to JSON when closing the UI."""
        self.save_params()
        event.accept()  # Allow the window to close

    def save_params(self):
        """Save parameters to a JSON file."""
        try:
            with open("params.json", "w") as file:
                self.params["repeat"] = 0
                self.params["start"] = 0
                print("self.params : ", self.params)
                json.dump(self.params, file, indent=4)
            print("✅ Parameters saved successfully!")
        except Exception as e:
            print(f"❌ Error saving parameters: {e}")
    
    def load_params(self):
        """Load parameters from JSON file and update self.params."""
        try:
            with open("params.json", "r") as file:
                loaded_params = json.load(file)

            # Update only existing keys to avoid overwriting defaults
            for key, value in loaded_params.items():

                # if key in self.params:  # Ensure we don't add unknown keys
                self.params[key] = value
            
            print("✅ Parameters loaded successfully!")
        except FileNotFoundError:
            print("⚠️ No existing parameters file found, using defaults.")
        except Exception as e:
            print(f"❌ Error loading parameters: {e}")



if __name__ == "__main__":

    actions=showCoordinates.CLICK_DETECTOR()

    ### TURN-ON WORKERS THREADS
    # threading.Thread(target=workerVAR1_camera.worker1,  args=(params,), daemon=True).start()

    # -----------INITIALIZE UI--------------
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = MyApp()
    ui = VarUI.Ui_MainWindow()
    ui.setupUi(MainWindow)


    print(MainWindow.params)
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

    if MainWindow.params["visualise"]==1:
        ui.checkBox_visualise.setChecked(True)
    else:
        ui.checkBox_visualise.setChecked(False)

    if MainWindow.params["from_file"]==1:
        ui.checkBox_from_file.setChecked(True)
    else:
        ui.checkBox_from_file.setChecked(False)

    ui.checkBox_record_video.stateChanged.connect(lambda: checkboxes_.on_checkbox_changed(MainWindow, ui)) 
    ui.checkBox_plot_video.stateChanged.connect(lambda: checkboxes_.on_checkbox_changed(MainWindow, ui)) 
    ui.checkBox_visualise.stateChanged.connect(lambda: checkboxes_.on_checkbox_changed(MainWindow, ui)) 
    ui.checkBox_from_file.stateChanged.connect(lambda: checkboxes_.on_checkbox_changed(MainWindow, ui)) 
    ui.file_pushButton.clicked.connect(select_file)
    ui.court_points_L_pushButton.clicked.connect(lambda: template_.draw_points(MainWindow, actions,"L"))
    ui.court_points_R_pushButton.clicked.connect(lambda: template_.draw_points(MainWindow, actions,"R"))
    ui.save_points_pushButton.clicked.connect(lambda: template_.save_points(MainWindow, actions))
    

    ui.folder_name_textEdit.setText(MainWindow.params["folder_name"])

    ui.img_size_comboBox.addItems(MainWindow.params["image_size"])

        # Set default selection
    ui.img_size_comboBox.setCurrentIndex(MainWindow.params["current_size_index"])
    ui.img_size_comboBox.currentIndexChanged.connect(lambda index: checkboxes_.item_changed(MainWindow, ui, index))


    MainWindow.show()
    
    sys.exit(app.exec())  # Use exec() instead of exec_()


