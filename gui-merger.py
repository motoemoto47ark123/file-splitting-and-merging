import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QFileDialog, QVBoxLayout, QWidget
from PySide6.QtGui import QFont

class FileMergerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Merger")
        self.setGeometry(100, 100, 800, 700)
        self.setStyleSheet("background-color: #1a1a1a;")

        self.font = QFont("Arial", 12)

        self.label_parts = QLabel("Input File Parts:", self)
        self.label_parts.setFont(self.font)
        self.label_parts.setStyleSheet("color: #ffffff;")
        self.label_parts.setGeometry(50, 50, 150, 30)

        self.part_layout = QVBoxLayout()
        self.part_widget = QWidget(self)
        self.part_widget.setLayout(self.part_layout)
        self.part_widget.setGeometry(220, 50, 500, 400)

        self.button_add = QPushButton("+", self)
        self.button_add.setFont(self.font)
        self.button_add.setStyleSheet("color: #ffffff; background-color: #333333;")
        self.button_add.setGeometry(720, 550, 50, 30)
        self.button_add.clicked.connect(self.add_part)

        self.label_output = QLabel("Output File:", self)
        self.label_output.setFont(self.font)
        self.label_output.setStyleSheet("color: #ffffff;")
        self.label_output.setGeometry(50, 500, 120, 30)

        self.entry_output = QLineEdit(self)
        self.entry_output.setFont(self.font)
        self.entry_output.setStyleSheet("color: #ffffff; background-color: #333333;")
        self.entry_output.setGeometry(220, 500, 500, 30)

        self.button_merge = QPushButton("Merge", self)
        self.button_merge.setFont(self.font)
        self.button_merge.setStyleSheet("color: #ffffff; background-color: #333333;")
        self.button_merge.setGeometry(350, 600, 100, 30)
        self.button_merge.clicked.connect(self.merge_button_click)

        self.part_inputs = []

    def add_part(self):
        part_input = QLineEdit(self)
        part_input.setFont(self.font)
        part_input.setStyleSheet("color: #ffffff; background-color: #333333;")
        self.part_layout.addWidget(part_input)

        select_file_button = QPushButton("Select File", self)
        select_file_button.setFont(self.font)
        select_file_button.setStyleSheet("color: #ffffff; background-color: #333333;")
        select_file_button.clicked.connect(self.select_file_button_click)
        self.part_layout.addWidget(select_file_button)

        self.part_inputs.append(part_input)

    def merge_button_click(self):
        input_parts = []
        for part_input in self.part_inputs:
            part_path = part_input.text()
            if part_path:
                input_parts.append(part_path)

        output_file = self.entry_output.text()

        if input_parts and output_file:
            self.merge_files(input_parts, output_file)

    def merge_files(self, input_parts, output_file):
        print('Start...')
        try:
            with open(output_file, 'wb') as output:
                for part in input_parts:
                    with open(part, 'rb') as file:
                        chunk = file.read()
                        output.write(chunk)

                    print(f"Merging... {part}")

            print(f"Done. File saved in {output_file}")
        except Exception as e:
            print(f"Error: {str(e)}")

    def select_file_button_click(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                file_path = file_paths[0]
                button = self.sender()
                index = self.part_layout.indexOf(button)
                part_input = self.part_inputs[index]
                part_input.setText(file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileMergerWindow()
    window.show()
    sys.exit(app.exec())
