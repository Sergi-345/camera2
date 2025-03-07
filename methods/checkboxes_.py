import subprocess


def on_checkbox_changed(MainWindow,ui):
    if ui.checkBox_record_video.isChecked():
        MainWindow.params["record"]=  1
    else:
        MainWindow.params["record"]=  0

    if ui.checkBox_plot_video.isChecked():
        MainWindow.params["plot"]=  1
    else:
        MainWindow.params["plot"]=  0

    if ui.checkBox_visualise.isChecked():
        MainWindow.params["visualise"]=  1
    else:
        MainWindow.params["visualise"]=  0

    if ui.checkBox_from_file.isChecked():
        MainWindow.params["from_file"]=  1
        
    else:
        MainWindow.params["from_file"]=  0





def set_brightness(MainWindow,ui):
    ## Camera 1
    brightness = int(ui.brightness_textEdit.toPlainText())
    print("new brightness : ", brightness)
    """Runs the v4l2-ctl command to set brightness."""
    # command = ["v4l2-ctl", "--device=/dev/video0", "--set-ctrl=brightness=200"]
    command = ["v4l2-ctl", "--device=/dev/video0", "--set-ctrl=brightness={}".format(brightness)]

    try:
        subprocess.run(command, check=True)
        MainWindow.params["brightness"]=brightness
        print("Brightness set successfully!")
    except subprocess.CalledProcessError as e:
        print("Error setting brightness:", e)


    command = ["v4l2-ctl", "--device=/dev/video2", "--set-ctrl=brightness={}".format(brightness)]

    try:
        subprocess.run(command, check=True)
        MainWindow.params["brightness"]=brightness
        print("Brightness set successfully!")
    except subprocess.CalledProcessError as e:
        print("Error setting brightness:", e)

def set_contrast(MainWindow,ui):

    contrast = int(ui.contrast_textEdit.toPlainText())
    print("new contrast : ", contrast)
    """Runs the v4l2-ctl command to set brightness."""
    # command = ["v4l2-ctl", "--device=/dev/video0", "--set-ctrl=brightness=200"]
    command = ["v4l2-ctl", "--device=/dev/video0", "--set-ctrl=contrast={}".format(contrast)]

    try:
        subprocess.run(command, check=True)
        MainWindow.params["contrast"]=contrast
        print("contrast set successfully!")
    except subprocess.CalledProcessError as e:
        print("Error setting contrast:", e)

    command = ["v4l2-ctl", "--device=/dev/video2", "--set-ctrl=contrast={}".format(contrast)]

    try:
        subprocess.run(command, check=True)
        MainWindow.params["contrast"]=contrast
        print("contrast set successfully!")
    except subprocess.CalledProcessError as e:
        print("Error setting contrast:", e)

def set_saturation(MainWindow,ui):

    saturation = int(ui.saturation_textEdit.toPlainText())
    print("new saturation : ", saturation)
    """Runs the v4l2-ctl command to set brightness."""
    # command = ["v4l2-ctl", "--device=/dev/video0", "--set-ctrl=brightness=200"]
    command = ["v4l2-ctl", "--device=/dev/video0", "--set-ctrl=saturation={}".format(saturation)]

    try:
        subprocess.run(command, check=True)
        MainWindow.params["saturation"]=saturation
        print("saturation set successfully!")
    except subprocess.CalledProcessError as e:
        print("Error setting saturation:", e)

    command = ["v4l2-ctl", "--device=/dev/video2", "--set-ctrl=saturation={}".format(saturation)]

    try:
        subprocess.run(command, check=True)
        MainWindow.params["saturation"]=saturation
        print("saturation set successfully!")
    except subprocess.CalledProcessError as e:
        print("Error setting saturation:", e)

def set_gamma(MainWindow,ui):

    gamma = int(ui.gamma_textEdit.toPlainText())
    print("new gamma : ", gamma)
    """Runs the v4l2-ctl command to set brightness."""
    # command = ["v4l2-ctl", "--device=/dev/video0", "--set-ctrl=brightness=200"]
    command = ["v4l2-ctl", "--device=/dev/video0", "--set-ctrl=gamma={}".format(gamma)]

    try:
        subprocess.run(command, check=True)
        MainWindow.params["gamma"]=gamma
        print("gamma set successfully!")
    except subprocess.CalledProcessError as e:
        print("Error setting gamma:", e)

    command = ["v4l2-ctl", "--device=/dev/video2", "--set-ctrl=gamma={}".format(gamma)]

    try:
        subprocess.run(command, check=True)
        MainWindow.params["gamma"]=gamma
        print("gamma set successfully!")
    except subprocess.CalledProcessError as e:
        print("Error setting gamma:", e)

def set_white_balance(MainWindow,ui):

    white_balance_temperature = int(ui.white_balance_textEdit.toPlainText())
    print("new white_balance_temperature : ", white_balance_temperature)
    """Runs the v4l2-ctl command to set brightness."""
    # command = ["v4l2-ctl", "--device=/dev/video0", "--set-ctrl=brightness=200"]
    command = ["v4l2-ctl", "--device=/dev/video0", "--set-ctrl=white_balance_temperature={}".format(white_balance_temperature)]

    try:
        subprocess.run(["v4l2-ctl", "--device=/dev/video0", "--set-ctrl=white_balance_temperature_auto=0"])
        subprocess.run(command, check=True)
        MainWindow.params["white_balance_temperature"]=white_balance_temperature
        print("white_balance_temperature set successfully!")
    except subprocess.CalledProcessError as e:
        print("Error setting white_balance_temperature:", e)

    command = ["v4l2-ctl", "--device=/dev/video2", "--set-ctrl=white_balance_temperature={}".format(white_balance_temperature)]

    try:
        subprocess.run(["v4l2-ctl","--device=/dev/video2", "--set-ctrl=white_balance_temperature_auto=0"])
        subprocess.run(command, check=True)
        MainWindow.params["white_balance_temperature"]=white_balance_temperature
        print("white_balance_temperature set successfully!")
    except subprocess.CalledProcessError as e:
        print("Error setting white_balance_temperature:", e)

    if white_balance_temperature==5000:
        subprocess.run(["v4l2-ctl", "-d", "/dev/video0", "--set-ctrl=white_balance_temperature_auto=1"])
        subprocess.run(["v4l2-ctl", "-d", "/dev/video2", "--set-ctrl=white_balance_temperature_auto=1"])


def item_changed(MainWindow, ui,index):
    MainWindow.params["current_size_index"]=index
    curr_width=MainWindow.params["widthList"][index]
    curr_height=MainWindow.params["heightList"][index]
    MainWindow.params["width"]=curr_width
    MainWindow.params["height"]=curr_height


