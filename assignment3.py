def union(l1 , l2):
	ans = []
	for i in l1:
		ans.append(i)
	for i in l2:	
		if i not in l1:
			ans.append(i)
	return ans
	
def intersection(l1 ,l2):
	ans = []
	for i in l1:
		if i in l2:
			ans.append(i)
	return ans
	
def difference(l1 , l2):
	ans = []
	for i in l1:
		if(i not in l2):
			ans.append(i)
	return ans
	
def mainmenu():

	n = int(input("Enter the no of student who play Cricket : "))
	for i in range (n):
		print("Enter the roll no of " , i+1 ," th student who play Cricket : ")
		C.append(input())
	n = int(input("Enter the no of student who play Badminton : "))
	for i in range (n):
		print("Enter the roll no of " , i+1 ," th student who play Badminton : ")
		B.append(input())	
	n = int(input("Enter the no of student who play Football : "))
	for i in range (n):
		print("Enter the roll no of " , i+1 ," th student who play Football :")
		F.append(input())	
	
	
	print("\n----------------------------MENU-------------------------------------------\n\n")
	print("1. press 1 to get list of student who play both cricket and football :\n")
	print("2. press 2 to get list of student who play either cricket or badminton but not both :\n")
	print("3. press 3 to no of student who play neither cricket nor badminton :\n")
	print("4. press 4 to no of student who play cricket and football but not badminton :\n")
	ch=int(input("Enter your choice : "))
	
	if(ch==1):
		print(intersection(C,F))
		rep=input("Do you want to try again:(yes/no) ")
		if(rep=="yes"):
			mainmenu()
		else:
			print("-------thanks to use our product--------")
	if(ch==2):

		un = list(union(C,B))
		inter = list(intersection(C,B))
		print(difference(un , inter))
		rep=input("Do you want to try again:(yes/no) ")
		if(rep=="yes"):
			mainmenu()
		else:
			print("-------thanks to use our product--------")
	if(ch==3):
		un = list(union(C,B))
		print(difference(F,un))
		rep=input("Do you want to try again:(yes/no) ")
		if(rep=="yes"):
			mainmenu()
		else:
			print("-------thanks to use our product--------")
	if(ch==4):
		un = list(union(C,F))
		print(difference(un,B))
		rep=input("Do you want to try again:(yes/no) ")
		if(rep=="yes"):
			mainmenu()
		else:
			print("-------thanks to use our product--------")


C=[]
B=[]
F=[]
	
mainmenu()
		
			
			
			
			
			
			
			
			
			
			
	
	 


