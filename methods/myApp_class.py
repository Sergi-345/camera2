import json
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal, pyqtSlot, Qt)
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog


class EmptyClass:
    pass

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
