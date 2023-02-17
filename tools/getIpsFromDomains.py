import argparse
import socket

parser = argparse.ArgumentParser(description='Resolve IP addresses for a list of domains')
parser.add_argument('input_file', help='the file containing the list of domains')
parser.add_argument('-o', '--output_file', help='the file to write the results to', default='output.txt')

args = parser.parse_args()

with open(args.input_file, 'r') as f, open(args.output_file, 'w') as out:
    for domain in f:
        domain = domain.strip()
        try:
            ip = socket.gethostbyname(domain)
            result = f"{domain} - {ip}"
        except socket.gaierror:
            result = f"Error resolving {domain}"
        print(result)
        out.write(result + '\n')
