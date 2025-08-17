#!/usr/bin/env python3
"""
Turbo Loader v3 - Quick Installation Verification
Lightweight verification script for post-installation validation
"""

import os
import sys
import json
import time
import platform
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class QuickVerification:
    """Quick installation verification for end users"""
    
    def __init__(self):
        self.os_name = platform.system()
        self.plugin_directory = self._find_plugin_directory()
        
    def _find_plugin_directory(self) -> Optional[Path]:
        """Find the Turbo Loader v3 plugin directory"""
        documents = Path.home() / "Documents"
        plugin_path = documents / "Dungeondraft Mods" / "TurboLoaderV3"
        
        return plugin_path if plugin_path.exists() else None
    
    def verify(self) -> Dict[str, any]:
        """Perform quick verification"""
        
        print("Turbo Loader v3 - Quick Installation Verification")
        print("=" * 55)
        
        if not self.plugin_directory:
            return {
                "success": False,
                "error": "Plugin directory not found",
                "message": "Turbo Loader v3 is not installed or not in the expected location"
            }
        
        print(f"Plugin Directory: {self.plugin_directory}")
        
        # Core verification checks
        checks = [
            (" Required Files", self._check_required_files),
            (" Configuration", self._check_configuration),
            (" Mod Definition", self._check_ddmod_file),
            (" GDScript Code", self._check_gdscript),
            (" Permissions", self._check_permissions)
        ]
        
        results = []
        all_passed = True
        
        for check_name, check_function in checks:
            print(f"\n{check_name}:")
            
            try:
                passed, message, details = check_function()
                status = "PASS PASS" if passed else "FAIL FAIL"
                print(f"  {status}: {message}")
                
                results.append({
                    "check": check_name,
                    "passed": passed,
                    "message": message,
                    "details": details
                })
                
                if not passed:
                    all_passed = False
                    
            except Exception as e:
                print(f"  FAIL ERROR: {e}")
                results.append({
                    "check": check_name,
                    "passed": False,
                    "message": f"Check failed with error: {e}",
                    "details": None
                })
                all_passed = False
        
        # Summary
        print("\n" + "=" * 55)
        if all_passed:
            print(" VERIFICATION SUCCESSFUL!")
            print("PASS Turbo Loader v3 is correctly installed and ready to use")
            print("\nNext Steps:")
            print("  1. Start Dungeondraft")
            print("  2. Go to Tools > Mods")
            print("  3. Enable 'Turbo Loader v3'")
            print("  4. Enjoy improved performance!")
        else:
            print("WARN  VERIFICATION ISSUES FOUND")
            print("FAIL Some issues were detected with the installation")
            print("   Please review the details above and retry installation if needed")
        
        return {
            "success": all_passed,
            "plugin_directory": str(self.plugin_directory),
            "checks": results,
            "timestamp": time.time()
        }
    
    def _check_required_files(self) -> Tuple[bool, str, Dict]:
        """Check that all required files are present"""
        required_files = [
            "TurboLoaderV3.ddmod",
            "main.gd",
            "config.json"
        ]
        
        missing_files = []
        found_files = []
        
        for file_name in required_files:
            file_path = self.plugin_directory / file_name
            if file_path.exists():
                found_files.append(file_name)
            else:
                missing_files.append(file_name)
        
        if missing_files:
            return False, f"Missing files: {', '.join(missing_files)}", {
                "missing": missing_files,
                "found": found_files
            }
        else:
            return True, f"All {len(required_files)} required files present", {
                "found": found_files
            }
    
    def _check_configuration(self) -> Tuple[bool, str, Dict]:
        """Check configuration file"""
        config_path = self.plugin_directory / "config.json"
        
        if not config_path.exists():
            return False, "Configuration file not found", {}
        
        try:
            with open(config_path, 'r') as f:
                config_data = json.load(f)
            
            # Check for expected fields
            expected_fields = ["installation_date", "installer_version"]
            missing_fields = [field for field in expected_fields if field not in config_data]
            
            if missing_fields:
                return False, f"Configuration missing fields: {', '.join(missing_fields)}", {
                    "config_data": config_data,
                    "missing_fields": missing_fields
                }
            else:
                return True, "Configuration is valid", {
                    "installer_version": config_data.get("installer_version"),
                    "installation_date": config_data.get("installation_date")
                }
                
        except json.JSONDecodeError:
            return False, "Configuration file contains invalid JSON", {}
        except Exception as e:
            return False, f"Error reading configuration: {e}", {}
    
    def _check_ddmod_file(self) -> Tuple[bool, str, Dict]:
        """Check .ddmod file validity"""
        ddmod_path = self.plugin_directory / "TurboLoaderV3.ddmod"
        
        if not ddmod_path.exists():
            return False, "Mod definition file (.ddmod) not found", {}
        
        try:
            with open(ddmod_path, 'r') as f:
                ddmod_data = json.load(f)
            
            # Check required fields
            required_fields = ["name", "unique_id", "version", "author"]
            missing_fields = [field for field in required_fields if field not in ddmod_data]
            
            if missing_fields:
                return False, f"Mod definition missing fields: {', '.join(missing_fields)}", {
                    "ddmod_data": ddmod_data,
                    "missing_fields": missing_fields
                }
            else:
                return True, f"Mod '{ddmod_data['name']}' v{ddmod_data['version']} is valid", {
                    "name": ddmod_data["name"],
                    "version": ddmod_data["version"],
                    "unique_id": ddmod_data["unique_id"]
                }
                
        except json.JSONDecodeError:
            return False, "Mod definition file contains invalid JSON", {}
        except Exception as e:
            return False, f"Error reading mod definition: {e}", {}
    
    def _check_gdscript(self) -> Tuple[bool, str, Dict]:
        """Check GDScript file"""
        gdscript_path = self.plugin_directory / "main.gd"
        
        if not gdscript_path.exists():
            return False, "GDScript file (main.gd) not found", {}
        
        try:
            with open(gdscript_path, 'r') as f:
                gdscript_content = f.read()
            
            # Basic checks
            if not gdscript_content.strip():
                return False, "GDScript file is empty", {}
            
            # Check for required Dungeondraft function
            if "func start(" not in gdscript_content:
                return False, "Missing required start() function for Dungeondraft", {}
            
            return True, f"GDScript file is valid ({len(gdscript_content)} characters)", {
                "file_size": len(gdscript_content),
                "line_count": gdscript_content.count('\n') + 1
            }
            
        except Exception as e:
            return False, f"Error reading GDScript file: {e}", {}
    
    def _check_permissions(self) -> Tuple[bool, str, Dict]:
        """Check file permissions"""
        permission_issues = []
        
        # Check directory permissions
        if not os.access(self.plugin_directory, os.R_OK):
            permission_issues.append("Cannot read plugin directory")
        
        # Check file permissions
        for file_path in self.plugin_directory.iterdir():
            if file_path.is_file():
                if not os.access(file_path, os.R_OK):
                    permission_issues.append(f"Cannot read {file_path.name}")
        
        if permission_issues:
            return False, f"Permission issues: {', '.join(permission_issues)}", {
                "issues": permission_issues
            }
        else:
            return True, "All file permissions are correct", {}

def main():
    """Main entry point"""
    try:
        verifier = QuickVerification()
        result = verifier.verify()
        
        # Exit with appropriate code
        sys.exit(0 if result["success"] else 1)
        
    except KeyboardInterrupt:
        print("\n\nSTOP  Verification cancelled by user")
        sys.exit(130)
    except Exception as e:
        print(f"\nFAIL Verification failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()