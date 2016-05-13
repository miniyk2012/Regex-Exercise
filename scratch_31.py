import re

print(re.search(r'(\d)\d(\d)', '65789190').groups())
print(re.findall(r'(\d)\d(\d)', '657891907'))