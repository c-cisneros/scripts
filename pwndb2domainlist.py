import re
pattern = re.compile("@([a-z]+\.[a-z]+):")
domains = []
output = open("domains_deduped.txt", "w")

for i, line in enumerate(open('test.txt')):
    for match in re.finditer(pattern, line):
        domains.append(match.group(1))

dedup = list(dict.fromkeys(domains))

for element in dedup:
    count = domains.count(element)
    count_str = str(count)
    output.write(element + " " + count_str + "\n")
output.close()