import math
print("be samane khosh amadid")
count=int(input("tedad danesh amozan ra vared konid: "))
nomredarskam=0
nomredarsziad=20
num2=1
sum=0
for i in range(count):
    danesh_amoz=i+1
    print("nomre danesh amoze",danesh_amoz , "(az 20): ")
    nomre = float(input("nomre: "))
    sum += nomre
    if nomredarskam<nomre:
        nomredarskam=nomre
        num1=danesh_amoz
    if nomredarsziad>nomre:
        nomredarsziad=nomre
        num2=danesh_amoz
avarage= sum / count
#output
print("miangine class =",avarage)
print("bishtarin nomre male daneshamoze",num1,"ba nomre=",nomredarskam)
print("kamtarin nomre male daneshamoz",num2, "ba nomre=",nomredarsziad)