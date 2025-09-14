@echo off
echo YOLO ADB Setup Helper
echo ====================
echo.

echo Checking if ADB is already installed...
adb version >nul 2>&1
if %errorlevel% == 0 (
    echo ADB is already installed!
    adb version
    echo.
    goto :check_devices
)

echo ADB is not installed or not in PATH.
echo.
echo To use ADB inference, you need to install Android Platform Tools.
echo.
echo Please follow these steps:
echo 1. Download Android Platform Tools from:
echo    https://developer.android.com/studio/releases/platform-tools
echo.
echo 2. Extract the zip file to C:\platform-tools
echo.
echo 3. Add C:\platform-tools to your Windows PATH:
echo    - Press Win+R, type 'sysdm.cpl', press Enter
echo    - Go to Advanced tab → Environment Variables
echo    - Under System Variables, find 'Path' and click Edit
echo    - Click New and add: C:\platform-tools
echo    - Click OK to save
echo.
echo 4. Restart Command Prompt and run this script again
echo.
goto :end

:check_devices
echo Checking for connected Android devices...
adb devices
echo.
echo If no devices are listed:
echo 1. Connect your Android device via USB
echo 2. Enable Developer Options (tap Build Number 7 times in About Phone)
echo 3. Enable USB Debugging in Developer Options
echo 4. Allow USB debugging when prompted on your phone
echo.
echo Test screenshot capture:
echo adb exec-out screencap -p ^> test_screenshot.png
echo.

:end
echo See ADB_SETUP_GUIDE.md for detailed instructions.
pause
