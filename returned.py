import datetime as dt

def readfile():
    files=open("costumelist.txt","r")
    inside=files.readlines()
    files.close()
    return inside

def to_dict(filelist):
    dictionary={}
    for index in range(len(filelist)):
        dictionary[index+1]=filelist[index].replace("\n","").split(",")
    return dictionary

def prints_list():
    filelist=readfile()
    display=to_dict(filelist)
    print("--------------------------------------------------------------------------------------------------")
    print(" {:<10} {:<33} {:<13} {:<13} {:<10} ".format("S.No","Custoume Name","Brand","Price","Quantity"))
    print("--------------------------------------------------------------------------------------------------")
    for x,y in display.items():
        print("{:<10} {:<30} {:<20} {:<10} {:<10}".format(x,y[0],y[1],y[2],y[3],"\n"))
    return display
     
def sno():
    filelist=readfile()
    display=to_dict(filelist)
    validate_sno=False
    while validate_sno==False:
        try:
            idno_input=int(input("\nEnter the serial number of costume you wanna return :"))
            if idno_input<=len(display)and idno_input>0:
                print("++++++++++++++++++++++++++++++++++\n We have that custoume. \n++++++++++++++++++++++++++++++++++\n")
                validate_sno=True
                return idno_input
            elif idno_input<=0 or idno_input>len(display):
                print("++++++++++++++++++++++++++++++++++\n Invalid input\n Re-type again!!!\n++++++++++++++++++++++++++++++++++\n")
        except :
           print("\n-------------------------------\n Invalid input!!!\n Please enter valid numbers.\n-------------------------------\n")
            

def valid_quantity(idno_input):
    filelist=readfile()
    display=to_dict(filelist)
    validate_quantity=False
    while validate_quantity==False:
        try:
          quantity_inputs=int(input("\nEnter the number of quantity you wanna return :"))
          if quantity_inputs<0 or quantity_inputs>int(display[idno_input][3]):
            print("++++++++++++++++++++++++++++++++++\n Value not matched.\n Re-type again!!!\n++++++++++++++++++++++++++++++++++\n")
            sno()
          elif quantity_inputs<=int(display[idno_input][3]):
            print("++++++++++++++++++++++++++++++++++\n The custoume you asked is available in stock.\n++++++++++++++++++++++++++++++++++\n")
            validate_quantity=True
            return quantity_inputs
        except:
           print("+++++++++++++++++++++++++++++\n Format Incorrect!!\n+++++++++++++++++++++++++++++\n ")
        
def writedata(display):
    file=open("costumelist.txt",'w')
    for value in display.values():
        noted=value[0]+","+value[1]+","+value[2]+","+value[3]+"\n"
        file.write(noted)
    file.close()
    return noted
    
    
def returned_multiple_costume():
    listed = []
    brands=[]
    costumename=[]
    filelist = readfile()
    display=to_dict(filelist)
    while True:
        idno_input=sno()
        quantity_inputs=valid_quantity(idno_input)
        listed.append([idno_input,quantity_inputs])
        display[idno_input][3]=str(int(display[idno_input][3])+quantity_inputs)
        writedata(display)
        print("--------------------------------------------------------------------------------------------------")
        print(" {:<10} {:<33} {:<13} {:<13} {:<10} ".format("S.No","Custoume Name","Brand","Price","Quantity"))
        print("--------------------------------------------------------------------------------------------------")
        for a,b in display.items():
            print("{:<10} {:<30} {:<20} {:<10} {:<10}".format(a,b[0],b[1],b[2],b[3],"\n"))

        again=str(input("Want to add more to return the custoumer(yes/no) :"))
        if again == "no":
            databill = billing(listed,brands,costumename)

            write_bill(databill,brands,costumename)
            break

            
def billing(listed,brands,costumename):
     filelist=readfile()
     display=to_dict(filelist)
     a=str(input("Enter the name of the costumer :"))
             
             
     print("=================================================================================================================\n")
     print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
     print("\t\tCustoume Rental Shop\n\t\tBafal,KTM,Nepal\n\t\tABBREVIATED TAX INVOICE\n\t\tBILL")
     print("=================================================================================================================\n")
     print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
     print(" {:<10} {:<33} {:<13} {:<13} {:<10} ".format("S.No","Custoume Name","Brand","Price","Quantity"))
     print("-----------------------------------------------------------------------------------------------------------------\n")
     print("Name :" +a)
     print("Date and time of rented coustume :" +getdatetime())
     fine=0
     grandtotal=0
     for number in range(len(listed)):
        r_id=int(listed[number][0])
        r_custoumename=display[r_id][0]
        r_brand=display[r_id][1]
        r_quantity=int(listed[number][1])
        r_price=int(display[r_id][2].replace("$",""))*r_quantity
        grandtotal+= r_price
        brands.append([r_brand])
        costumename.append([r_custoumename])
        print("{:<10} {:<33} {:<13} {:<13} {:<10} ".format(r_id, r_custoumename,r_brand,r_quantity,str(r_price)))
        print("\n-----------------------------------------------------------------------------------------------------------------\n")
     print("\t Grand Total :\t\t\t\t" +str(grandtotal))
     stats=int(input("how many days have been rented from now??"))
     if (stats<=5):
         fine=0
         print("Your total fine is :" +str(fine))
     else:
        r_price=int(r_price)
        minus=stats-5
        fine=minus*r_price
        grandtotal=grandtotal+fine
        print("\n-------------------------------------------------------------------------------\n")
        print("Name of custoumer is : "+a)
        print("date and time is :" +getdatetime())
        print("\n---------------------------------------------------------------------------------\n")
        print("your total fine is :" +str(fine))
        print("Your total sum is :"+str(grandtotal))
     return a, r_id, r_custoumename,r_brand,r_quantity,str(r_price),str(grandtotal),str(fine)

def write_bill(datas,brands,costumename):

    minute = str(dt.datetime.now().minute)
    second = str(dt.datetime.now().second)
    microsecond = str(dt.datetime.now().microsecond)
    FileName = "Return_"+datas[0]+"_"+minute+second+microsecond+".txt"

    file = open(FileName,"w")
    file.write("Name of costumer is:"+str(datas[0]))
    file.write("\n\n")
    file.write("Costume is:"+str(costumename))
    file.write("\n\n")
    file.write("Brand is:"+str(brands))
    file.write("\n\n")
    file.write("Quantity is:"+str(datas[4]))
    file.write("\n")
    file.write("Price is:"+"$"+str(datas[5]))
    file.write("\n")
    file.write("====================================\n")
    file.write("Fine is :"+ str(datas[7]))
    file.write("\nTotal is :" +str(datas[6]))
    
    file.close()
    
    
def getdatetime():
    year = str(dt.datetime.now().year)
    month = str(dt.datetime.now().month)
    day = str(dt.datetime.now().day)
    hour = str(dt.datetime.now().hour)
    minute = str(dt.datetime.now().minute)
    second = str(dt.datetime.now().second)
    now = year+"/"+month+"/"+day+'/'+hour+'/'+minute+'/'+second
    return now
