#Convert the decimal number in string below to a floating point number

str = "X-DSPAM-Confidence: 0.8475 "
colon_pos = str.find(':')
number=str[colon_pos+1 :]
print(float(number))
