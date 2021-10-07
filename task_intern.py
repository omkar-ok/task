import datetime
import calendar
 

#This function is used to calculated average values if value of day is not in input
def fun(num1, num2, num):
    avg = abs((num1-num2)/(num+1))
    return(num1+avg if (num1<num2) else num1-avg)

#This is the main function and algo of this program which returns output Dictionary
def find_solution(D):
    Output_D ={'Mon':0, 'Tue':0, 'Wed':0, 'Thu':0, 'Fri':0, 'Sat':0, 'Sun':0}
    temp_dic ={} # I have created this temp_dic to store some temporary data for calculation purpose

    #this loop is used to sum of each day if multiple input dates belong to same day
    for key, value in D.items():
        Day_num = datetime.datetime.strptime(key, '%Y-%m-%d').weekday()
        try:
            temp_dic[Day_num]= temp_dic.get(Day_num)+value
        except:
            temp_dic[Day_num]=value

    #This loop is used to check whether all weekdays are in dictionary or not, if not then call funtion and calculate its value 
    for j in range(0,7):
        if(j not in sorted(temp_dic.keys())):
            temp_dic[j]=fun(temp_dic.get(j-1),temp_dic.get(sorted (temp_dic.keys())[j]),sorted (temp_dic.keys())[j]-j)


    #This Loop is used to verify all value and prepare final output dictionary
    for i in sorted (temp_dic.keys()):
        day=calendar.day_name[i][0:3]
        Output_D[day]=temp_dic.get(i)

    return Output_D



#Dic = {'2020-01-01':4, '2020-01-02':4, '2020-01-03':6, '2020-01-04':8, '2020-01-05':2, '2020-01-06':-6, '2020-01-07':2, '2020-01-08':-2}
#Dic = {'2020-01-01':4, '2020-01-02':5, '2020-01-05':2, '2020-01-06':-6, '2020-01-07':2, '2020-01-08':-2}
#Dic = {'2020-01-01':6, '2020-01-04':12, '2020-01-05': 14,'2020-01-06':2, '2020-01-07':4}

#This used to take input values
#Note- here assumption is input must have mon & sun and all input format(Date format) is right so i haven't used any input validation 
n = int(input("enter no of key-value pairs value:"))
Dic = {}
for i in range(n):
    keys = input("input date in format %Y-%m-%d eg.(2020-01-25) : ")
    values = int(input("input value integer only                      : "))
    Dic[keys] = values
print("\nYour input Dictionary is \n" , Dic)
print("\nOutput is : \n", find_solution(Dic))

#this will hold the output screen if no any ide or idle used to run this script
input()
