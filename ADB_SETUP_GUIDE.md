# ADB Setup Guide for YOLO Inference

This guide will help you set up Android Debug Bridge (ADB) to use the ADB inference feature in the YOLO app.

## Step 1: Install ADB (Android Debug Bridge)

### Option A: Download Android Platform Tools (Recommended)
1. Go to https://developer.android.com/studio/releases/platform-tools
2. Download "SDK Platform-Tools for Windows"
3. Extract the zip file to `C:\platform-tools` (or any folder you prefer)
4. Add the folder to your Windows PATH:
   - Press `Win + R`, type `sysdm.cpl`, press Enter
   - Go to "Advanced" tab → "Environment Variables"
   - Under "System Variables", find "Path" and click "Edit"
   - Click "New" and add `C:\platform-tools`
   - Click "OK" to save

### Option B: Using Chocolatey (if you have it installed)
```cmd
choco install adb
```

### Option C: Using Scoop (if you have it installed)
```cmd
scoop install adb
```

## Step 2: Enable Developer Options on Your Android Device

1. Go to **Settings** → **About phone** (or **About device**)
2. Find **Build number** and tap it **7 times**
3. You'll see "Developer mode enabled" message
4. Go back to **Settings** → **Developer options** (or **System** → **Developer options**)
5. Enable **USB debugging**
6. Optional: Enable **Stay awake** (keeps screen on while charging)

## Step 3: Connect Your Android Device

1. Connect your Android device to your computer using a USB cable
2. On your phone, you'll see a popup asking "Allow USB debugging?"
3. Check "Always allow from this computer" and tap "OK"
4. Test the connection by opening Command Prompt and running:
   ```cmd
   adb devices
   ```
5. You should see your device listed with "device" status

## Step 4: Test ADB Screen Capture

Test if ADB can capture screenshots from your device:
```cmd
adb exec-out screencap -p > test_screenshot.png
```

If this works, you should see a `test_screenshot.png` file with your phone's current screen.

## Step 5: Use ADB Inference in the App

1. Make sure your Android device is connected and ADB is working
2. Run the YOLO app: `python app.py`
3. Go to the "ADB" tab
4. Configure your inference settings (confidence, IoU, model, etc.)
5. Click to start the inference - it will continuously capture screenshots from your device and run YOLO detection

## Troubleshooting

### "adb: device unauthorized"
- Make sure you allowed USB debugging on your phone
- Try revoking USB debugging authorizations in Developer Options and reconnect

### "adb: no devices found"
- Check USB cable connection
- Try a different USB port
- Enable "Transfer files" mode on your phone
- Install device drivers if needed

### "adb: device offline"
- Disconnect and reconnect the USB cable
- Restart ADB: `adb kill-server` then `adb start-server`

### App shows black screen or errors
- Make sure your phone screen is on and unlocked
- Check that ADB can capture screenshots using the test command above

## Security Note

USB debugging gives your computer significant access to your Android device. Only enable it on trusted computers and disable it when not needed.
