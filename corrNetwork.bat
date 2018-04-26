@echo off

:: get current path
SET PWD=%~dp0
SET PWD=%PWD:~0,-1%

:: environment variables
SET VENV_HOME=%PWD%/venv_win
SET VENV_ACTIVE=%VENV_HOME%/Scripts/activate

:: input arguments
REM SET PARAM_INFILE=S:\U_Proteomica\PROYECTOS\PESA_omicas\Results_tables_V1\Con_fraccionamiento\Clustering\PESA_V1_Proteinas_RF.xlsx
REM SET PARAM_INFILE=D:\projects\corrNetwork\tests\test1-in.xlsx
REM SET PARAM_METHOD=kendall
REM SET PARAM_OUTFILE=D:\projects\corrNetwork\tests\test1-out_kendall.csv

:: interactive arguments
SET /p PARAM_INFILE="Enter the input file (in XLSX format): "
SET /p PARAM_OUTFILE="Enter the output file (in CSV extension): "
CHOICE /C PSK /N /T 10 /D P /M "Choice the method: Pearson [P], Spearman [S], Kendall [K] (Pearson by default)"
IF ERRORLEVEL 1 SET PARAM_METHOD=pearson
IF ERRORLEVEL 2 SET PARAM_METHOD=spearman
IF ERRORLEVEL 3 SET PARAM_METHOD=kendall

:: execute workflow
CMD /k "%VENV_ACTIVE% && python %PWD%/correlation_network.py -i %PARAM_INFILE% -m %PARAM_METHOD% -o %PARAM_OUTFILE%"

SET /P DUMMY=Hit ENTER to continue...