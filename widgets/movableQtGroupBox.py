from typing import Optional

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QGroupBox, QPushButton


class MovableQtGroupBox(QGroupBox):
    def __init__(self, title: Optional[str] = None, parent: Optional[QWidget] = None):
        super().__init__(parent)

        # Determines if the widget can be moved
        self.is_movable = True
        self._drag_start_position = None  # Stores the initial position for dragging

        # Layout setup
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins for a clean layout

        # Create a group box for content, with no border
        self.customGroupBox = QGroupBox()
        self.customGroupBox.setStyleSheet("border: none;")

        # Title bar setup (used for dragging and displaying the title)
        self.titleBar = QWidget()
        self.titleBar.setObjectName("titleBar")
        self.titleBar.setFixedHeight(40)  # Set a fixed height for the title bar

        # Layout for the title bar
        self.titleLayout = QHBoxLayout(self.titleBar)
        self.titleLayout.setContentsMargins(5, 0, 5, 0)

        # Lock icon button to toggle movability
        self.lockIcon = QPushButton("🔒", self)
        self.lockIcon.setFixedSize(QSize(24, 24))  # Set button size
        self.lockIcon.clicked.connect(self.toggle_lock)  # Connect click event to toggle lock function
        self.titleLayout.addWidget(self.lockIcon)

        # Title text label
        self.titleBarTitle = QLabel(title)
        self.titleBarTitle.setObjectName("titleBarTitle")
        self.titleLayout.addWidget(self.titleBarTitle)

        self.titleLayout.addStretch()  # Push title to the left and icon to the right

        # Add title bar and content group box to the main layout
        self.main_layout.addWidget(self.titleBar)
        self.main_layout.addWidget(self.customGroupBox)

    def toggle_lock(self):
        """ Toggle between locked and unlocked state. """
        self.is_movable = not self.is_movable  # Reverse the movability state
        self.lockIcon.setText("🔓" if self.is_movable else "🔒")  # Update icon based on state

    # noinspection PyPep8Naming
    def settitleBarTitle(self, text: str):
        """ Set the title of the draggable group box dynamically. """
        self.titleBarTitle.setText(text)
        self.update()

    def mousePressEvent(self, event):
        """ Handle mouse press event to start dragging the widget. """
        if event.button() == Qt.MouseButton.LeftButton and self.is_movable:
            # Calculate offset between mouse click and widget's position
            self._drag_start_position = event.globalPosition().toPoint() - self.pos()
            self.grabMouse()  # Capture mouse events for smooth dragging

    def mouseMoveEvent(self, event):
        """ Handle mouse movement to update the widget's position while dragging. """
        if self._drag_start_position:
            self.move(event.globalPosition().toPoint() - self._drag_start_position)

    def mouseReleaseEvent(self, event):
        """ Handle mouse release event to stop dragging. """
        if self._drag_start_position:
            self.releaseMouse()  # Stop capturing mouse events

        self._drag_start_position = None  # Reset drag position
