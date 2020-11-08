import os
import argparse
import sublist3r

#Set arguments
parser = argparse.ArgumentParser(description='Get you some!')
parser.add_argument('-d','--domain',help='Domain to be tested', required=True)
parser.add_argument('-o','--output',help='Output file for results', required=True)
args = parser.parse_args()

#Set variables
domain = args.domain
output = args.output

#Enumerate subdomains using Sublist3r
subdomains = sublist3r.main(domain, 40, output, ports= None, silent=True, verbose= True, enable_bruteforce= False, engines=None)

#Use Eyewitness against discovered subdomains
eyewitness = f"eyewitness -f {output} -d Screens --web --prepend-https --delay 5 --no-prompt"
os.system(eyewitness)

#Use Takeover to scan for subdomain takeover
takeover = f"takeover -l {output} -o takeover.txt -v"
os.system(takeover)
