@echo off
echo Adding ADB to Windows PATH permanently...
echo.

REM Add the ADB path to the system PATH
setx PATH "%PATH%;D:\platform-tools-latest-windows\platform-tools" /M

if %errorlevel% == 0 (
    echo SUCCESS: ADB path added to system PATH.
    echo Please restart your command prompt or VS Code to use ADB from anywhere.
) else (
    echo FAILED: Could not add to system PATH. You may need to run as Administrator.
    echo.
    echo Alternative: Add manually through Windows Settings:
    echo 1. Press Win+R, type 'sysdm.cpl', press Enter
    echo 2. Go to Advanced tab → Environment Variables
    echo 3. Under System Variables, find 'Path' and click Edit
    echo 4. Click New and add: D:\platform-tools-latest-windows\platform-tools
    echo 5. Click OK to save
)

echo.
echo Current ADB status:
set PATH=%PATH%;D:\platform-tools-latest-windows\platform-tools
adb version
echo.
echo Connected devices:
adb devices
echo.
pause
