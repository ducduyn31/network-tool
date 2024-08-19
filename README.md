# Project Setup Guide

## Prerequisites
Before setting up this project, ensure you have the following installed on your system:
- Python (version 3.6 or higher)
- Poetry (version 1.1.0 or higher)

## Installation Steps
Follow these steps to set up the project using Poetry:

1. **Clone the Repository**
    First, clone the repository to your local machine:
    ```bash
    git clone https://github.com/ducduyn31/network_activity_stream.git
    cd network-activity-stream
    ```

2. **Install Poetry**
    If you haven't installed Poetry yet, you can do so by following the instructions on the [official Poetry website](https://python-poetry.org/docs/#installation). For convenience, here's a quick command for Unix-based systems:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. **Install Project Dependencies**
    With Poetry installed, you can now install the project dependencies:
    ```bash
    poetry install
    ```

4. **Activate the Virtual Environment**
    Poetry automatically creates a virtual environment for your project. You can activate it using:
    ```bash
    poetry shell
    ```

5. **Run the Application**
    Once the virtual environment is activated and dependencies are installed, you can run the application using:
    ```bash
    python -m network_activity_stream.main
    ```
   Or you can run with this shortcut from poetry (after `poetry install`):
    ```bash
   network-capture -i <your_1st_interface> <your_second_interface> ...
    ``` 
6. **Build the Application**
    If you want to build the application, you can use the following command:
    ```bash
   poetry run pyinstaller --name network-capture --onefile network_activity_stream/main.py
    ```
   Or you can use the shortcut (after `poetry install`):
    ```bash
   build-network-capture
    ```
    The executable file will be in the `dist` folder.

## TODO:
- [ ] Save report to csv file
- [ ] Stream network activity to datalake
