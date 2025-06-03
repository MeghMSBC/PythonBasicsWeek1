# list=[]
# for i in range(3):
#    num= input("Enter "+str(i)+" Number: ")
#    list.append(int(num))

# i=0
# j=len(list)-1
# flag=1
# while i<j:
#     if list[i]!=list[j]:
#         flag=0
#         break
#     else:
#         i+=1
#         j-=1
# if(flag!=0):
#     print("Is a palindrome")
# else:
#     print("Is not a palindrome")

# rev = list.copy()
# rev.reverse()
# print(rev)
# if(list==rev):
#    print("Is a palindrome")
# else:
#    print("Is not a palindrome")


#dictionary
# dict = {
#    "table":["a piece of furniture","list of facts & figures"],
#    "cat":["a small animal"]
# }
# print(dict)

#factorial using recusrion
#def factorial(n):
#    if(n==0 or n==-1):
#       return 1
#    else:
#       return n* factorial(n-1)
# ans = factorial(5)
# print(ans)

# def sum(n):
#     if(n==0):
#         return 0
#     return sum(n-1)+n
# ans = sum(4)
# print(ans)

def showList(list,idx):
    if(idx==len(list)):
        return
    print(list[idx])
    showList(list,idx+1)

myList = [1,2,3,4,5]

showList(myList,0)