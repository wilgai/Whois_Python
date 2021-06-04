import whois

file="google.com"
record=whois.whois(file) 
print(record, file=open("info.txt","a"))