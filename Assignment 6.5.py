#Write code using find() and string slicing to extract the number at the end
#of the line below. Convert the extracted value to a floating point number
#and print it out.


#col stands for colon.

text = "X-DSPAM-Confidence:    0.8475";
col = text.find(':')
num_only = text[col+1 : ]
convert = float(num_only)
print(convert)

#Output should be equal to 0.8475