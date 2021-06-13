'''
Download image-predictions TSV file from the Udacity servers using the Requests library
'''
import requests

r = requests.get('https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv')
print(r.status_code)

with open('image-predictions.tsv', 'w') as outfile:
    outfile.write(r.text)
