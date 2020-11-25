str = 'X-DSPAM-Confidence:0.8475'
col = str.find(':')
par = str[col+2:]
numb = float(par)
print(numb)
