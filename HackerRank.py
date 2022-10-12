A= -1
P = -5
K =1

# formula for remaining # of problems kelly needs to exceed Asha after first day
remainingDays = A + P - K
countingDays = 1 # counter to keep track of days minimum, counter starts at 1,                since its initially subtracts and Kelly is already done 1 day  

# keep subtracting as long as it hits 0 days reaming 
while remainingDays >= 0:
    remainingDays = remainingDays - K 
    countingDays +=1
    
    # break loop as soon as days hit less than 0, which means kelly passed Asha, since less than 0 problems left  
    if remainingDays< 0:
        break
    
#edge case for when it is impossible if Asha is done 0 questions and Kelly has done more
if A == 0 and P == 0:
    print("-1")
ifelse A<0 and P<0:
    print("-1")
