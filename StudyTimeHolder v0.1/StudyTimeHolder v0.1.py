import os

def ReadFunction():
    with open("data.txt","r") as file:
        return file.readline()

def WriteFunction(strData_to_write):
    with open("data.txt","w") as file:
        file.write(strData_to_write)


def SplitFunction(strData):
    return strData.split(":")
    
def MergeFunction(merged_list1):
    return_str = ""
    return_str += str(merged_list1[0])+":"+str(merged_list1[1])+":"+str(merged_list1[2])+":"+str(merged_list1[3])
    return return_str

def MainFunction(strData_input):


    values = SplitFunction(ReadFunction())
    day = int(values[0])
    hour = int(values[1])
    minute = int(values[2])
    second = int(values[3])

    values = SplitFunction(strData_input)
    day += int(values[0])
    hour += int(values[1])
    minute += int(values[2])
    second += int(values[3])

    minute += second//60
    hour += minute//60
    day += hour//24

    second %=60
    minute %=60
    hour %=24

    list1 = [day,hour,minute,second]

    WriteFunction(MergeFunction(list1))

    print("Day: "+str(day)+" Hour: "+str(hour)+" Minute: "+str(minute)+" Second: "+str(second))

while(True):

    try:
        print("Please write in this format day:hour:minute:second or in this format hour:minute:second or this format minute:second or this format second")

        strData_input=str(input())

        count_number = strData_input.count(":")

        if(count_number==0):
            strData_input="0:0:0:"+strData_input
        elif(count_number==1):
            strData_input="0:0:"+strData_input
        elif(count_number==2):
            strData_input="0:"+strData_input

        if(strData_input=="quit"):
            break
        MainFunction(strData_input)

    except:
        if(os.path.isfile("data.txt") != True):
            print("Error! data.txt does not exist")
            with open("data.txt","w") as file:
                file.write("0:0:0:0")
            print("data.txt is created pls rewrite you previous data")
            print(" ")
        else:
            print("Error! "+"\n")
            break

