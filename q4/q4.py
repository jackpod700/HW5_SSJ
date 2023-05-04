import csv
def main():
    f=open('202303_Seoul_Subway.csv','r',encoding='ANSI')
    data=csv.reader(f)
    header=next(data)
    
    line1b=1
    line1l=99999999
    line2b=1
    line2l=99999999
    line3b=1
    line3l=99999999
    line4b=1
    line4l=99999999
    line1bn=""
    line1ln=""
    line2bn=""
    line2ln=""
    line3bn=""
    line3ln=""
    line4bn=""
    line4ln=""
    for row in data:
        if((row[1])[0]=="1"):
            if(line1b<int(row[-3])):
                line1bn=row[3]
                line1b=int(row[-3])
            if(line1l>int(row[-3])):
                line1ln=row[3]
                line1l=int(row[-3])
        elif((row[1])[0]=="2"):
            if(line2b<int(row[-3])):
                line2bn=row[3]
                line2b=int(row[-3])
            if(line2l>int(row[-3])):
                line2ln=row[3]
                line2l=int(row[-3])
        elif((row[1])[0]=="3"):
            if(line3b<int(row[-3])):
                line3bn=row[3]
                line3b=int(row[-3])
            if(line3l>int(row[-3])):
                line3ln=row[3]
                line3l=int(row[-3])
        elif((row[1])[0]=="4"):
            if(line4b<int(row[-3])):
                line4bn=row[3]
                line4b=int(row[-3])
            if(line4l>int(row[-3])):
                line4ln=row[3]
                line4l=int(row[-3])
    
    print("***Subway Report for Seoul on March 2023***")
    print("Line ",1)
    print("Busiest Station: {0:s} ({1:d})".format(line1bn,line1b))
    print("Least used Station: {0:s} ({1:d})".format(line1ln,line1l))
    print("Line ",2)
    print("Busiest Station: {0:s} ({1:d})".format(line2bn,line2b))
    print("Least used Station: {0:s} ({1:d})".format(line2ln,line2l))
    print("Line ",3)
    print("Busiest Station: {0:s} ({1:d})".format(line3bn,line3b))
    print("Least used Station: {0:s} ({1:d})".format(line3ln,line3l))
    print("Line ",4)
    print("Busiest Station: {0:s} ({1:d})".format(line4bn,line4b))
    print("Least used Station: {0:s} ({1:d})".format(line4ln,line4l))
            
    
    f.close()
if __name__=="__main__":
    main()
