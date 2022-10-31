#funcation to print number of consecutive 0's between two 1's in Binary number of any integer 
def solution(n): #define function and give colon, python have no bracket, its just colon and then next line you need to give indentation, everything with indentation falls with in that function or if or while condition, any line outside of this indentation is considered outside of function or if or while loop , see line 18 which is outside this function 
    b = bin(n)[2:] #binary is function in Python which converts integer into binary, bin(100) will return 1b1100100 where 1b represents it binary, to remove these extra charater in start python has array funcation on each string, [2:] which will remove first 2 character and gives all character after that as length is not given, syntax of this funcation is [starting position:length] if we need only 3rd letter thens skip 2 and take 1 , which means skip index 0, index 1 and start from index 2 and length of 1, [2:1]
    print('binary number is ' + b)
    s1=False #variable used to check if we have any occurance of 1 when we start
    tz=0 #intermediate count of zero
    mz=0 #maximum number of zeros 
    for e in b: #for loop syntax
        if e=='1': #if syntax
            mz=max(tz,mz) #finding max
            tz=0 #resetting to 0 for further count
            s1=True #marking start as we have occurance of 1
        else: #else means we have 0 number 
            if(s1==True): #if we already have first 1 then only
                tz+=1 #count number of 0's
    return mz #return maximum number of 0's

answer=solution(100) #to call a function which return any result you need to assing value to some variable, so we need placeholder variable which is answer here
print('the number of consecutive zeors in this binary number is ' + str(answer)) #see how print function can concate 2 strings, we need to convert answer to string to print it with regular string 
######
#result screen for above program is as below:
# binary number is 1100100
# the number of consecutive zeors in this binary number is 2
######
#an example logic for number 100
#binary of 100 is 1100100 
#for loop runs trhough each number 1 by 1, below are value of variable in each step and how final answer comes to number 2
#for first 1: mz=0, tz=0, S1=True
#for second1: mz=0, tz=0, S1=True
#for third 0: mz=0, tz=1, S1=True
#for forth 0: mz=0, tz=2, S1=True
#for fifth 1: mz=2, tz=0, S1=True
#for sixth 0: mz=2, tz=1, S1=True
#for seven 0: mz=2, tz=2, S1=True
#all 7 element is compelte so for loop ends and returns mz which is 2 so result is 2
