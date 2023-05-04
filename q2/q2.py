import csv
def main():
    f=open('2022_Seoul_Temp.csv','r',encoding='ANSI')
    data=csv.reader(f)
    header=next(data)
    minimumday=""
    maximumday=""
    minimum=999
    maximum=-999
    for row in data:
        if(row[2]==""or row[-1]=="" or row[-2]==""):
            continue
        dif=float(row[-1])-float(row[-2])
        if(maximum<dif):
            maximumday=row[0]
            maximum=dif
        if(minimum>dif):
            minimumday=row[0]
            minimum=dif    
    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Day with the Largest Temperature Variation: {0:s}".format(maximumday))
    print("Maximum Temperature Difference: {0:0.1f} Celsius".format(maximum))
    print("Day with the Smallest Temperature Variation: {0:s}".format(minimumday))
    print("Minimum Temperature Difference: {0:0.1f} Celsius".format(minimum))
    f.close()
if __name__=="__main__":
    main()
