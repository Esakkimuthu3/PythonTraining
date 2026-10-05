#Mutiple value only if value>50

domains = ['www.google.com','localhost:3888','openai.com']

cleaned =[ d.upper().replace('WWW.','')
           for d in domains
           if '.' in d
]
print(cleaned)


























