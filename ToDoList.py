import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

class ToDoList(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        ruta_ui = os.path.join(os.path.dirname(__file__), "ToDoList.ui")
        uic.loadUi(ruta_ui, self)
        
        self.btnAgregar.clicked.connect(self.agregar_tarea)
        self.btnEliminar.clicked.connect(self.eliminar_tarea)
        self.btnEditar.clicked.connect(self.actualizar_tarea)
        self.lstTareas.itemClicked.connect(self.cargar_tarea_select)
        self.editTarea.returnPressed.connect(self.agregar_tarea)

    def _limpiar_campo(self):
        self.editTarea.clear()
        self.editTarea.setFocus()

    def agregar_tarea(self):
        tarea = self.editTarea.text().strip()
        if not tarea:
            QMessageBox.warning(self, "Advertencia", "No se puede agregar una tarea vacía.")
            self._limpiar_campo()
            #papi ye
            return
        self.lstTareas.addItem(tarea)
        self._limpiar_campo()

    def actualizar_tarea(self):
        indice = self.lstTareas.currentRow()
        if indice == -1:
            QMessageBox.warning(self, "Sin selección", "Selecciona una tarea de la lista para editar.")
            return
        nuevo_texto = self.editTarea.text().strip()
        if not nuevo_texto:
            QMessageBox.warning(self,"Texto inválido","No se puede actualizar a una tarea vacía ni contener solo espacios.",)
            self._limpiar_campo()
            return
        
        self.lstTareas.item(indice).setText(nuevo_texto)
        self._limpiar_campo()

    def cargar_tarea_select(self):
        item_selec = self.lstTareas.currentItem()
        if item_selec:
            self.editTarea.setText(item_selec.text())

    def eliminar_tarea(self):
        indice = self.lstTareas.currentRow()
        if indice == -1:
            QMessageBox.warning(self, "Sin selección", "Selecciona una tarea de la lista para eliminar.")
            return
        
        self.lstTareas.takeItem(indice)
        self._limpiar_campo()