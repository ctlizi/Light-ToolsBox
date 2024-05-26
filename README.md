<style>
    a {
        color: aquamarine;
        text-underline: None;
    }
</style>
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
<h3>Compiling Dependencies</h3>
[Python3](https://www.python.org/) Installation  
First: `cd your Light-ToolsBox storage path`.  
Library installation: `pip3 install -r requirements.txt`  
Compile: `python3 Light-ToolsBox.py`.  
<h3>Frequently Asked Questions</h3>
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
<h3>Running</h3>
- Open the downloaded release
- Run the .exe
<h3>Frequently Asked Questions</h3>
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
<h3>Functionality</h3>
- Encoding/Decoding
- Encoding: Convert text to base85, base64, base32, base16, etc.
- Decode: convert the encoded text back to the original text.
<h3>Usage</h3>
- The first selection box is used to choose the type of encoding.  
- Enter the text to be encoded or decoded in the input box.  
- Click "Encode" or "Decode" button to encode or decode.  
- Click "Copy" to copy the output text to the clipboard.
- If the encoding format is not standardised, an error will be prompted when decoding and "error" will be displayed in the output box.  
<h3>Frequently Asked Questions</h3>
- Decoding Error
  - Check if the encoding type is correct.
### File (folder) encryption/decryption
- Function
- Use
- Frequently Asked Questions
<h3>Functions</h3>
- Encryption/Decryption
- Encrypt: Encrypt files or folders
- Decrypt: decrypt the encrypted file, the folder can not be decrypted directly, you need to decrypt the file encrypted output .base64 file, in the decompression into a folder.
<h3>Usage</h3>
- The first selection box is used to choose whether to encrypt/decrypt a folder or a file.
- Click "Select" button to choose the file or folder to be encrypted/decrypted.
- Click "Open Button" to open the parent directory of the output file.
- Click "Encrypt" or "Decrypt" button to encrypt/decrypt.
<h3>Frequently Asked Questions</h3>
- Decryption Error
  - Check if the encrypted file is correct.
## Frequently Asked Questions
The font is not correct, please install . /font/cmdysj.ttf font.