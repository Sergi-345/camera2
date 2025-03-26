import json
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal, pyqtSlot, Qt)
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog
from PyQt6.QtCore import pyqtSlot
from UI import VarUI

class EmptyClass:
    pass

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = VarUI.Ui_MainWindow()  # Create the UI object inside MyApp
        self.ui.setupUi(self)

        self.params = vars(EmptyClass())
        self.load_params()  # Update with JSON values if available
        self.cnt_video_frames=0
        self.start=0
        self.start_vect=[0,0]
        self.qstad_size=0
        self.qsaveL_size=0
        self.qsaveR_size=0
        self.velR=0
        self.velL=0
        self.qdetL_size=0
        self.qdetR_size=0  

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
                # print("self.params : ", self.params)
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
    
    @pyqtSlot()
    def update_ui(self):
        self.ui.qsaveL_size_textEdit.setText(str(self.qsaveL_size))
        self.ui.qsaveR_size_textEdit.setText(str(self.qsaveR_size))
        self.ui.qdetL_size_textEdit.setText(str(self.qdetL_size))
        self.ui.qdetR_size_textEdit.setText(str(self.qdetR_size))
        self.ui.qstad_size_textEdit.setText(str(self.qstad_size))
        self.ui.velL_textEdit.setText(str(self.velL))
        self.ui.velR_textEdit.setText(str(self.velR))

    # @pyqtSlot()
    # def update_ui(self):
    #     self.ui.qstad_size_textEdit.setText(str(self.qstad_size))
    #     self.ui.qsaveL_size_textEdit.setText(str(self.qsaveL_size))
    #     self.ui.qsaveR_size_textEdit.setText(str(self.qsaveR_size))
    #     self.ui.velL_textEdit.setText(str(self.velL))
    #     self.ui.velR_textEdit.setText(str(self.velR))
