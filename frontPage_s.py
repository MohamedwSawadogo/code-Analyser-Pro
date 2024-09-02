from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QMenu, QWidget
from PySide6.QtGui import QAction
from ui_index import Ui_MainWindow

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")
    #Hide Widget Menu
        self.icon_onky_widget.setHidden(True)    

    #Hide Dropdowns
        self.Analysis_dropdown.setHidden(True)    
        
    #Connect Buttons to switch to different pages
        self.Home_1.clicked.connect(self.switch_to_home_page)
        self.Home_2.clicked.connect(self.switch_to_home_page)

        self.Data_Analysis.clicked.connect(self.switch_to_Data_Analysis_page)
        self.Data_Comparisons.clicked.connect(self.switch_to_Data_Comparisons_page)
        self.References.clicked.connect(self.switch_to_References_page)

        self.Help_1.clicked.connect(self.switch_to_Help_page)
        self.Help_2.clicked.connect(self.switch_to_Help_page)

        self.About_1.clicked.connect(self.switch_to_About_page)
        self.About_2.clicked.connect(self.switch_to_About_page)

        self.Setting_1.clicked.connect(self.switch_to_Setting_page)
        self.Setting_2.clicked.connect(self.switch_to_Setting_page)

    # Connect Buttons to respective context menus
        self.Analysis_1.clicked.connect(self.analysis_context_menu)

        
    #Methods to switch to different pages
    def switch_to_home_page(self):
        self.stackedWidget.setCurrentIndex(0)    

    def switch_to_Data_Analysis_page(self):
        self.stackedWidget.setCurrentIndex(1)    

    def switch_to_Data_Comparisons_page(self):
        self.stackedWidget.setCurrentIndex(2)   

    def switch_to_References_page(self):
        self.stackedWidget.setCurrentIndex(3)    

    def switch_to_Help_page(self):
        self.stackedWidget.setCurrentIndex(4)    
    
    def switch_to_About_page(self):
        self.stackedWidget.setCurrentIndex(5)
    
    def switch_to_Setting_page(self):
        self.stackedWidget.setCurrentIndex(6)

    # Methods to show context menus
    def analysis_context_menu(self):
        self.show_custom_context_menu(self.Analysis_1, ["Data Analysis", "Data Comparisons", "References"])
        

    def show_custom_context_menu(self, button, menu_items):
        menu = QMenu(self)

        #Set style for the menu
        menu.setStyleSheet("""
                           QMenu{
                           background-color: black;
                           color: white;
                           }
                           
                           QMenu: selected{
                           background-color: white;
                           color: #12B298;
                           }
                           """)
        #Add actions to the menu
        for item_text in menu_items:
            action = QAction(item_text, self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)

        #Show the menu
        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()


    
    def handle_menu_item_click(self):

        text = self.sender().text()

        if text == "Data Analysis":
            self.switch_to_Data_Analysis_page()
        elif text == "Data Comparisons":
            self.switch_to_Data_Comparisons_page()
        elif text == "References":
            self.switch_to_References_page()

       