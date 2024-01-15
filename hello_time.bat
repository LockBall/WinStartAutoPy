@echo off

:: newline
echo:

echo resetting errorlevel
ver > nul

echo looking for python_ht process
tasklist | findstr /I "python_ht.exe"
if %errorlevel% == 1 (
    echo starting python_ht script
    python_ht C:\from_git\WinStartAutoPy\hello_time.py %* 
) else (
    echo python_ht already running
)