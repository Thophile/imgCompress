# imgCompress
## Sommaire

1. [Requirement](#requirement)
2. [Usage](#usage)

## Usage <a name="requirement"></a>

- Python 3 or more is required

- Package PIL may need to be installed

## Usage <a name="usage"></a>

The script will compress **png**, **jpg** and **gif** file in the **current working directory** by default or to the **specified path** if you add the optional argument *--path*

Flag *-r* makes the script recursive (IE. will compress subfolder too)

Please note that if the path is a valide file, only this file will be compressed even if the *-r* flag is present

*Synthax* : 
```bash
# Compress all file in current working directory
~/C/W/D> compress.py
# Compress all file in current working directory and subdirectories
~/C/W/D> compress.py -r
# Compress all file in the specified path / Compress specified file
~ compress.py --path path/to/file/or/folder
# Compress all file in the specified directory and subdirectories / Compress specified file
~ compress.py -r --path path/to/file/or/folder
```
