import requests
from pprint import pprint

r = requests.get('https://github.com/Raviteja474/Raviteja_teaching/blob/main/project/conval_trigger/Configuration/Eagle_Dell_config.json')

print(r)

pprint(str(r.content))
#print(r.headers)