information = []
data = []
count = 0
class Apps():
    def app_input(self):
        global information
        global data
        global count
        print("Enter the software application details :")
        count = int(input('Enter the total number of apps :'))
        for i in range(count):
            name = input("\n\nEnter the " +str(i+1)+" app name : ")
            information.append(name)
            developer = input("Enter the " +str(i+1)+" app developer : ")
            information.append(developer)
            version = input("Enter the " +str(i+1)+" app's version : ")
            information.append(version)
            year = int(input("Enter the "+str(i+1)+" app developed year: "))
            information.append(year)
            price = int(input("Enter the "+str(i+1)+" app's price : "))
            information.append(price)
            data.append(information)
            information = []
    def details(self):
        for i in range(count):
            print("\n\n{5} The name of the app is {0}, developed by {1}.\nthe version {2} published in the year {3} at the price of {4}".format(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],i+1))
    def sort_price(self):
        print("\n\n Increasing price")
        p=[]
        for i in range(count):
            o = data[i][4]
            p.append(o)
        p.sort()
        print("\nThe app by price from low to high")
        for i in p:
            for j in range (count):
                if(i == data[j][4]):
                    print(data[j])
    def search(self):
        print("\n\nsearching")
        while(True):
            choice=int(input(("Enter  1 to search \nOR\nEnter 0 to stop ")))
            if(choice==1):
                s=input("Enter the developer name : ")
                q=int(input("Enter the developed year : "))
                flag=0
                for i in range(count):
                    if(q == data[i][3]):
                        if(s == data[i][1]):
                            print("The searched app is  ",data[i])
                            flag=flag+1
                if(flag == 0):
                    print("No apps developed by {1} in {0}".format(q, s))
            elif(choice==0):
                return print("THANK YOU!!")
    def sort_year(self):
        year=[]
        for i in range(count):
            b = data[i][3]
            year.append(b)
        year.sort()
        for i in year:
            for j in range(count):
                if(i == data[j][3]):
                    print(data[j])
obj = Apps()
obj.app_input()
obj.details()
obj.sort_price()
obj.search()
obj.sort_year()
