@echo off
:: Check for admin rights
openfiles >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting admin privileges...
    powershell -Command "Start-Process -FilePath '%~f0' -Verb runAs"
    exit /b
)

:: Run the Python script
python ""C:\Users\salol\Desktop\rosex.py""

pause
