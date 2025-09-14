@echo off
echo ADB Connection Troubleshooter
echo ============================
echo.

set ADB_PATH=D:\platform-tools-latest-windows\platform-tools\adb.exe

echo Step 1: Killing ADB server...
"%ADB_PATH%" kill-server
echo.

echo Step 2: Starting ADB server...
"%ADB_PATH%" start-server
echo.

echo Step 3: Checking connected devices...
"%ADB_PATH%" devices
echo.

echo Step 4: Testing screenshot capture...
"%ADB_PATH%" exec-out screencap -p > adb_test.png

if exist adb_test.png (
    echo ✅ Screenshot test successful!
    for %%A in (adb_test.png) do echo Screenshot size: %%~zA bytes
    del adb_test.png
) else (
    echo ❌ Screenshot test failed!
)

echo.
echo If you see your device listed above with 'device' status, ADB is working correctly.
echo If you see 'unauthorized', please allow USB debugging on your phone.
echo If no devices are listed, check:
echo - USB cable connection
echo - USB debugging is enabled in Developer Options
echo - Try a different USB port
echo.

pause
