import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
# Import necessary PySide6 modules for GUI components
from PySide6.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QStackedWidget

from screens.dashboard import Dashboard  # Import the Dashboard screen


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.setWindowIcon(QIcon('../icons/custom_logo1.png'))

        # Create an instance of the Dashboard screen, passing 'self' as the container
        self.dashboard = Dashboard(container=self)

        # Set the directory for the qss files
        STYLE_DIR = os.path.dirname(os.path.abspath(__file__))

        # Defne the paths to the QSS (stylesheet) files
        self.base_application_stylesheet = os.path.join(STYLE_DIR, './resources/_base.qss')
        self.dashboard_screen_stylesheet = os.path.join(STYLE_DIR, './resources/_dashboard.qss')

        # Set up the central widget for the main window
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Use a horizontal layout to organize widgets
        self.layout = QHBoxLayout(self.central_widget)

        # Create a stacked widget to manage multiple screens
        self.container = QStackedWidget(self)
        self.layout.addWidget(self.container)

        # Add the dashboard screen to the container and set it as the current view
        self.container.addWidget(self.dashboard)
        self.container.setCurrentWidget(self.dashboard)

        # Apply the QSS stylesheets
        self.apply_stylesheets('base')
        self.apply_stylesheets('dashboard')

    def apply_stylesheets(self, style_type):
        """ Applies the corresponding stylesheet based on the style_type parameter. """
        style_files = {
            'base': self.base_application_stylesheet,
            'dashboard': self.dashboard_screen_stylesheet,
        }

        if style_type in style_files:
            style_file = style_files[style_type]

            # Check if the specified stylesheet file exists
            if os.path.exists(style_file):
                with open(style_file, 'r') as f:
                    style = f.read()

                    # Apply the styles appropriately
                    if style_type == 'base':
                        self.setStyleSheet(style) # Set base styles
                    elif style_type == 'dashboard':
                        current_style = self.styleSheet()
                        self.setStyleSheet(current_style + "\n" + style) # Append dashboard styles

# Entry point for the application
if __name__ == '__main__':
    app = QApplication(sys.argv) # Initialize the application
    window = MainWindow() # Create the main window
    window.show() # Show the window
    app.exec() # Start the event loop