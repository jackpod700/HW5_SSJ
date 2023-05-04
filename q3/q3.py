import csv
def main():
    f=open('q3.csv','r',encoding='ANSI')
    data=csv.reader(f)
    header=next(data)
    total=[0,0,0,0,0,0,0,0,0]

    maximum1=-1
    maximum2=-1
    maximum1line=1
    maximum2line=1
    minimum1=999999999
    minimum2=999999999
    minimum1line=1
    minimum2line=1
    
    for row in data:
        if(not((row[1])[0] in ["1","2","3","4","5","6","7","8","9"])):
            continue
        total[int((row[1])[0])-1] += int(row[-3])+int(row[-2])
    total2=total.copy()
    
    maximum1=max(total)
    maximum1line=total.index(maximum1)+1
    minimum1=min(total)
    minimum1line=total.index(minimum1)+1
    total2.remove(maximum1)
    total2.remove(minimum1)
    maximum2=max(total2)
    minimum2=min(total2)
    maximum2line=total.index(maximum2)+1
    minimum2line=total.index(minimum2)+1
            
    print("*** Subway Report for Seoul on March 2023 ***")
    print("1st Busiest Line: Line {0:d} ({1:d})".format(maximum1line,maximum1))
    print("2nd Busiest Line: Line {0:d} ({1:d})".format(maximum2line, maximum2))
    print("1st Least used Line: Line {0:d} ({1:d})".format(minimum1line, minimum1))
    print("2nd Least used Line: Line {0:d} ({1:d})".format(minimum2line, minimum2))
    
    f.close()
if __name__=="__main__":
    main()
