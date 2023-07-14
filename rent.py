import datetime as dt

def read():
    file=open("costumelist.txt","r") #reads the file.
    inside=file.readlines()
    file.close()
    return inside

def into_dict(file_list):
    inside={}
    for index in range(len(file_list)):            #converts and stores into dictionary.
        inside[index+1]=file_list[index].replace("\n","").split(",")
    return inside

def print_list():
    ''' to print the value of dictionary into bill form'''
    file_list=read()
    main_to_show=into_dict(file_list)
    print("--------------------------------------------------------------------------------------------------")
    print(" {:<10} {:<33} {:<13} {:<13} {:<10} ".format("S.No","Custoume Name","Brand","Price","Quantity"))
    print("--------------------------------------------------------------------------------------------------")
    for x,y in main_to_show.items():
        print("{:<10} {:<30} {:<20} {:<10} {:<10}".format(x,y[0],y[1],y[2],y[3],"\n"))
    return main_to_show
     
def ask_sno():
    file_list=read()                #prints serial number.
    main_to_show=into_dict(file_list)
    valid_sno=False
    while valid_sno==False:
        try:
            sno_input=int(input("\nEnter the serial number of costume you wanna rent :"))
            if sno_input<=len(main_to_show)or sno_input>0 :
                print("++++++++++++++++++++++++++++++++++\n We have that custoume. \n++++++++++++++++++++++++++++++++++\n")
                valid_sno=True
                return sno_input
            elif sno_input<0 or sno_input>len(main_to_show):
                print("++++++++++++++++++++++++++++++++++\n Invalid input\n Re-type again!!!\n++++++++++++++++++++++++++++++++++\n")
        except :
           print("\n-------------------------------\n Invalid input!!!\n Please enter valid numbers.\n-------------------------------\n")
            

def get_valid_quantity(sno_input):     #prints validate quantity
    file_list=read()
    main_to_show=into_dict(file_list)
    valid_quantity=False
    while valid_quantity==False:
        try:
            quantity_input=int(input("\nEnter the number of quantity you wanna rent :"))
            
            if quantity_input<0 or quantity_input>int(main_to_show[sno_input][3]):
                print("++++++++++++++++++++++++++++++++++\n Value not matched.\n Re-type again!!!\n++++++++++++++++++++++++++++++++++\n")
                ask_sno()
            elif quantity_input<=int(main_to_show[sno_input][3]):
                print("++++++++++++++++++++++++++++++++++\n The custoume you asked is available in stock.\n++++++++++++++++++++++++++++++++++\n")
                valid_quantity=True
                return quantity_input
        except:
            print("+++++++++++++++++++++++++++++\n Format Incorrect!!\n+++++++++++++++++++++++++++++\n ")
        
def write_data(main_to_show):
    file=open("costumelist.txt",'w')       #writes the updated value to the txt file.
    for value in main_to_show.values():
        writes=value[0]+","+value[1]+","+value[2]+","+value[3]+"\n"
        file.write(writes)
    file.close()
    return writes
    
    
def rent_multiple_costume():
    cart = []
    brand=[]         #allows to rent the custoume multiple times if user wants.
    costume_name=[]
    file_list = read()
    main_to_show=into_dict(file_list)
    while True:
        sno_input=ask_sno()
        quantity_input=get_valid_quantity(sno_input)
        cart.append([sno_input,quantity_input])
        main_to_show[sno_input][3]=str(int(main_to_show[sno_input][3])-quantity_input)
        write_data(main_to_show)
        print("--------------------------------------------------------------------------------------------------")
        print(" {:<10} {:<33} {:<13} {:<13} {:<10} ".format("S.No","Custoume Name","Brand","Quantity","Price"))
        print("--------------------------------------------------------------------------------------------------")
        for a,b in main_to_show.items():
            print("{:<10} {:<30} {:<20} {:<10} {:<10}".format(a,b[0],b[1],b[2],b[3],"\n"))

        again=str(input("Want to add more to rent the custoumer(yes/no) :"))
        if again == "no":
            data_bill = billing(cart,brand,costume_name)

            write_bill(data_bill,brand,costume_name)
            break




            
def billing(cart,brand,costume_name):
     file_list=read()
     main_to_show=into_dict(file_list)
     name=str(input("Enter the name of the costumer :"))
             
             
     print("=================================================================================================================\n")
     print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
     print("\t\tCustoume Rental Shop\n\t\tBafal,KTM,Nepal\n\t\tABBREVIATED TAX INVOICE\n\t\tBILL")
     print("=================================================================================================================\n")
     print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
     print(" {:<10} {:<33} {:<13} {:<13} {:<10} ".format("S.No","Custoume Name","Brand","Quantity","Price"))
     print("-----------------------------------------------------------------------------------------------------------------\n")
     print("Name :" +name)
     print("Date and time of rented coustume :" +get_datetime())
     
     grand_total=0
     for number in range(len(cart)):
        e_id=int(cart[number][0])
        e_custoumename=main_to_show[e_id][0]
        e_brand=main_to_show[e_id][1]
        e_quantity=int(cart[number][1])
        e_price=int(main_to_show[e_id][2].replace("$",""))*e_quantity
        grand_total+= e_price
        brand.append([e_brand])
        costume_name.append([e_custoumename])
        print("{:<10} {:<33} {:<13} {:<13} {:<10} ".format(e_id, e_custoumename,e_brand,e_quantity,str(e_price)))
        print("\n-----------------------------------------------------------------------------------------------------------------\n")
     print("\t Grand Total :\t\t\t\t" +str(grand_total))

     return name, e_id, e_custoumename,e_brand,e_quantity,str(e_price),str(grand_total)

def write_bill(data,brand,costume_name):

    minute = str(dt.datetime.now().minute)
    second = str(dt.datetime.now().second)
    microsecond = str(dt.datetime.now().microsecond)
    uniqueFileName = "Rent_"+data[0]+"_"+minute+second+microsecond+".txt"

    file = open(uniqueFileName,"w")
    file.write("Name of costumer is:"+str(data[0]))
    file.write("\n\n")
    file.write("Costume is:"+str(costume_name))
    file.write("\n\n")
    file.write("Brand is:"+str(brand))
    file.write("\n\n")
    file.write("Quantity is:"+str(data[4]))
    file.write("\n")
    file.write("Price is:"+data[5])
    
    file.close()
    
    
def get_datetime():
    year = str(dt.datetime.now().year)
    month = str(dt.datetime.now().month)
    day = str(dt.datetime.now().day)
    hour = str(dt.datetime.now().hour)
    minute = str(dt.datetime.now().minute)
    second = str(dt.datetime.now().second)
    now = year+"/"+month+"/"+day+'/'+hour+'/'+minute+'/'+second
    return now
