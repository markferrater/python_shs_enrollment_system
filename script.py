from PyQt6.QtWidgets import QComboBox, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, \
    QPushButton, QGroupBox, QLineEdit
from PyQt6.QtGui import QIcon, QPixmap
import sys

from PyQt6.QtCore import Qt


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        # self.setFixedSize(900, 500)
        self.setFixedSize(1040, 550)
        # self.setGeometry(100,100,1040,550)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Top Part

        top_layout = QHBoxLayout()

        top_layout_logo = QVBoxLayout()
        top_layout_logo_title = QVBoxLayout()

        # Bottom contents Scrollbar
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        scroll_widget = QWidget()
        scroll_widget.setStyleSheet("""
        background-color: #e9f5f9;
        """)

        # Bottom Part

        bottom_layout = QVBoxLayout(scroll_widget)
        bottom_layout.setContentsMargins(40, 0, 40, 0)

        #GrouBox Form

        #GB 1
        for i in range(10):
            group_box = QGroupBox("Information Fillout Form")
            group_box.setStyleSheet("""
                    background-color: white;
                    """)
            group_layout = QHBoxLayout()

            line_edit1 = QLineEdit()
            line_edit2 = QLineEdit()
            line_edit3 = QLineEdit()

            line_edit1.setPlaceholderText('Enter something')
            line_edit2.setPlaceholderText('Enter something')
            line_edit3.setPlaceholderText('Enter something')

            group_layout.addWidget(line_edit1)
            group_layout.addWidget(line_edit2)
            group_layout.addWidget(line_edit3)

            group_box.setLayout(group_layout)
            bottom_layout.addWidget(group_box)

        #GB 2



        #GB 3


        #GB 4


        #GB 5


       # group_box.setLayout(group_layout)
        #bottom_layout.addWidget(group_box)







        label2 = QLabel("Hello From The Bottom\n" * 30)
        label2.setStyleSheet("""
        background-color: #e3fcf6;

        """)
        btn = QPushButton("Submit Form")
        btn.setStyleSheet("""
        background-color: #e3e7fc;
        """)

        bottom_layout.addWidget(btn)
       # bottom_layout.addWidget(label2)
        bottom_layout.addWidget(btn)
        bottom_layout.addStretch()

        scroll.setWidget(scroll_widget)

        main_layout.addLayout(top_layout, 1)
        main_layout.addWidget(scroll, 3)
        # main_layout.addLayout(bottom_layout,3)
        self.setLayout(main_layout)

        # Top Contents logo

        logo_label = QLabel()
        pixmap = QPixmap("img.png")
        logo_label.setPixmap(pixmap)

        # Optional: scale the logo so it fits nicely
        logo_label.setPixmap(
            pixmap.scaled(
                120, 200,  # width, height
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )

        top_layout.addWidget(logo_label)

        # Label part moved to the bottom for the logo to the left

        label1 = QLabel("Hello From The Top")
        label1.setStyleSheet("""background-color: rgb(255, 255, 255);
        padding-left: 110px;
        """)
        top_layout.addWidget(label1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
