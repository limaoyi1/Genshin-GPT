@echo off

REM Change directory to Myvenv/Scripts/
cd .\Myvenv\Scripts\

REM Activate the virtual environment
activate

REM Change directory back two levels (to the parent directory)
cd ../../

REM Run the Python application
nohup python application.py > output.log 2>&1 &