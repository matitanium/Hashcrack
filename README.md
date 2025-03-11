# Hash Cracking Tool

## Overview
Hash-Crack is a simple and efficient hash cracking tool written in Python. It supports multiple hash algorithms and uses a wordlist-based attack to find the original plaintext of a given hash.

## Features
- Supports the following hash types:
  - MD5
  - SHA-1
  - SHA-224
  - SHA-256
  - SHA-384
  - SHA-512
- Uses a wordlist to crack hashes
- Provides a simple CLI interface with color-coded output
- Compatible with Windows and Linux

## Installation
Ensure you have Python installed. If `colorama` is not installed, the script will attempt to install it automatically.

```bash
pip install colorama
```

## Usage
Run the script and follow the prompts:

```bash
python hash_cracker.py
```

### Example
```bash
Enter Your HashType -- (example 1 / 2 / 3) : 1
Enter Your Hash: ... 8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918
Enter Your WordList Address: Example D:\password.txt
```

If the hash is found in the wordlist, the tool will display the cracked password.

## Notes
- The script uses a wordlist-based attack; ensure you provide a good-quality wordlist for best results.
- The tool is meant for educational and ethical security testing purposes only.

## Author
Coded by: **Matin Nouriyan**  
Email: [matinnoryan@gmail.com](mailto:matinnoryan@gmail.com)

