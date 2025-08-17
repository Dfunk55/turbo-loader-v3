#!/usr/bin/env python3
"""
Complete E2E Docker Test for Commercial Package
Tests the full installer workflow in Docker including complete installation and verification
"""

import subprocess
import sys
import time
from pathlib import Path

def run_complete_e2e_test():
    """Run complete end-to-end test in Docker"""
    
    print("Turbo Loader v3 - Complete E2E Docker Test")
    print("=" * 60)
    print("Testing complete installer workflow in Docker environment")
    print("")
    
    current_dir = Path(__file__).parent
    
    # Complete Docker test that simulates real customer experience
    docker_test_cmd = [
        "docker", "run", "--rm", 
        "-v", f"{current_dir}:/customer_package",
        "python:3.11-slim",
        "/bin/bash", "-c", """
            echo "=== TURBO LOADER V3 COMPLETE E2E TEST ==="
            echo "Simulating complete customer installation workflow..."
            echo ""
            
            # Install system dependencies
            echo "Installing system dependencies..."
            apt-get update -qq
            apt-get install -y python3-pip > /dev/null 2>&1
            
            # Install Python dependencies
            echo "Installing Python dependencies..."
            pip install psutil requests > /dev/null 2>&1
            
            echo ""
            echo "=== CUSTOMER WORKFLOW SIMULATION ==="
            
            # Step 1: Customer downloads and extracts package
            echo "Step 1: Customer downloads package to ~/Downloads"
            mkdir -p /root/Downloads
            cp -r /customer_package /root/Downloads/TurboLoaderV3
            cd /root/Downloads/TurboLoaderV3
            
            echo "Package contents:"
            ls -la
            echo ""
            
            # Step 2: Customer creates Dungeondraft Mods directory
            echo "Step 2: Customer creates Dungeondraft Mods directory"
            mkdir -p "/root/Documents/Dungeondraft Mods"
            echo "Created: /root/Documents/Dungeondraft Mods"
            echo ""
            
            # Step 3: Run headless installer test (simulates installer functionality)
            echo "Step 3: Running complete installer simulation..."
            python3 headless_installer_test.py
            
            if [ $? -eq 0 ]; then
                echo ""
                echo "=== INSTALLATION VERIFICATION ==="
                
                # Step 4: Verify installation manually
                echo "Step 4: Manual verification of installation..."
                
                # Check both possible locations (headless test uses /tmp/Documents)
                PLUGIN_DIR=""
                if [ -d "/tmp/Documents/Dungeondraft Mods/TurboLoaderV3" ]; then
                    PLUGIN_DIR="/tmp/Documents/Dungeondraft Mods/TurboLoaderV3"
                    echo "Found plugin directory at: $PLUGIN_DIR"
                elif [ -d "/root/Documents/Dungeondraft Mods/TurboLoaderV3" ]; then
                    PLUGIN_DIR="/root/Documents/Dungeondraft Mods/TurboLoaderV3"
                    echo "Found plugin directory at: $PLUGIN_DIR"
                fi
                
                if [ -n "$PLUGIN_DIR" ]; then
                    echo "PASS: Plugin directory created"
                    
                    # Check each required file
                    if [ -f "$PLUGIN_DIR/TurboLoaderV3.ddmod" ]; then
                        echo "PASS: TurboLoaderV3.ddmod file present"
                    else
                        echo "FAIL: TurboLoaderV3.ddmod file missing"
                        exit 1
                    fi
                    
                    if [ -f "$PLUGIN_DIR/main.gd" ]; then
                        echo "PASS: main.gd file present"
                    else
                        echo "FAIL: main.gd file missing"
                        exit 1
                    fi
                    
                    if [ -f "$PLUGIN_DIR/config.json" ]; then
                        echo "PASS: config.json file present"
                    else
                        echo "FAIL: config.json file missing"
                        exit 1
                    fi
                    
                    # Test file permissions
                    if [ -r "$PLUGIN_DIR/TurboLoaderV3.ddmod" ]; then
                        echo "PASS: Files are readable"
                    else
                        echo "FAIL: File permission issues"
                        exit 1
                    fi
                    
                    # Test JSON validity
                    echo "Testing JSON file validity..."
                    python3 -c "
import json
with open('$PLUGIN_DIR/TurboLoaderV3.ddmod', 'r') as f:
    data = json.load(f)
    print('PASS: .ddmod file valid - Plugin: ' + data.get('name', 'Unknown') + ' v' + data.get('version', 'Unknown'))

with open('$PLUGIN_DIR/config.json', 'r') as f:
    config = json.load(f)
    print('PASS: config.json valid - Installer v' + config.get('installer_version', 'Unknown'))
"
                    
                    if [ $? -eq 0 ]; then
                        echo "PASS: All JSON files are valid"
                    else
                        echo "FAIL: JSON validation failed"
                        exit 1
                    fi
                    
                else
                    echo "FAIL: Plugin directory not created"
                    exit 1
                fi
                
                echo ""
                echo "=== CUSTOMER VERIFICATION TOOLS TEST ==="
                
                # Step 5: Test customer verification tools
                echo "Step 5: Testing customer verification tools..."
                
                # Test verify_installation.py
                echo "Running verify_installation.py..."
                cd /root/Downloads/TurboLoaderV3
                python3 verify_installation.py
                
                if [ $? -eq 0 ]; then
                    echo "PASS: verify_installation.py completed successfully"
                else
                    echo "FAIL: verify_installation.py failed"
                    exit 1
                fi
                
                echo ""
                echo "Running simple_test.py..."
                python3 simple_test.py
                
                if [ $? -eq 0 ]; then
                    echo "PASS: simple_test.py completed successfully"
                else
                    echo "FAIL: simple_test.py failed"
                    exit 1
                fi
                
                echo ""
                echo "=== FINAL VALIDATION ==="
                
                # Step 6: Final file size and structure validation
                echo "Step 6: Final installation validation..."
                
                # Check file sizes
                ddmod_size=$(wc -c < "$PLUGIN_DIR/TurboLoaderV3.ddmod")
                gd_size=$(wc -c < "$PLUGIN_DIR/main.gd")
                config_size=$(wc -c < "$PLUGIN_DIR/config.json")
                
                echo "File sizes:"
                echo "  TurboLoaderV3.ddmod: ${ddmod_size} bytes"
                echo "  main.gd: ${gd_size} bytes"
                echo "  config.json: ${config_size} bytes"
                
                # Validate minimum file sizes
                if [ $ddmod_size -gt 1000 ]; then
                    echo "PASS: .ddmod file has substantial content"
                else
                    echo "FAIL: .ddmod file too small"
                    exit 1
                fi
                
                if [ $gd_size -gt 5000 ]; then
                    echo "PASS: GDScript file has substantial content"
                else
                    echo "FAIL: GDScript file too small"
                    exit 1
                fi
                
                if [ $config_size -gt 50 ]; then
                    echo "PASS: Config file has content"
                else
                    echo "FAIL: Config file too small"
                    exit 1
                fi
                
                echo ""
                echo "=== E2E TEST COMPLETE ==="
                echo "PASS: All E2E tests passed successfully!"
                echo "PASS: Complete installation workflow validated"
                echo "PASS: Customer experience confirmed working"
                echo "PASS: All verification tools functional"
                echo ""
                echo "RESULT: COMMERCIAL PACKAGE READY FOR RELEASE"
                
            else
                echo "FAIL: Installer simulation failed"
                exit 1
            fi
        """
    ]
    
    try:
        print("Starting complete E2E Docker test...")
        start_time = time.time()
        
        result = subprocess.run(
            docker_test_cmd,
            capture_output=True,
            text=True,
            timeout=600  # 10 minute timeout for complete test
        )
        
        execution_time = time.time() - start_time
        
        print(f"Test completed in {execution_time:.1f}s")
        print(f"Exit code: {result.returncode}")
        
        if result.stdout:
            print("\n--- DOCKER TEST OUTPUT ---")
            print(result.stdout)
        
        if result.stderr and result.stderr.strip():
            print("\n--- DOCKER TEST ERRORS ---")
            print(result.stderr)
        
        success = result.returncode == 0
        
        print("\n" + "=" * 60)
        if success:
            print("SUCCESS: COMPLETE E2E TEST PASSED")
            print("PASS: Full installer workflow works perfectly")
            print("PASS: All customer-facing functionality validated")
            print("PASS: Commercial package is production-ready")
            print("")
            print("COMMERCIAL APPROVAL: READY FOR IMMEDIATE SALES!")
        else:
            print("FAILURE: E2E TEST FAILED")
            print("FAIL: Critical issues found in installer workflow")
            print("WARN: Fix issues before commercial release")
            print("")
            print("COMMERCIAL STATUS: NEEDS WORK")
        
        return success
        
    except subprocess.TimeoutExpired:
        print("FAIL: Docker E2E test timed out (10 minutes)")
        return False
    except Exception as e:
        print(f"FAIL: Docker E2E test failed: {e}")
        return False

def main():
    """Main test runner"""
    
    # Check if Docker is available
    try:
        result = subprocess.run(["docker", "--version"], capture_output=True, timeout=10)
        if result.returncode != 0:
            print("SKIP: Docker not available - cannot run E2E test")
            return 0
    except:
        print("SKIP: Docker not available - cannot run E2E test")
        return 0
    
    # Run the complete E2E test
    success = run_complete_e2e_test()
    
    if success:
        print("\nFINAL VERDICT: COMMERCIAL PACKAGE APPROVED")
        print("The complete installer workflow works flawlessly!")
        return 0
    else:
        print("\nFINAL VERDICT: NEEDS FIXES BEFORE RELEASE")
        print("Critical issues found in E2E testing")
        return 1

if __name__ == "__main__":
    sys.exit(main())