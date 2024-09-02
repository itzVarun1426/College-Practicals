def average(m):
	print("This is average function: ")
	sum=0
	abs=0
	for i in range (0,n,1):
		if(m[i]!=-999):
				sum+=m[i]
		else:
			abs+=1
	avg=sum/(n-abs)
	print("The average of the marks obtained in class is : ",avg )

def maximum(m):
	print("This is maximum function: ")
	maxi=m[0]
	for i in range(0,n,1):
		if(m[i]>maxi):
			maxi=m[i]
	print("The maximum marks obtained in class is : ",maxi)


def minimum(m):
	print("This is minimum function: ")
	mini=m[0]
	for i in range(0,n,1):
		if(m[i]==-999):
			continue
		if(m[i]<mini):
			mini=m[i]
	print("The minimum marks obtained in class is : ",mini)

def absent(m):
	print("This is function to find absent student :")
	absent=0
	for i in range(0,n,1):
		if(m[i]==-999):
			absent+=1
	print("Number of absent student is : ",absent)

def frequency(m):
	print("This is frequency function: ")
	count=1
	maxfreq=1
	for i in range (0, n , 1):
		for j in range (i+1, n ,1):
			if(m[i]==m[j]):
				count+=1
		if(count>maxfreq):
			maxfreq=count
			print("The most frequent mark is : ", m[i])
			print("The number is ",maxfreq ," times frequent
	
def mainmenu(m):
	print("\n\n----------------------------MENU-------------------------------------------\n\n")
	print("1. press 1 to find average of the marks :\n")
	print("2. press 2 to find highest among the marks :\n")
	print("3. press 3 to find lowest among the marks :\n")
	print("4. press 4 to find number of absent student :\n")
	print("5. press 5 to find most frequent marks :\n\n")
	ch=int(input("Enter your choice : "))
	
	if(ch==1):
		average(m)
		rep=input("Do you want to try again (yes/no) : ")
		if(rep=="yes"):
			mainmenu(m)
		else:			
			print("Thank you for using my programme")
			
	elif(ch==2):
		maximum(m)
		rep=input("Do you want to try again (yes/no) : ")
		if(rep=="yes"):
			mainmenu(m)
		else:
			
			print("Thank you for using my programme")
			
	elif(ch==3):
		minimum(m)
		rep=input("Do you want to try again (yes/no) : ")
		if(rep=="yes"):
			mainmenu(m)
		else:
			
			print("Thank you for using my programme")
			
	elif(ch==4):
		absent(m)
		rep=input("Do you want to try again (yes/no) : ")
		if(rep=="yes"):
			mainmenu(m)
		else:
			print("Thank you for using my programme")	
			
	elif(ch==5):
		frequency(m)
		rep=input("Do you want to try again (yes/no) : ")
		if(rep=="yes"):
			mainmenu(m)
		else:
			print("Thank you for using my programme")	
			
	else:
		print("Invalid input")	
		rep=input("Do you want to try again (yes/no) : ")
		if(rep=="yes"):
			mainmenu(m)
		else:
				
			print("Thank you for using my programme")

marksofFDS=[]
n=int(input("Enter the number of Student : "))
i=0
while(i<n):
	print("Enter the marks of ", i+1 ,"th student")
	mark=int(input())
	if(mark>30 or mark<0):
		if(mark==-999 or mark==-1):
			marksofFDS.append(mark)
			print("--The last number student was absent--")
			i+=1
			continue
		print("-----------------------invalid input ---------------------")
		print("Enter the marks of ", i+1 ,"th student again")
		i-=1
	else:
		marksofFDS.append(mark)
	i+=1
print(marksofFDS)
mainmenu(marksofFDS)

			
			
			
			
			
			
			
			
			
			
			
			
	
	 


