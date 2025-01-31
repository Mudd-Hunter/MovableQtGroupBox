# Import necessary PySide6 modules for UI components
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

# Import the custom draggable group box widget
from widgets.movableQtGroupBox import MovableQtGroupBox


class Dashboard(QWidget):
    def __init__(self, container, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.container = container  # Reference to the parent container (MainWindow)

        # Create the main layout for the Dashboard widget
        main_layout = QVBoxLayout(self)

        # Create an instance of the draggable group box
        self.movable_frame = MovableQtGroupBox("This is the MovableQtGroupBox", parent=self)
        self.movable_frame.setObjectName("movable_frame")  # Set an object name for styling or debugging

        # Create a layout to hold widgets inside the movable group box
        form_layout = QVBoxLayout(self.movable_frame.customGroupBox)

        # Set the layout for the movable frame
        self.movable_frame.setLayout(form_layout)

        # Create a label inside the draggable group box
        self.label1 = QLabel("Hello From The Draggable Screen")
        self.label1.setObjectName("label1")  # Set an object name for potential styling

        # Add the label to the form layout inside the movable frame
        form_layout.addWidget(self.label1)

        # Add the movable group box to the main layout
        main_layout.addWidget(self.movable_frame)

        # Set the main layout for the Dashboard
        self.setLayout(main_layout)
