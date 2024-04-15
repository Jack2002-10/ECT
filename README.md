# ECT Scanner Data Processing and Graphics Presentation

# Overview

Eddy Current Testing (ECT) is a way to test surface defects without destroying the material’s original structure. This GitHub project is designed to show the code for data processing and graphics presentation. Traditionally, only impedance against time graph could be drawn. In this project, impedance against distance is successfully achieved. Changing the x-axis from time to distance can help locate the defect more easily. The code of how this is realised is shown here.

![Fig 1. Defect Sample with Defect Presentation from Software](ECT%20Scanner%20Data%20Processing%20and%20Graphics%20Presentat%20a58ef996bd994fe1b6b8ed074b784b31/defect_comparison.png)

Fig 1. Defect Sample with Defect Presentation from Software

# User Installation Instructions

## 1. Install Python Interprenter

To install the Python interpreter, follow the instructions below:

1. Visit the official Python website at '[https://www.python.org/](https://www.python.org/)'.
2. Hover over the 'Downloads' tab and click on the version of Python that corresponds to your operating system (Windows, MacOS, or Linux/UNIX).
3. Once the download is complete, open the installer.
4. During the installation, make sure to check the box that says "Add Python to PATH" before clicking 'Install Now'.
5. After the installation is complete, you can confirm that Python was successfully installed by opening a command prompt (Windows) or terminal (MacOS, Linux) and typing 'python --version'. This should display the version of Python that you installed.

Note: Python 3.x is recommended for this project as Python 2.x is no longer maintained.

## 2. Install Python libraries

Several Python libraries need to be installed first to run programs smoothly. The following are some examples of how to install these libraries on Windows.

### Installing matplotlib on Windows:

1. Open Command Prompt by searching for `cmd` in the start menu.
2. Once the Command Prompt is open, type the following command and press Enter:

```
pip install matplotlib
```

1. The installation process will begin. It may take a few minutes to install matplotlib, depending on your internet speed. Once the installation is complete, you should see a message that says, "Successfully installed matplotlib".

### Installing seaborn on Windows:

1. Open Command Prompt by searching for `cmd` in the start menu.
2. Once the Command Prompt is open, type the following command and press Enter:

```
pip install seaborn
```

1. The installation process will begin. Depending on your internet speed, it may take a few minutes to install Seaborn. Once the installation is complete, you should see a message that says, "Successfully installed Seaborn.”

### Installing pandas on Windows:

1. Open Command Prompt by searching for `cmd` in the start menu.
2. Once the Command Prompt is open, type the following command and press Enter:

```
pip install pandas
```

1. The installation process will begin. Depending on your internet speed, it may take a few minutes to install pandas. Once the installation is complete, you should see a message saying, "Successfully installed pandas.”

Note: If you are using a Python version older than 3.4, `pip` might not be installed by default. In this case, you can install `pip` by downloading the `get-pip.py` file from the official pip website and running it with Python.

## 3. Download the GitHub Python project

To download the project files, follow the instructions below:

1. Visit the GitHub repository page for the project.
2. Click on the 'Code' button and then click 'Download ZIP'.
3. Once the download is complete, locate the ZIP file on your computer and unzip it. This will create a new folder that contains all the files from the Github repository.

Ensure that you have saved and unzipped the files in a location you can easily access, as you will need to navigate to this folder in the command prompt or terminal to run the Python program.

## 4. Version Explanation

There are three versions kept inside this project: Version 1 Initial Scatter Version, Version 2 Advanced Scatter Version, and Version 3 Heatmap Version. Here’s a detailed explanation of each.

### 1. Version 1 Initial Scatter Version

This version shows the scatter plot of the impedance against the distance diagram. It is very straightforward. However, the defect cannot be seen very clearly from the diagram.

To run this program, double-click on the file named “Version 1 Initial Scatter Version.py”, and it should pop up the diagram the following:

![Fig 2. *Version 1 Scatter Plot – real impedance against distance*](ECT%20Scanner%20Data%20Processing%20and%20Graphics%20Presentat%20a58ef996bd994fe1b6b8ed074b784b31/Untitled.png)

Fig 2. *Version 1 Scatter Plot – real impedance against distance*

### 2. Version 2 Advanced Scatter Version

To solve the previous problem of contrast between normal surface and defect, an offset is subtracted from all the impedance data in this version. This can make the defect more easily identifiable. 

To run this program, double-click on the file named “Version 2 Advanced Scatter Version.py”, and it should pop up the diagram the following:

![*Fig 3. Version 2 Scatter Plot with offset subtraction – real impedance against distance*](ECT%20Scanner%20Data%20Processing%20and%20Graphics%20Presentat%20a58ef996bd994fe1b6b8ed074b784b31/Untitled%201.png)

*Fig 3. Version 2 Scatter Plot with offset subtraction – real impedance against distance*

### 3. Version 3 Heatmap Version

To reduce the gaps between adjacent samples on the x-axis, the version 3 heatmap is being developed. This can perfectly illustrate the relative position between the defect and the normal surface. 

To run this program, double-click on the file named “Version 3 Heatmap Version” and it should pop up the diagram of the following:

![Fig 4. *Version 3 Heatmap – real impedance against distance*](ECT%20Scanner%20Data%20Processing%20and%20Graphics%20Presentat%20a58ef996bd994fe1b6b8ed074b784b31/Untitled%202.png)

Fig 4. *Version 3 Heatmap – real impedance against distance*

Note:
There should be two diagrams popped up after each time you run the program, however, attention should be paid to the real impedance against distance as this one shows a better defect distribution.

# More technical detail

If you wish to run a different set of data rather than the sample one, you may change the file name of the scanner data at the following line:

```jsx
filename = "test_0322.json" # change the filename to the scanner data output
```

The processing_sample_4.py, processing_sample_5.py and processing_sample_6.py provides initial data conditioning for each of the program written. These programs are imported as a library to change the scanner raw data into x, y and z axis coordinates, helping plot data for the next stage.

# Future Improvements

Rather than default selecting the first data samples as offset, future programs may allow users to choose which point they want to be the group of their offset values.

Also, artificial intelligence (AI) can be incorporated into the program to help identify and label the defects. This could further increase the program’s ease of operation.

