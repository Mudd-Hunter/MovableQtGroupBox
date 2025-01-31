# MovableQtGroupBox Project

## Overview
The MovableQtGroupBox project is a Python-based GUI application that utilizes the PySide6 framework to create a draggable and movable group box widget. This project demonstrates how to create custom widgets with enhanced functionality, such as the ability to move the widget around within a parent container.

## Features
- **Draggable Group Box**: A custom `QGroupBox` that can be moved around within its parent container.
- **Lock/Unlock Movability**: A button to toggle the movability of the group box.
- **Dynamic Title**: The title of the group box can be set dynamically.
- **Customizable Layout**: The group box can contain other widgets and layouts.

## Requirements
- Python 3.7+
- PySide6 6.8.1.1

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/MovableQtGroupBox.git
    cd MovableQtGroupBox
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Run the main application:
    ```sh
    python main.py
    ```

2. The main window will display a dashboard with a movable group box. You can drag the group box around by clicking and holding the title bar. Use the lock icon to toggle the movability of the group box.

## Project Structure
- `main.py`: Entry point of the application.
- `widgets/movableQtGroupBox.py`: Contains the `MovableQtGroupBox` class definition.
- `screens/dashboard.py`: Contains the `Dashboard` class which integrates the `MovableQtGroupBox`.
- `requirements.txt`: Lists the required dependencies for the project.

## Customization
- **Stylesheets**: The project uses QSS files for styling. You can modify the styles in the `resources/_base.qss` and `resources/_dashboard.qss` files.
- **Widgets**: You can add more widgets to the `MovableQtGroupBox` by modifying the `Dashboard` class in `screens/dashboard.py`.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Contact
For any questions or issues, please open an issue on the GitHub repository or contact the project maintainer at your.email@example.com.