@echo off

set "error_level=0"
set "requirements_file=requirements.txt"
set "venv_folder=.venv"
set "install_status=0"

echo Creating virtual environment...
python -m venv "%venv_folder%"
if %errorlevel% NEQ 0 (
    echo Error while creating virtual environment.
    goto :cleanup
)

echo Changing PowerShell execution policy...
powershell -Command "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser"
if %errorlevel% NEQ 0 (
    echo Error while changing PowerShell execution policy.
    goto :cleanup
)

echo Activating virtual environment...
call "%venv_folder%\Scripts\activate.bat"
if %errorlevel% NEQ 0 (
    echo Error while activating virtual environment.
    goto :cleanup
)

echo Upgrading pip to the latest version...
python -m pip install --upgrade pip
if %errorlevel% NEQ 0 (
    echo Error while upgrading pip.
    goto :cleanup
)

if exist "%requirements_file%" (
    echo Installing libraries from %requirements_file%...
    pip install -r "%requirements_file%"
    if %errorlevel% NEQ 0 (
        echo Error while installing libraries.
        set "install_status=1"
    ) else (
        echo Libraries installed.
    )
) else (
    echo %requirements_file% not found. Library installation skipped.
    set "install_status=1"
)

goto :check_install_status

:cleanup
echo Finishing with errors.
goto :eof

:check_install_status
if %install_status%==1 (
    echo Finishing with errors.
) else (
    echo All commands executed successfully.
)