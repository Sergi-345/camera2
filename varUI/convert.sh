#!/bin/bash

# Convertir el archivo .ui a .py usando pyuic6
pyuic6 VarUI.ui -o VarUI.py

# Mensaje de éxito
echo "Conversión completada: VarUI.ui → VarUI.py"