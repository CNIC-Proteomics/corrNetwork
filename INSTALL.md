# Steps to create the Virtual Environment

## Create an installation in a virtual environment, use the following commands

1. Open Powershell or cmd

2.1 Run for Python 3.6 (win64)
```bash
virtualenv.exe -p 'C:\Users\jmrodriguezc\AppData\Local\Programs\Python\Python36\python.exe' python_venv_win
```

<!-- 2.2 Run for Python27 (win64)
```bash
virtualenv.exe -p 'C:\Program Files\Python27\python.exe' python27_venv_win
``` -->


## Active the virtual environment

On Powershell or cmd
```bash
./python_venv_win/Scripts/activate
```
In remote
```bash
//CNIC-27181/python_venv_win/Scripts/activate
```

## Install the python package's using pip

```bash
pip install pandas
pip install logging
...
```
