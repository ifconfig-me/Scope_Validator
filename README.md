# Domain Scope Filter

A simple Python script to filter valid domains from list of domains based on Scopes.

## Features
- Compare domains from a list with a scope file
- Filters only valid scopes and their subdomains
- Saves results to a custom output file
- Command-line options for flexibility

## Prerequisites
Install required dependencies:
```bash
pip install tldextract
```
## Usage

### **Basic Usage**
```bash
python filter_scope.py
```
(Default files: `domains.txt`, `scope.txt`, `final-scope.txt`)

### **Custom Files**
```bash
python filter_scope.py -l my_domains.txt -s my_scope.txt -o output.txt
```
- `-l` → File with discovered domains  
- `-s` → File with valid scope domains  
- `-o` → Output file for filtered results  

## Example

### **scope.txt**
```
example.com
target.org
```

### **domains.txt**
```
sub.example.com
api.target.org
random.com
```

### **Command**
```bash
python filter_scope.py -l domains.txt -s scope.txt -o final-scope.txt
```

### **Output (`final-scope.txt`)**
```
sub.example.com
api.target.org
```
