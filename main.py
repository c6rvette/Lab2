#n1 (done)
ref_list=[['Никита','Тимур','Азат'], ['Куренин','Зекрин','Юлдашев']]
mass=[]
def list_reorder(ref_list):
    try: #Трай и эксепт нужны, чтобы скрипт в любом случае выводился
        for g in ref_list[0]:
            mass.append([g])
        for i in range(len(ref_list[1])):
            mass[i].append(ref_list[1][i])
        return mass
    except: 
        return
print (list_reorder(ref_list))
#n2 (done)
# def del_rep(listt):
#     a=list(set(listt))
#     i=0
#     g=0
#     b=0
#     while True: #Цикл работает, пока он принимает значение True
#         if a[i] > a[i+1]:
#             g=a[i]
#             a[i]=a[i+1]
#             a[i+1]=g
#         if a[i] < a[i+1]:
#             b+=1
#         else:
#             b=0
#         if b==len(a):
#             break
#     return a
# print(del_rep([1,1,1,4,3,9,5]))
#n3 (done)
# nums=(10,20,30,40,50,60,70,80,90)
# def lim_max(nums, limit):
#     g=0
#     e=list(nums)
#     for i in range(len(e)):
#         if e[i]<limit and e[i]>g: #Сравнение заданного числа с limit и g
#             g=e[i]
#     if g == 0:
#         return -1 #"Если такого значения нет, вернуть -1."
#     else:
#         return g
# print(lim_max(nums, 55))
#n4 (done)
# temp=10
# def temp_cat(temp):
#     try: #Трай и эксепт нужны, чтобы скрипт в любом случае выводился
#         if temp<-20:                      
#             return 1, 'Холодно'
#         elif temp >= -20 and temp <= 0:
#             return 2, 'Прохладно'
#         elif temp >= 0 and temp <= 15:
#             return 3, 'Зябко'
#         elif temp >= 15 and temp <= 25:
#             return 4, 'Тепло'
#         elif temp > 25:
#             return 5, "Жарко"
#     except: 
#         return 404, 'Ошибка'
# print(temp_cat(temp))
#n5


        
        
        
        
        
    
    
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        







