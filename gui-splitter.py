import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QFileDialog, QTextEdit
from PySide6.QtGui import QFont, QColor

class FileSplitterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Splitter")
        self.setGeometry(100, 100, 600, 500)
        self.setStyleSheet("background-color: #1a1a1a;")

        self.font = QFont("Arial", 12)

        self.label_file_path = QLabel("Input File:", self)
        self.label_file_path.setFont(self.font)
        self.label_file_path.setStyleSheet("color: #ffffff;")
        self.label_file_path.setGeometry(50, 50, 100, 30)

        self.entry_file_path = QLineEdit(self)
        self.entry_file_path.setFont(self.font)
        self.entry_file_path.setStyleSheet("color: #ffffff; background-color: #333333;")
        self.entry_file_path.setGeometry(180, 50, 300, 30)

        self.button_browse = QPushButton("Browse", self)
        self.button_browse.setFont(self.font)
        self.button_browse.setStyleSheet("color: #ffffff; background-color: #333333;")
        self.button_browse.setGeometry(500, 50, 80, 30)
        self.button_browse.clicked.connect(self.browse_file)

        self.label_part_size = QLabel("Part Size (MB):", self)
        self.label_part_size.setFont(self.font)
        self.label_part_size.setStyleSheet("color: #ffffff;")
        self.label_part_size.setGeometry(50, 100, 130, 30)

        self.entry_part_size = QLineEdit(self)
        self.entry_part_size.setFont(self.font)
        self.entry_part_size.setStyleSheet("color: #ffffff; background-color: #333333;")
        self.entry_part_size.setGeometry(180, 100, 100, 30)

        self.button_split = QPushButton("Split", self)
        self.button_split.setFont(self.font)
        self.button_split.setStyleSheet("color: #ffffff; background-color: #333333;")
        self.button_split.setGeometry(180, 150, 80, 30)
        self.button_split.clicked.connect(self.split_button_click)

        self.log_window = QTextEdit(self)
        self.log_window.setFont(self.font)
        self.log_window.setStyleSheet("color: #ffffff; background-color: #333333;")
        self.log_window.setGeometry(50, 200, 530, 250)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Input File")
        self.entry_file_path.setText(file_path)

    def split_button_click(self):
        input_file = self.entry_file_path.text()
        part_size = self.entry_part_size.text()

        if input_file and part_size:
            self.split_file(input_file, part_size)

    def split_file(self, input_file, part_size):
        self.log_window.clear()
        self.log_window.append("Start...")

        try:
            file_size = os.path.getsize(input_file)
            size_mb = int(part_size)
            part_size_bytes = size_mb * 1024 * 1024
            num_parts = file_size // part_size_bytes + (file_size % part_size_bytes > 0)
            file_dir, file_name = os.path.split(input_file)

            with open(input_file, 'rb') as f:
                part_number = 1
                bytes_written = 0

                while True:
                    chunk = f.read(part_size_bytes)
                    if not chunk:
                        break

                    part_name = f"{file_name}.part{part_number}"
                    output_path = os.path.join(file_dir, part_name)
                    with open(output_path, 'wb') as part_file:
                        part_file.write(chunk)

                    bytes_written += len(chunk)
                    if bytes_written >= file_size:
                        break

                    part_number += 1

                    self.log_window.append(f"Splitting... Part {part_number}/{num_parts}")

            self.log_window.append("Done. File split into parts.")
        except Exception as e:
            self.log_window.append(f"Error: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileSplitterWindow()
    window.show()
    sys.exit(app.exec())
