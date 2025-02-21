import argparse
import tldextract

def load_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return set(line.strip().lower() for line in file if line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return set()

def is_subdomain(domain, scope_list):
    extracted_domain = tldextract.extract(domain)
    root_domain = f"{extracted_domain.domain}.{extracted_domain.suffix}"
    
    return root_domain in scope_list or domain in scope_list

def filter_domains(domain_file, scope_file, output_file):
    domains = load_file(domain_file)
    scopes = load_file(scope_file)
    
    valid_domains = [domain for domain in domains if is_subdomain(domain, scopes)]
    
    with open(output_file, "w", encoding="utf-8") as out:
        out.write("\n".join(valid_domains))
    
    print(f"✅ {len(valid_domains)} valid domains saved to '{output_file}'")

def main():
    parser = argparse.ArgumentParser(description="Filter domains based on a scope list.")
    parser.add_argument("-l", "--list", default="domains.txt", help="File containing discovered domains (default: domains.txt)")
    parser.add_argument("-s", "--scope", default="scope.txt", help="File containing valid scope domains (default: scope.txt)")
    parser.add_argument("-o", "--output", default="final-scope.txt", help="Output file for valid domains (default: final-scope.txt)")
    
    args = parser.parse_args()
    
    filter_domains(args.list, args.scope, args.output)

if __name__ == "__main__":
    main()
