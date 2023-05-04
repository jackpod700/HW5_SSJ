import csv
def main():
    f=open('2022_Seoul_Temp.csv','r',encoding='ANSI')
    data=csv.reader(f)
    header=next(data)
    average=0
    count=0
    minimum=0
    maximum=0
    for row in data:
        if(row[2]==""or row[-1]=="" or row[-2]==""):
            continue
        average+=float(row[2])
        count+=1
        maximum+=float(row[-1])
        minimum+=float(row[-2])   
    average=average/count
    maximum=maximum/count
    minimum=minimum/count
    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Average Temperature: {0:0.2f} Celsius".format(average))
    print("Average Minimum Temperature: {0:0.2f} Celsius".format(minimum))
    print("Average Maximum Temperature: {0:0.2f} Celsius".format(maximum))
    f.close()
if __name__=="__main__":
    main()
