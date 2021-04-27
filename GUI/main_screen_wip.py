"""
This class handles the building of all GUI elements.

pertaining to the static layout. rb_panel.py handles
page loading on the bottom rightmost panel.

"""

import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from GUI import rb_panel as rbp
from src import search

class MainWindow(qtw.QWidget):
    """Builds the root stage."""
    
    search_result = search.Search()
    left_panel = None
    rt_panel = None
    rb_panel = None

    def __init__(self, hsize, wsize, *args, **kwargs):
        """
        Build the constructor of this class.

        It sets the root layout (var 'layout').

        """
        super().__init__(*args, **kwargs)
        self.resize(int(wsize * 0.5), int(hsize * 0.5))
        self.setStyleSheet("background-color: #1c1c1c;")

        self.left_panel = self.set_left_panel()
        self.rt_panel = self.set_right_tpanel()
        self.rb_panel = self.set_right_bpanel()

        # for _ in range(0, 100):  # for testing purposes only
        #     button = qtw.QPushButton("""
        #     Helllllooooo000000000000000000000000000000000000000000000000000000000000000000000000000000
        #     """)
        #     rb_panel.layout().addWidget(button)

        scroll_area = qtw.QScrollArea()
        scroll_area.setWidget(self.rb_panel)
        scroll_area.setWidgetResizable(True)
        scroll_area.verticalScrollBar().setStyleSheet(
            """
            background-color: powderblue;
            color: black;
        """
        )
        scroll_area.horizontalScrollBar().setStyleSheet(
            """
            background-color: powderblue;
            color: black;
        """
        )

        rpanel = qtw.QWidget()
        rpanel.setStyleSheet("border: 2px solid green;")
        rpanel.setLayout(qtw.QVBoxLayout())
        rpanel.layout().addWidget(self.rt_panel, 0)
        rpanel.layout().addWidget(scroll_area, 7)

        # -- root layout --
        layout = qtw.QHBoxLayout()
        layout.addWidget(self.left_panel, 3)
        layout.addWidget(rpanel, 7)

        self.setLayout(layout)
        

    def set_left_panel(self):
        """Build the left vbox panel."""
        logo = qtw.QLabel(
            pixmap=qtg.QPixmap("GUI/assets/logo_placeholder.png").scaled(
                200, 200
            )
        )
        # logo.setStyleSheet('border: 2px solid red;')
        logo.setAlignment(qtc.Qt.AlignCenter)

        left_panel = qtw.QWidget()
        # left_panel.setStyleSheet('border:2px solid white;')
        left_panel.setLayout(qtw.QVBoxLayout())
        left_panel.setFixedWidth(300)

        menu = qtw.QMenu()
        menu.setContentsMargins(5, 0, 0, 0)
        act1 = qtw.QAction("Vegan", menu)
        act1.setCheckable(True)
        act2 = qtw.QAction("Vegetarian", menu)
        act2.setCheckable(True)
        act3 = qtw.QAction("Pescatarian", menu)
        act3.setCheckable(True)
        act4 = qtw.QAction("Keto", menu)
        act4.setCheckable(True)
        act5 = qtw.QAction("Paleo", menu)
        act5.setCheckable(True)

        menu.addAction(act1)
        menu.addAction(act2)
        menu.addAction(act3)
        menu.addAction(act4)
        menu.addAction(act5)

        dietary_filter = qtw.QPushButton()
        dietary_filter.setMenu(menu)
        dietary_filter.setStyleSheet(
            """
            margin-left: 5px;
            background-color: white;
            """
        )
        dietary_filter.setFixedWidth(25)

        pre = qtw.QLabel()
        pre.setLayout(qtw.QStackedLayout())

        search_bar = qtw.QLineEdit()
        search_bar.setStyleSheet("background-color: white; font-size: 14px;")
        search_bar.setFixedSize(240, 40)
        search_bar.setContentsMargins(20, 0, 20, 0)
        
        list_box = qtw.QListWidget()
        list_box.addItems(self.search_result.search_result_list)
        list_box.setStyleSheet("background-color: white; font-size: 14px; position: absolute; margin-left: 20px;")
        list_box.setFixedWidth(240)
        list_box.setFixedHeight(len(self.search_result.search_result_list)*25)
        list_box.setSpacing(0)
        
        if search_bar.text():
            list_box.setVisible(True)
            self.show()
        else:
            list_box.setVisible(False)
            self.show()
            
        search_button = qtw.QPushButton(
            icon=qtg.QIcon(qtg.QPixmap("GUI/assets/search.png"))
        )
        search_button.setIconSize(qtc.QSize(25, 25))
        search_button.setStyleSheet(
            """
            background-color: transparent;
            margin-top: 1px;
            position: absolute;
        """
        )
        pre.setStyleSheet("background-color: white; margin-top: 1.1px;")
        pre.setFixedSize(qtc.QSize(30, search_bar.height() - 1))
        search_button.setFixedSize(qtc.QSize(30, search_bar.height()))

        search = qtw.QWidget()
        search.setLayout(qtw.QGridLayout())
        # search.setStyleSheet('border: 2px solid red;')
        search.layout().addWidget(search_bar, 0, 0)
        search.layout().addWidget(pre, 0, 2)
        search.layout().addWidget(search_button, 0, 2)
        search.layout().addWidget(list_box, 1, 0)
        search.layout().addWidget(dietary_filter, 0, 3)
        search.layout().setAlignment(qtc.Qt.AlignTop)
        search.layout().setSpacing(0)
        
        

        donate_text = qtw.QLabel(text="DONATE")
        donate_text.setStyleSheet("color: white; font-weight: bold;")
        fb_icon = qtw.QPushButton(
            icon=qtg.QIcon(qtg.QPixmap("GUI/assets/fb_icon.png"))
        )
        fb_icon.setIconSize(qtc.QSize(30, 30))
        fb_icon.setStyleSheet("background: transparent;")
        donate = qtw.QWidget()
        # donate.setStyleSheet('border: 2px solid red')
        donate.setLayout(qtw.QHBoxLayout())
        donate.layout().addWidget(fb_icon, 0)
        donate.layout().addWidget(donate_text, 10)
        donate.setFixedHeight(60)
        donate.layout().setAlignment(qtc.Qt.AlignBottom)

        # !--- run with vs. without margins and pick preference
        logo.setContentsMargins(0, 150, 0, 0)

        left_panel.layout().addWidget(logo)
        left_panel.layout().addWidget(search)
        left_panel.layout().addWidget(donate)
        left_panel.layout().addWidget(list_box)
        left_panel.layout().setSpacing(0)

        return left_panel

    def set_right_tpanel(self):
        """Set top rightmost hbox panel [icon bar]."""
        r_top = qtw.QWidget()
        r_top.setStyleSheet("border:2px solid powderblue;")
        r_top.setLayout(qtw.QHBoxLayout())

        text = qtw.QLabel()
        text.setStyleSheet("border: none; color: white; font-size: 20px")
        favorites_icon = qtw.QPushButton(
            icon=qtg.QIcon(qtg.QPixmap("GUI/assets/fav_icon.png"))
        )
        favorites_icon.setStyleSheet("border: None; margin: auto;")
        # favorites_icon.setStyleSheet('background-color: white;')
        favorites_icon.setFixedSize(40, 30)
        favorites_icon.setIconSize(qtc.QSize(30, 30))

        recipes_icon = qtw.QPushButton(
            icon=qtg.QIcon(qtg.QPixmap("GUI/assets/recipes_icon.png"))
        )
        recipes_icon.setStyleSheet("border: None; margin-top: 4px;")
        # favorites_icon.setStyleSheet('background-color: white;')
        recipes_icon.setFixedSize(40, 30)
        recipes_icon.setIconSize(qtc.QSize(30, 30))

        back_icon = qtw.QPushButton(
            icon=qtg.QIcon(qtg.QPixmap("GUI/assets/back_icon.png"))
        )
        back_icon.setStyleSheet("border: None;")
        # favorites_icon.setStyleSheet('background-color: white;')
        back_icon.setFixedSize(40, 30)
        back_icon.setIconSize(qtc.QSize(30, 30))

        r_top.layout().addWidget(back_icon)
        r_top.layout().addWidget(text)
        r_top.layout().addWidget(favorites_icon)
        r_top.layout().addWidget(recipes_icon)
        return r_top

    # responsive slot method that governs what pages load from the
    # ... rbp.RightBottomPanel() class?
    def set_right_bpanel(self, page="trending"):
        """Set right bottom panel/widget w.r.t. emitted signals/events."""
        rp_bottom = None
        if page.lower() == "trending":
            rp_bottom = rbp.RightBottomPanel().trending_page()
        elif page.lower() == "search_results":
            rp_bottom = rbp.RightBottomPanel().search_results_page()
        elif page.lower() == "favorites":
            rp_bottom = rbp.RightBottomPanel().favorite_page()
        return rp_bottom



