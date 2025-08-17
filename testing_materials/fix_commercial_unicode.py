#!/usr/bin/env python3
"""
Fix Unicode characters in commercial installer for Windows compatibility
"""

import re

def fix_unicode_in_file(file_path):
    """Replace Unicode characters with ASCII equivalents"""
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Define Unicode replacements for commercial installer
    replacements = {
        '✓': 'PASS',
        '✗': 'FAIL', 
        '⚠': 'WARN',
        '✅': 'PASS',
        '❌': 'FAIL',
        '⚡': '>>',
        '🚀': '>>',
        '🎯': '>>',
        '📦': '>>',
        '💻': '>>',
        '🔧': '>>',
        '📚': '>>',
        '🔄': '>>',
        '🔍': '>>',
        '⭐': '*',
        '🎉': '>>',
        '👍': '>>',
        '👎': '>>',
        '💡': '>>',
        '⬇': 'v',
        '⬆': '^',
        '➡': '>',
        '⬅': '<',
        '•': '-',
        '→': '>',
        '←': '<',
        '↑': '^',
        '↓': 'v',
        '≥': '>=',
        '≤': '<=',
        '≠': '!=',
        '…': '...',
        '"': '"',
        '"': '"',
        ''': "'",
        ''': "'",
        '–': '-',
        '—': '--',
    }
    
    # Apply replacements
    for unicode_char, replacement in replacements.items():
        content = content.replace(unicode_char, replacement)
    
    # Write back with UTF-8 encoding
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed Unicode characters in {file_path}")

if __name__ == "__main__":
    # Fix all Python files in the commercial test directory
    files_to_fix = [
        "TurboLoaderV3_Installer.py",
        "verify_installation.py", 
        "simple_test.py"
    ]
    
    for filename in files_to_fix:
        try:
            fix_unicode_in_file(filename)
        except FileNotFoundError:
            print(f"File not found: {filename}")
        except Exception as e:
            print(f"Error fixing {filename}: {e}")
            
    print("Unicode fix complete for commercial package!")