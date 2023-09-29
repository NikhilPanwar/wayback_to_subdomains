import argparse
import requests

def get_archived_urls(domain):
    api_url = f"http://web.archive.org/cdx/search/cdx?url=*.{domain}/*&output=text&fl=original&collapse=urlkey"
    response = requests.get(api_url, verify=False)
    
    if response.status_code == 200:
        cleaned_urls = set()
        for line in response.text.splitlines():
            cleaned_url = line.replace('https://', '').replace('http://', '').split('/')[0].split(':')[0].replace('www.', '').rstrip('.')
            if '@' not in cleaned_url:
                cleaned_urls.add(cleaned_url)
        return sorted(cleaned_urls)
    else:
        return None

def main():
    parser = argparse.ArgumentParser(description='Retrieve archived URLs for a domain from the Wayback Machine.')
    parser.add_argument('-d', '--domain', required=True, help='Domain for which archived URLs need to be retrieved.')
    parser.add_argument('-o', '--output', help='Output file to save the discovered subdomains.')
    args = parser.parse_args()
    
    archived_urls = get_archived_urls(args.domain)
    
    if archived_urls:
        for url in archived_urls:
            print(url)
        
        if args.output:
            with open(args.output, 'w') as file:
                for url in archived_urls:
                    file.write(url + '\n')
            print(f"Discovered subdomains saved to {args.output}.")
    else:
        print("Failed to retrieve archived URLs.")

if __name__ == "__main__":
    main()
