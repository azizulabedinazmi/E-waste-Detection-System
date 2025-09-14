import os
import sys
import subprocess
from PIL import Image
from io import BytesIO

# Add the ADB path to the environment for this session
adb_path = r"D:\platform-tools-latest-windows\platform-tools"
if adb_path not in os.environ.get('PATH', ''):
    os.environ['PATH'] = os.environ.get('PATH', '') + ';' + adb_path

def test_adb_connection():
    """Test ADB connection and device status"""
    print("Testing ADB connection...")
    
    try:
        # Test ADB devices
        proc = subprocess.Popen('adb devices', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        
        print(f"ADB devices output:")
        print(stdout.decode())
        
        if stderr:
            print(f"ADB devices errors:")
            print(stderr.decode())
        
        # Test screenshot capture
        print("\nTesting screenshot capture...")
        proc = subprocess.Popen('adb exec-out screencap -p', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        image_bytes, stderr = proc.communicate()
        
        if proc.returncode != 0:
            print(f"Screenshot failed with error: {stderr.decode()}")
            return False
        
        if len(image_bytes) == 0:
            print("Screenshot returned empty data")
            return False
        
        print(f"Screenshot captured successfully: {len(image_bytes)} bytes")
        
        # Try to create PIL image
        try:
            image = Image.open(BytesIO(image_bytes))
            print(f"Image created successfully: {image.size} pixels, mode: {image.mode}")
            
            # Save test image
            image.save("adb_test_screenshot.png")
            print("Test screenshot saved as 'adb_test_screenshot.png'")
            
            return True
        except Exception as e:
            print(f"Failed to create PIL image: {e}")
            return False
            
    except Exception as e:
        print(f"ADB test failed: {e}")
        return False

def test_yolo_inference():
    """Test YOLO inference on captured screenshot"""
    print("\nTesting YOLO inference...")
    
    try:
        from yolo import img_inf
        
        # Load the test screenshot
        image = Image.open("adb_test_screenshot.png")
        print(f"Loaded test image: {image.size}")
        
        # Run YOLO inference
        result = img_inf(image, 0.25, 0.45, 'yolo11n')
        
        print("YOLO inference results:")
        print(f"- Inference time: {result[1]} seconds")
        print(f"- Objects detected: {result[2]}")
        print(f"- Average confidence: {result[3]}")
        print(f"- Objects details: {result[4]}")
        
        # Save result image
        result[0].save("adb_test_result.png")
        print("Result image saved as 'adb_test_result.png'")
        
        return True
        
    except Exception as e:
        print(f"YOLO inference failed: {e}")
        return False

if __name__ == "__main__":
    print("=== ADB + YOLO Test Script ===\n")
    
    # Test ADB connection and screenshot
    if test_adb_connection():
        print("\n✅ ADB connection and screenshot capture working!")
        
        # Test YOLO inference
        if test_yolo_inference():
            print("\n✅ YOLO inference working!")
            print("\n🎉 Everything is working correctly!")
            print("\nYour ADB inference should work in the Gradio app.")
            print("Make sure to:")
            print("1. Keep your Android device screen ON and UNLOCKED")
            print("2. Have something visible on screen for YOLO to detect")
            print("3. Use the 'ADB' tab in the Gradio interface")
        else:
            print("\n❌ YOLO inference failed")
    else:
        print("\n❌ ADB connection or screenshot capture failed")
        print("\nTroubleshooting steps:")
        print("1. Make sure your Android device is connected via USB")
        print("2. Enable USB debugging in Developer Options")
        print("3. Allow USB debugging when prompted on your phone")
        print("4. Make sure your device screen is ON and UNLOCKED")
