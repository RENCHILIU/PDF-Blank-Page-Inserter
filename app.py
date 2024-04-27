import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyPDF2 import PdfReader, PdfWriter, PageObject


class PDFDropWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)
        self.setWindowTitle('PDF Insert Blank Page')
        self.setGeometry(300, 300, 300, 200)
        layout = QVBoxLayout()
        self.label = QLabel("Drag and Drop PDF Here", self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.lower().endswith('.pdf'):
                self.processPDF(file_path)
                self.label.setText('Processed: ' + file_path)
            else:
                self.label.setText('Not a PDF: ' + file_path)


    def processPDF(self, pdf_path):
        output_path = pdf_path[:-4] + '_modified.pdf'
        reader = PdfReader(pdf_path)
        writer = PdfWriter()

        # Get dimensions of the first page
        first_page = reader.pages[0]
        width = first_page.mediabox[2]  # upper-right x-coordinate
        height = first_page.mediabox[3]  # upper-right y-coordinate

        for page in reader.pages:
            writer.add_page(page)
            # Create a blank page with the same dimensions as the first page
            blank_page = PageObject.create_blank_page(None, width=width, height=height)
            writer.add_page(blank_page)

        with open(output_path, 'wb') as f:
            writer.write(f)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PDFDropWidget()
    ex.show()
    sys.exit(app.exec_())
