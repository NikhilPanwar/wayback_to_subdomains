# wayback_to_subdomains
Discovers Subdomains using waybackmachine cdx api

### How to Use

1. **Requirements:**
   - Python 3.x
   - Requests library (install it using `pip install requests`)

2. **Usage:**
   - Clone the repository or download the script.
   - Open a terminal or command prompt and navigate to the script's directory.

3. **Command-line Arguments:**
   - `-d` or `--domain`: Specify the target domain for which archived subdomains need to be discovered.
   - `-o` or `--output`: Optional. Provide a filename to save the discovered subdomains in a text file.

4. **Examples:**
   - To discover subdomains for `example.com` and print them to the console:
     ```
     python waybacktosubdomains.py -d example.com
     ```
   - To discover subdomains for `example.com` and save them to a file named `output.txt`:
     ```
     python waybacktosubdomains.py -d example.com -o output.txt
     ```

