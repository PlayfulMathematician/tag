# File Tagger
## A simple tool to tag files with metadata

This program is designed to tag files with metadata. It can be used to tag a single file, or a directory of files. It has been designed to be as easy to use as possible, and to not require any knowledge of Python.
### Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Development](#development)
4. [Contributing](#contributing)
5. [License](#license)
6. [Authors](#authors)
7. [Acknowledgements](#acknowledgements)
8. [Changelog](#changelog)
### Installation
The program requires Python 3.11 or later. It can be installed using pip:
#### Windows
##### PIP
```bash
py -m pip install file-tagger
```
##### Git
```bash
git clone https://github.io/PlayfulMathematician/tag
```
##### Manual
Download the latest release from the [releases page](https://github.io/PlayfulMathematician/tag/releases), and extract it to a folder of your choice.
#### Linux
##### PIP
```bash
python3 -m pip install file-tagger
```
##### Git
```bash
git clone https://github.io/PlayfulMathematician/tag
```
##### Manual
Download the latest release from the [releases page](https://github.io/PlayfulMathematician/tag/releases), and extract it to a folder of your choice.

### Usage
#### CLI
The program can be run using the CLI:
```bash
tag <file> <tag> <value>
```
##### Examples
```bash
tag test.txt author "PlayfulMathematician"
```
```bash
tag test.txt date "2021-07-17"
```
### Development
#### Building
The program can be built using PyInstaller:
```bash
pyinstaller --onefile --windowed --icon "icon.ico" "tag.py"
```


### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

### License
[MIT](https://choosealicense.com/licenses/mit/)

### Authors
PlayfulMathematician

### Acknowledgements
This program was inspired by MacOS's Finder, which allows you to tag files with colours.

### Changelog
#### 0.1.0
- Initial release