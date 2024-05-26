# Light-ToolsBox
[English](./README.md) | [中文简体](./README-zh-CN.md)
## README
A [Python3](https://www.python.org/) based toolkit with many widgets.
![preview](./pic/preview.png)
## make use of Light-ToolsBox
- Source code compilation
- release run
### Source code compilation
- Compiling Dependencies
- Frequently Asked Questions
### Compiling Dependencies
[Python3](https://www.python.org/) Installation  
First: `cd your Light-ToolsBox storage path`.  
Library installation: `pip3 install -r requirements.txt`  
Compile: `python3 Light-ToolsBox.py`.  
### Frequently Asked Questions
- Run error.
  - Check if Python 3 is installed.
  - Check if dependent libraries are installed.
  - Check if pip3 is installed when Python3 is installed.
  - Check if running in Light-ToolsBox directory.
  - Check for missing files.
  - Check for file format.
### release run
- Run
- Frequently Asked Questions
### Running
- Open the downloaded release
- Run the .exe
### Frequently Asked Questions
- Run error
  - Check if you are running in the Light-ToolsBox directory.
  - Check for missing files
  - Check file format
## Tools
- base Encode/Decode
- File (folder) encryption/decryption
### base encode/decode
- Function
- Use
- Frequently Asked Questions
### Functionality
- Encoding/Decoding
- Encoding: Convert text to base85, base64, base32, base16, etc.
- Decode: convert the encoded text back to the original text.
### Usage
- The first selection box is used to choose the type of encoding.  
- Enter the text to be encoded or decoded in the input box.  
- Click "Encode" or "Decode" button to encode or decode.  
- Click "Copy" to copy the output text to the clipboard.
- If the encoding format is not standardised, an error will be prompted when decoding and "error" will be displayed in the output box.  
### Frequently Asked Questions
- Decoding Error
  - Check if the encoding type is correct.
### File (folder) encryption/decryption
- Function
- Use
- Frequently Asked Questions
### Functions
- Encryption/Decryption
- Encrypt: Encrypt files or folders
- Decrypt: decrypt the encrypted file, the folder can not be decrypted directly, you need to decrypt the file encrypted output .base64 file, in the decompression into a folder.
### Usage
- The first selection box is used to choose whether to encrypt/decrypt a folder or a file.
- Click "Select" button to choose the file or folder to be encrypted/decrypted.
- Click "Open Button" to open the parent directory of the output file.
- Click "Encrypt" or "Decrypt" button to encrypt/decrypt.
### Frequently Asked Questions
- Decryption Error
  - Check if the encrypted file is correct.
## Frequently Asked Questions
The font is not correct, please install ./font/cmdysj.ttf font.
