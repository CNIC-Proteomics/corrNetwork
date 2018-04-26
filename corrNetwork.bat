@echo off

:: get current path
SET PWD=%~dp0
SET PWD=%PWD:~0,-1%

:: environment variables
SET VENV_HOME=%PWD%/venv_win
SET VENV_ACTIVE=%VENV_HOME%/Scripts/activate

:: workflow variables
:: TODO!!!! Interactive inputs
REM SET PARAM_INFILE=S:\U_Proteomica\PROYECTOS\PESA_omicas\Results_tables_V1\Con_fraccionamiento\Clustering\PESA_V1_Proteinas_RF.xlsx
SET PARAM_INFILE=D:\projects\corrNetwork\tests\test1-in.xlsx
SET PARAM_METHOD=kendall
SET PARAM_OUTFILE=D:\projects\corrNetwork\tests\test1-out_kendall.csv

:: interactive arguments
REM SET /p PARAM_INFILE="Enter the input file (in XLSX format):"


:: execute workflow
CMD /k "%VENV_ACTIVE% && python %PWD%/correlation_network.py -i %PARAM_INFILE% -m %PARAM_METHOD% -o %PARAM_OUTFILE%"

SET /P DUMMY=Hit ENTER to continue...