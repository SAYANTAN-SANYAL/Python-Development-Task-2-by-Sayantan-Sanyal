sample = {'physics':88 , 'maths':75, 'chemistry':72, 'Basic electrical':89}
print("The original dictionary is: " + str(sample))
minimum = min(sample.values())
res = [key for key in sample if sample[key] == minimum ]
print("Minimum value is: ", minimum)
print("Key corresponding to minimum value is: " + str(res)) 