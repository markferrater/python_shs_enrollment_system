from PyQt6.QtWidgets import QComboBox, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, \
    QPushButton, QGroupBox, QLineEdit, QMessageBox
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

        # GrouBox Form

        # GB 1
        group_box = QGroupBox("Personal Information")
        group_box_layout = QVBoxLayout()
        group_box.setStyleSheet("""
                    QGroupBox {
                       background-color: white;
                       border: 1px solid #dcdcdc;
                       border-radius: 10px;
                       padding: 10px;
                   }    

                    QGroupBox::title {
                       subcontrol-origin: margin;
                       left: 10px;
                       padding: 0 6px;
                   }


                   }
                           """)
        group_layout1 = QHBoxLayout()

        self.line_edit1 = QLineEdit()
        self.line_edit1.setStyleSheet("""
                   background-color: white;
                   padding: 6px;
                   border: 1px solid #ccc;
                   border-radius: 6px;                          
                   """)

        self.line_edit2 = QLineEdit()
        self.line_edit2.setStyleSheet("""
                   background-color: white;
                   padding: 6px;
                   border: 1px solid #ccc;
                   border-radius: 6px;                          
                   """)

        self.line_edit3 = QLineEdit()
        self.line_edit3.setStyleSheet("""
                   background-color: white;
                   padding: 6px;
                   border: 1px solid #ccc;
                   border-radius: 6px;                          
                   """)

        group_layout2 = QHBoxLayout()

        self.second_line_edit1 = QLineEdit()
        self.second_line_edit1.setStyleSheet("""
                           background-color: white;
                           padding: 6px;
                           border: 1px solid #ccc;
                           border-radius: 6px;
                                                  
                           """)

        self.combo = QComboBox()
        self.combo.setPlaceholderText('Gender')
        self.combo.setStyleSheet("""
                QComboBox {
                    background-color: #fefefe;
                    border: 1px solid #ccc;
                    border-radius: 6px;
                    padding: 6px 20px 6px 6px;

                }
                
                QComboBox QAbstractItemView {
                    border: 1px solid #ccc;
                    selection-background-color: #d6dbfa;
                }
                """)
        self.combo.addItem('Male')
        self.combo.addItem('Female')

        group_layout2.addWidget(self.second_line_edit1, 1)
        group_layout2.addWidget(self.combo, 1)

        self.line_edit1.setPlaceholderText('first name')
        self.line_edit2.setPlaceholderText('middle name')
        self.line_edit3.setPlaceholderText('last name')

        self.second_line_edit1.setPlaceholderText('Date of birth')

        group_layout1.addWidget(self.line_edit1)
        group_layout1.addWidget(self.line_edit2)
        group_layout1.addWidget(self.line_edit3)

        group_box_layout.addLayout(group_layout1)
        group_box_layout.addLayout(group_layout2)

        group_box.setLayout(group_box_layout)

        bottom_layout.addWidget(group_box)

        # GB 2
        contact_info = QGroupBox("Contact information")
        contact_info.setStyleSheet("""
                            QGroupBox {
                               background-color: white;
                               border: 1px solid #dcdcdc;
                               border-radius: 10px;
                               padding: 10px;
                           }    

                            QGroupBox::title {
                               subcontrol-origin: margin;
                               left: 10px;
                               padding: 0 6px;
                           }


                           }
                                   """)
        contact_layout = QHBoxLayout()

        self.contact_edit1 = QLineEdit()
        self.contact_edit1.setStyleSheet("""
                           background-color: white;
                           padding: 6px;
                           border: 1px solid #ccc;
                           border-radius: 6px;                          
                           """)

        self.contact_edit2 = QLineEdit()
        self.contact_edit2.setStyleSheet("""
                           background-color: white;
                           padding: 6px;
                           border: 1px solid #ccc;
                           border-radius: 6px;                          
                           """)
        self.contact_edit1.setPlaceholderText("Email Address")
        self.contact_edit2.setPlaceholderText("Phone Number")

        contact_layout.addWidget(self.contact_edit1)
        contact_layout.addWidget(self.contact_edit2)
        contact_info.setLayout(contact_layout)

        bottom_layout.addWidget(contact_info)

        # GB 3
        address = QGroupBox("Address")
        address_layout = QVBoxLayout()
        address.setStyleSheet("""
                                   QGroupBox {
                                      background-color: white;
                                      border: 1px solid #dcdcdc;
                                      border-radius: 10px;
                                      padding: 10px;
                                  }    

                                   QGroupBox::title {
                                      subcontrol-origin: margin;
                                      left: 10px;
                                      padding: 0 6px;
                                  }


                                  }
                                          """)
        address_layout1 = QHBoxLayout()
        address_layout2 = QHBoxLayout()

        self.address_edit1 = QLineEdit()
        self.address_edit1.setStyleSheet("""
                                  background-color: white;
                                  padding: 6px;
                                  border: 1px solid #ccc;
                                  border-radius: 6px;                          
                                  """)

        self.address_edit2 = QLineEdit()
        self.address_edit2.setStyleSheet("""
                                          background-color: white;
                                          padding: 6px;
                                          border: 1px solid #ccc;
                                          border-radius: 6px;                          
                                          """)

        self.address_edit3 = QLineEdit()
        self.address_edit3.setStyleSheet("""
                                          background-color: white;
                                          padding: 6px;
                                          border: 1px solid #ccc;
                                          border-radius: 6px;                          
                                          """)

        self.address_edit4 = QLineEdit()
        self.address_edit4.setStyleSheet("""
                                          background-color: white;
                                          padding: 6px;
                                          border: 1px solid #ccc;
                                          border-radius: 6px;                          
                                          """)

        self.address_edit1.setPlaceholderText("Street Address")
        self.address_edit2.setPlaceholderText("City")
        self.address_edit3.setPlaceholderText("Provice")
        self.address_edit4.setPlaceholderText("Zip Code")

        address_layout1.addWidget(self.address_edit1)
        address_layout2.addWidget(self.address_edit2)
        address_layout2.addWidget(self.address_edit3)
        address_layout2.addWidget(self.address_edit4)

        address.setLayout(address_layout)
        address_layout.addLayout(address_layout1)
        address_layout.addLayout(address_layout2)
        bottom_layout.addWidget(address)

        # GB 4
        guardian = QGroupBox("Guardian Information")
        guardian_layout = QHBoxLayout()
        guardian.setStyleSheet("""
                                           QGroupBox {
                                              background-color: white;
                                              border: 1px solid #dcdcdc;
                                              border-radius: 10px;
                                              padding: 10px;
                                          }    

                                           QGroupBox::title {
                                              subcontrol-origin: margin;
                                              left: 10px;
                                              padding: 0 6px;
                                          }


                                          }
                                                  """)

        self.guardian_edit1 = QLineEdit()
        self.guardian_edit1.setStyleSheet("""
                                          background-color: white;
                                          padding: 6px;
                                          border: 1px solid #ccc;
                                          border-radius: 6px;                          
                                          """)

        self.guardian_edit2 = QLineEdit()
        self.guardian_edit2.setStyleSheet("""
                                                  background-color: white;
                                                  padding: 6px;
                                                  border: 1px solid #ccc;
                                                  border-radius: 6px;                          
                                                  """)

        self.guardian_combo = QComboBox()
        self.guardian_combo.setPlaceholderText('Relation')
        self.guardian_combo.setStyleSheet("""
                        QComboBox {
                            background-color: #fefefe;
                            border: 1px solid #ccc;
                            border-radius: 6px;
                            padding: 6px 20px 6px 6px;

                        }

                        QComboBox QAbstractItemView {
                            border: 1px solid #ccc;
                            selection-background-color: #d6dbfa;
                        }
                        """)
        self.guardian_combo.addItem('Father')
        self.guardian_combo.addItem('Mother')
        self.guardian_combo.addItem('Legal Guardian')
        self.guardian_combo.addItem('Others')

        self.guardian_edit1.setPlaceholderText('Guardian Name')
        self.guardian_edit2.setPlaceholderText('Guardian Phone Number')

        guardian_layout.addWidget(self.guardian_edit1, 1)
        guardian_layout.addWidget(self.guardian_edit2, 1)
        guardian_layout.addWidget(self.guardian_combo, 1)

        guardian.setLayout(guardian_layout)

        bottom_layout.addWidget(guardian)

        # GB 5
        academic = QGroupBox("Academic Information")
        academic_layout = QVBoxLayout()
        academic.setStyleSheet("""
                                                   QGroupBox {
                                                      background-color: white;
                                                      border: 1px solid #dcdcdc;
                                                      border-radius: 10px;
                                                      padding: 10px;
                                                  }    

                                                   QGroupBox::title {
                                                      subcontrol-origin: margin;
                                                      left: 10px;
                                                      padding: 0 6px;
                                                  }


                                                  }
                                                          """)

        academic_layout1 = QHBoxLayout()
        academic_layout2 = QHBoxLayout()

        self.academic_edit1 = QLineEdit()
        self.academic_edit1.setStyleSheet("""
                                                          background-color: white;
                                                          padding: 6px;
                                                          border: 1px solid #ccc;
                                                          border-radius: 6px;                          
                                                          """)

        self.academic_combo = QComboBox()
        self.academic_combo.setPlaceholderText('Strand')
        self.academic_combo.setStyleSheet("""
                                QComboBox {
                                    background-color: #fefefe;
                                    border: 1px solid #ccc;
                                    border-radius: 6px;
                                    padding: 6px 20px 6px 6px;

                                }

                                QComboBox QAbstractItemView {
                                    border: 1px solid #ccc;
                                    selection-background-color: #d6dbfa;
                                }
                                """)
        self.academic_combo.addItem('STEM (Science, Technology, Engineering, Math)')
        self.academic_combo.addItem('ABM (Accountancy, Business, Management)')
        self.academic_combo.addItem('GAS (General Academic Strand)')
        self.academic_combo.addItem('HUMSS (Humanities and Social Sciences)')
        self.academic_combo.addItem('TVL (Technical-Vocational-Livelihood)')
        self.academic_combo.addItem('Arts and Design Track')

        self.academic_combo2 = QComboBox()
        self.academic_combo2.setPlaceholderText('Semester`')
        self.academic_combo2.setStyleSheet("""
                                        QComboBox {
                                            background-color: #fefefe;
                                            border: 1px solid #ccc;
                                            border-radius: 6px;
                                            padding: 6px 20px 6px 6px;

                                        }

                                        QComboBox QAbstractItemView {
                                            border: 1px solid #ccc;
                                            selection-background-color: #d6dbfa;
                                        }
                                        """)
        self.academic_combo2.addItem('1st Semester')
        self.academic_combo2.addItem('2st Semester')


        self.academic_combo3 = QComboBox()
        self.academic_combo3.setPlaceholderText('School Year')
        self.academic_combo3.setStyleSheet("""
                                        QComboBox {
                                            background-color: #fefefe;
                                            border: 1px solid #ccc;
                                            border-radius: 6px;
                                            padding: 6px 20px 6px 6px;

                                        }

                                        QComboBox QAbstractItemView {
                                            border: 1px solid #ccc;
                                            selection-background-color: #d6dbfa;
                                        }
                                        """)
        self.academic_combo3.addItem('2025 - 2026')
        self.academic_combo3.addItem('2026 - 2027')


        self.academic_edit1.setPlaceholderText('Previous School')

        academic_layout1.addWidget(self.academic_edit1, 1)
        academic_layout2.addWidget(self.academic_combo, 1)
        academic_layout2.addWidget(self.academic_combo2, 1)
        academic_layout2.addWidget(self.academic_combo3, 1)

        academic_layout.addLayout(academic_layout1)
        academic_layout.addLayout(academic_layout2)
        academic.setLayout(academic_layout)

        bottom_layout.addWidget(academic)

        # ============ Getting Data ==============

        #line edits

        # combo boxes









        # group_box.setLayout(group_layout)
        # bottom_layout.addWidget(group_box)

        label2 = QLabel("Hello From The Bottom\n" * 30)
        label2.setStyleSheet("""
        background-color: #e3fcf6;

        """)
        btn = QPushButton("Submit Form")
        btn.clicked.connect(self.submit_form)
        btn.setStyleSheet("""
        QPushButton {
                background-color: #e3e7fc;
                padding: 10px;
                border-radius: 8px;
                font-size: 14px;
            }
        
        QPushButton:hover {
        background-color: #d6dbfa;
            }
        """)

        bottom_layout.addWidget(btn)
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

    def submit_form(self):
        # Personal Info
        first_name = self.line_edit1.text()
        last_name = self.line_edit3.text()
        dob = self.second_line_edit1.text()
        gender = self.combo.currentText()

        # Contact Info
        email = self.contact_edit1.text()
        phone = self.contact_edit2.text()

        # Guardian Info
        guardian_name = self.guardian_edit1.text()
        guardian_phone = self.guardian_edit2.text()
        guardian_relation = self.guardian_combo.currentText()

        # Academic Info
        prev_school = self.academic_edit1.text()
        strand = self.academic_combo.currentText()
        semester = self.academic_combo2.currentText()
        school_year = self.academic_combo3.currentText()

        # Validation check
        if (not first_name or not last_name or not dob or
                gender == "Gender" or not email or not phone or
                not guardian_name or not guardian_phone or guardian_relation == "Relation" or
                not prev_school or strand == "Strand" or semester == "Semester`" or school_year == "School Year"):
            # Show warning message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setWindowTitle("Form Incomplete")
            msg.setText("Please fill in all required fields before submitting.")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()

            return  # stop execution if form is incomplete

        # If everything is filled
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Form Submitted")
        msg.setText("Form submitted successfully!")
        msg.exec()

        # You can also print or store data here
        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("DOB:", dob)
        print("Gender:", gender)
        print("Email:", email)
        print("Phone:", phone)
        print("Guardian Name:", guardian_name)
        print("Guardian Phone:", guardian_phone)
        print("Guardian Relation:", guardian_relation)
        print("Previous School:", prev_school)
        print("Strand:", strand)
        print("Semester:", semester)
        print("School Year:", school_year)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
