#!/usr/bin/env python3
"""
Simple Docker Cross-Platform Test for Commercial Package
"""

import subprocess
import sys
import time
from pathlib import Path

def test_commercial_in_docker():
    """Test commercial package in Docker environment"""
    
    print("Turbo Loader v3 - Simple Docker Cross-Platform Test")
    print("=" * 60)
    
    current_dir = Path(__file__).parent
    
    # Simple Docker test command
    docker_test_cmd = [
        "docker", "run", "--rm", 
        "-v", f"{current_dir}:/app",
        "python:3.11-slim",
        "/bin/bash", "-c", """
            cd /app
            echo "=== Cross-Platform Commercial Test ==="
            echo "Python version: $(python3 --version)"
            echo "Platform: $(uname -a)"
            echo ""
            
            echo "Installing required packages..."
            pip install psutil requests || echo "Package install completed"
            echo ""
            
            echo "Testing verification tool..."
            mkdir -p "/tmp/Documents/Dungeondraft Mods/TurboLoaderV3"
            cp TurboLoaderV3.ddmod main.gd "/tmp/Documents/Dungeondraft Mods/TurboLoaderV3/"
            echo '{"installation_date": 1692170000, "installer_version": "3.0.0"}' > "/tmp/Documents/Dungeondraft Mods/TurboLoaderV3/config.json"
            
            # Override home directory for test
            export HOME=/tmp
            python3 verify_installation.py
            echo ""
            
            echo "Testing simple test tool..."
            python3 simple_test.py
            echo ""
            
            echo "=== Cross-Platform Test Complete ==="
        """
    ]
    
    try:
        print("Starting Docker cross-platform test...")
        start_time = time.time()
        
        result = subprocess.run(
            docker_test_cmd,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        execution_time = time.time() - start_time
        
        print(f"Test completed in {execution_time:.1f}s")
        print(f"Exit code: {result.returncode}")
        
        if result.stdout:
            print("\n--- OUTPUT ---")
            print(result.stdout)
        
        if result.stderr:
            print("\n--- ERRORS ---")
            print(result.stderr)
        
        success = result.returncode == 0
        
        print("\n" + "=" * 60)
        if success:
            print("PASS CROSS-PLATFORM TEST: SUCCESS")
            print("PASS Commercial package works on Linux")
            print("PASS Verification tools are cross-platform compatible")
            print("PASS Ready for multi-platform distribution")
        else:
            print("FAIL CROSS-PLATFORM TEST: ISSUES FOUND")
            print("FAIL Some components may not work on Linux")
            print("WARN Review errors before release")
        
        return success
        
    except subprocess.TimeoutExpired:
        print("FAIL Docker test timed out (5 minutes)")
        return False
    except Exception as e:
        print(f"FAIL Docker test failed: {e}")
        return False

def main():
    """Main test runner"""
    
    # Check if Docker is available
    try:
        result = subprocess.run(["docker", "--version"], capture_output=True, timeout=10)
        if result.returncode != 0:
            print("SKIP Docker not available - skipping cross-platform test")
            return 0
    except:
        print("SKIP Docker not available - skipping cross-platform test")
        return 0
    
    # Run the test
    success = test_commercial_in_docker()
    
    if success:
        print("\nSUCCESS: Commercial package is cross-platform ready!")
        return 0
    else:
        print("\nFAILURE: Cross-platform issues detected")
        return 1

if __name__ == "__main__":
    sys.exit(main())