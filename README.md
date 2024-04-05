# Virtual-DataRoom-Generator
VDRgenerator is a tool designed to automate the process of creating a data room folder directory in your computer. It simplifies the often repetitive task of setting up folder structures for virtual data rooms, commonly used in M&A and Private Equity transactions.

## Installation
- If you don't have git installed just follow the 'Downloading the ZIP file' step by step
### Using git
1. Clone the repository:
```
git clone https://github.com/MoustaphaBazzoun/DataRoom-Generator.git
```

2. Navigate to the folder:
Navigate to the folder
```
cd VDRgenerator
```

### Downloading the ZIP file
1. Click on the green "Code" button.

2. Select "Download ZIP".

3. Extract the downloaded ZIP file to your desired location.

4. Open a terminal or command prompt and navigate to the extracted directory.

# Usage
1. Put the excel sheet with the file structure inside the directory 
2. pass the excel file name as a parameter (in this example, we are using duediligence.xlsx)

```
python3 dataroom-generator.py generate vdrStructure.xlsx
```

# Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request