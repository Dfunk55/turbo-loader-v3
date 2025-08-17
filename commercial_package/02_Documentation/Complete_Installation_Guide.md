# TURBO LOADER V3 - COMPLETE INSTALLATION GUIDE

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Installation Methods](#installation-methods)
3. [Automated Installation](#automated-installation)
4. [Manual Installation](#manual-installation)
5. [Verification](#verification)
6. [Troubleshooting](#troubleshooting)
7. [Uninstallation](#uninstallation)

## System Requirements

### Minimum Requirements
- **Dungeondraft:** Version 1.0 or later
- **Operating System:** 
  - Windows 10 (64-bit) or later
  - macOS 10.14 (Mojave) or later  
  - Linux: Ubuntu 20.04+ or equivalent
- **Free Disk Space:** 50MB
- **Privileges:** Administrator/admin access for installation

### Recommended Setup
- **Python:** 3.7 or later (for installer)
- **Dungeondraft:** Latest version
- **Asset Libraries:** Any size (plugin optimizes for large libraries)

### Compatibility
- **Steam Version:** Fully supported
- **Standalone Version:** Fully supported
- **Multiple Installations:** Supports both Steam and standalone simultaneously

## Installation Methods

### Method 1: Automated Installer (Recommended)
- **Best for:** Most users
- **Advantages:** Automatic detection, verification, easy setup
- **Requirements:** Python 3.7+

### Method 2: Manual Installation
- **Best for:** Advanced users, custom setups, Python installation issues
- **Advantages:** Full control, no Python required
- **Requirements:** Basic file management skills

### Method 3: Cross-Platform Package
- **Best for:** System administrators, multiple installations
- **Advantages:** Scriptable, batch installation
- **Requirements:** Command line familiarity

## Automated Installation

### Prerequisites
1. **Install Python 3.7+**
   - Windows: Download from python.org, check "Add to PATH"
   - macOS: Use Homebrew (`brew install python3`) or python.org
   - Linux: `sudo apt install python3 python3-pip`

2. **Close Dungeondraft**
   - Save any open projects
   - Completely exit the application

### Installation Steps

1. **Extract the Installer Package**
   ```
   TurboLoaderV3_Installer_v3.0.0.zip
   └── TurboLoaderV3_Installer.py
   └── TurboLoaderV3.ddmod
   └── main.gd
   └── config.json
   └── README.txt
   ```

2. **Run the Installer**
   
   **Windows:**
   - Double-click `TurboLoaderV3_Installer.py`
   - OR Right-click > "Open with" > "Python"
   - OR Open Command Prompt: `python TurboLoaderV3_Installer.py`
   
   **macOS:**
   ```bash
   cd /path/to/extracted/folder
   python3 TurboLoaderV3_Installer.py
   ```
   
   **Linux:**
   ```bash
   cd /path/to/extracted/folder
   python3 TurboLoaderV3_Installer.py
   ```

3. **Follow the Installer Interface**
   - The installer will auto-detect your Dungeondraft installation
   - Review the detected path
   - Click "Install" to proceed
   - Wait for completion confirmation

4. **Automatic Verification**
   - The installer runs verification automatically
   - You'll see a success message if everything is correct
   - Any issues will be reported with suggested fixes

### Installation Paths

The installer will search these locations automatically:

**Windows:**
- `C:\Program Files (x86)\Steam\steamapps\common\Dungeondraft`
- `C:\Program Files\Steam\steamapps\common\Dungeondraft`
- `%APPDATA%\Dungeondraft`
- `%DOCUMENTS%\Dungeondraft Mods`

**macOS:**
- `~/Library/Application Support/Steam/steamapps/common/Dungeondraft`
- `~/Applications/Dungeondraft.app`
- `~/Documents/Dungeondraft Mods`

**Linux:**
- `~/.local/share/Steam/steamapps/common/Dungeondraft`
- `~/.local/share/Dungeondraft`
- `~/Documents/Dungeondraft Mods`

## Manual Installation

If the automated installer doesn't work or you prefer manual control:

### Step 1: Locate Dungeondraft Mods Folder

**Default Locations:**
- **Windows:** `%USERPROFILE%\Documents\Dungeondraft Mods`
- **macOS:** `~/Documents/Dungeondraft Mods`
- **Linux:** `~/Documents/Dungeondraft Mods`

**Finding Custom Locations:**
1. Start Dungeondraft
2. Go to Tools > Mods
3. Click "Open Mods Folder" to see the exact path

### Step 2: Extract Manual Package
1. Extract `TurboLoaderV3_Manual_v3.0.0.zip`
2. You should see:
   ```
   TurboLoaderV3/
   ├── TurboLoaderV3.ddmod
   ├── main.gd
   └── config.json
   ```

### Step 3: Copy to Mods Folder
1. Copy the entire `TurboLoaderV3` folder
2. Paste it into your Dungeondraft Mods folder
3. Final structure should be:
   ```
   Dungeondraft Mods/
   └── TurboLoaderV3/
       ├── TurboLoaderV3.ddmod
       ├── main.gd
       └── config.json
   ```

### Step 4: Set Permissions
**Windows:**
- Right-click the TurboLoaderV3 folder
- Properties > Security > Edit
- Ensure "Full control" for your user

**macOS/Linux:**
```bash
chmod -R 755 ~/Documents/Dungeondraft\ Mods/TurboLoaderV3
```

## Verification

### Automated Verification
Run the verification script:
```bash
python3 verify_installation.py
```

This will check:
- Required files are present
- File permissions are correct
- JSON files are valid
- GDScript contains required functions

### Manual Verification
1. **Check Files Exist:**
   - Navigate to your Mods folder
   - Confirm TurboLoaderV3 folder exists
   - Confirm all 3 files are present

2. **Test in Dungeondraft:**
   - Start Dungeondraft
   - Go to Tools > Mods
   - Look for "Turbo Loader v3" in the list
   - Enable it and restart Dungeondraft

3. **Confirm Operation:**
   - Load a project with many assets
   - Notice improved loading times
   - Check for any error messages

## Troubleshooting

### Common Issues

**"Python is not recognized" (Windows)**
- Install Python from python.org
- During installation, check "Add Python to PATH"
- Restart Command Prompt

**"Permission denied" errors**
- Run installer as Administrator (Windows)
- Use `sudo` on macOS/Linux
- Check antivirus isn't blocking installation

**"Dungeondraft not found"**
- Use Manual Installation method
- Verify Dungeondraft is installed correctly
- Check for custom installation paths

**Plugin not appearing in Dungeondraft**
- Restart Dungeondraft completely
- Check files are in correct Mods subfolder
- Verify folder name is exactly "TurboLoaderV3"

**Installation verification fails**
- Re-run the installer
- Check file permissions
- Use Manual Installation as backup

### Getting Help

**Email Support:** support@ttrpgsuite.com
- Include your operating system
- Attach verification output if available
- Describe exact error messages

**Before Contacting Support:**
1. Run the verification script
2. Check the troubleshooting section
3. Try the manual installation method

## Uninstallation

### Complete Removal
1. **Disable in Dungeondraft:**
   - Tools > Mods
   - Uncheck "Turbo Loader v3"
   - Restart Dungeondraft

2. **Delete Plugin Files:**
   - Navigate to Dungeondraft Mods folder
   - Delete the "TurboLoaderV3" folder

3. **Clean Installation Files:**
   - Delete downloaded installer packages
   - Remove any temporary files

### Partial Removal (Disable Only)
- Simply uncheck the plugin in Dungeondraft's Mods menu
- Files remain for easy re-enabling later

---

**Installation complete? Start creating optimized maps today!**
