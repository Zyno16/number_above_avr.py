#display sum and number above the average
count =0
s=0
for i in [1,7,37,45,54,67,74]: 
   
      count = count + i
      s=s+1
      avr= count/s
print ("the sum is = ",count)

print ("the averge =",avr)
for i in [1,7,37,45,54,67,74]: 
      if i >  avr :
            print(i)
