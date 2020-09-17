import sys
# Librerías para la interfaz
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QDialog, QPushButton, QTableWidget,
                             QTableWidgetItem, QAbstractItemView, QHeaderView, QMenu,QActionGroup, QAction, QMessageBox)
import back



# Cargar la interfaz
sys.path.append(".")
qtCreatorFile = "interfazQT.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    # Metodo constructor que inicializa todos los controles de la interfaz. 
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        self.InitTable()
        self.btnGenerate.clicked.connect(self.GenerateTable)
        self.btnClean.clicked.connect(self.CleanData)
   
    def CleanData(self):
        self.txtSizeDatagram.setText("")
        self.txtMtu.setText("")
        self.tabla.clearContents()

        
    def GenerateTable(self):
        mtu = self.txtMtu.text()
        datagram = self.txtSizeDatagram.text()






        # Validación, verifica que los datos sean numericos
        if datagram.isnumeric() == False or mtu.isnumeric() == False:
            ms = 'Los datos ingresados son erroneos. Solo se aceptan valores numericos.'
            self.msgError.setText(ms)
            self.CleanData()
            return
        
        self.msgError.setText('')
        
        datos = back.generate_fragments(datagram, mtu)

        if datos is None:
            ms = 'Inconsistencia en los datos. Por favor verifique.'
            self.msgError.setText(ms)
            return

        self.tabla.clearContents()

        row = 0
        for endian in datos:
            self.tabla.setRowCount(row + 1)
            
            idDato = QTableWidgetItem(endian[0])
            idDato.setTextAlignment(4)
            
            self.tabla.setItem(row, 0, idDato)
            self.tabla.setItem(row, 1, QTableWidgetItem(endian[1]))
            self.tabla.setItem(row, 2, QTableWidgetItem(endian[2]))
            self.tabla.setItem(row, 3, QTableWidgetItem(endian[3]))
            self.tabla.setItem(row, 4, QTableWidgetItem(endian[4]))
            self.tabla.setItem(row, 5, QTableWidgetItem(endian[5]))
            self.tabla.setItem(row, 6, QTableWidgetItem(endian[6]))
            row += 1
    
    #Construir la tabla
    def InitTable(self):
        self.tabla = QTableWidget(self)
        # Deshabilitar edición
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Deshabilitar el comportamiento de arrastrar y soltar
        self.tabla.setDragDropOverwriteMode(False)
        # Seleccionar toda la fila
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Seleccionar una fila a la vez
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)
        # Especifica dónde deben aparecer los puntos suspensivos "..." cuando se muestran
        # textos que no encajan
        self.tabla.setTextElideMode(Qt.ElideRight)# Qt.ElideNone
        # Establecer el ajuste de palabras del texto 
        self.tabla.setWordWrap(False)
        # Deshabilitar clasificación
        self.tabla.setSortingEnabled(False)
        # Establecer el número de columnas
        self.tabla.setColumnCount(7)
        # Establecer el número de filas
        self.tabla.setRowCount(0)
        # Alineación del texto del encabezado
        self.tabla.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.tabla.horizontalHeader().setHighlightSections(False)
        # Hacer que la última sección visible del encabezado ocupa todo el espacio disponible
        self.tabla.horizontalHeader().setStretchLastSection(True)
        # Ocultar encabezado vertical
        self.tabla.verticalHeader().setVisible(False)
        # Dibujar el fondo usando colores alternados
        self.tabla.setAlternatingRowColors(True)
        # Establecer altura de las filas
        self.tabla.verticalHeader().setDefaultSectionSize(20)        
        # self.tabla.verticalHeader().setHighlightSections(True)
        nombreColumnas = ( "Longitud fragmento", "0","DF","MF","Offset en binario","Offset en decimal", "4 hexa (16 bits)")
        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tabla.setHorizontalHeaderLabels(nombreColumnas)        
        # Menú contextual
        self.tabla.setContextMenuPolicy(Qt.CustomContextMenu)
        # Establecer ancho de las columnas
        for indice, ancho in enumerate((170, 40,40,40, 160, 160, 160), start=0):
            self.tabla.setColumnWidth(indice, ancho)

        self.tabla.resize(800, 350)
        self.tabla.move(33, 180)

        row = 0
        for endian in range(15):
            self.tabla.setRowCount(row + 1)
            
            idDato = QTableWidgetItem("")
            idDato.setTextAlignment(4)
            
            self.tabla.setItem(row, 0, idDato)
            self.tabla.setItem(row, 1, QTableWidgetItem("") )
            self.tabla.setItem(row, 2, QTableWidgetItem("") )
            self.tabla.setItem(row, 3, QTableWidgetItem("") )
            self.tabla.setItem(row, 4, QTableWidgetItem("") )
            self.tabla.setItem(row, 5, QTableWidgetItem("") )
            self.tabla.setItem(row, 6, QTableWidgetItem("") )
            row += 1

  

# Inicialización de la aplicación gráfica
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
