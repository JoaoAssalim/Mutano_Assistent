# Mutano_Assistent

## Dependencies
To install dependencies, runs the following code in your command prompt.
```sh
pip install requirements.txt
```

To creat a executable file on windows, run this code in the project directory:
```sh
pyinstaller --onefile Mutano.py
```
on Linux:
```sh
pyinstaller -F Mutano.py
```

After you run the code, will creat two folders and a file.spec, you just have to keep the dist folder, because there, is the Mutano.exe.
Next, you have to put Mutano.exe in a folder to program creat necessary folders/files, and run the aplication.
