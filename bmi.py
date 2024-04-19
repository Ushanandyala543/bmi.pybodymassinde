w=eval(input("Enter weight in kg:"))
m=eval(input("Enter height if inches -->0 or cm -->1:"))
if(m==0):
    h=eval(input("enter the height:"))
    h=m*0.0254
else:
    h=eval(input("enter the height:"))
    h=m*0.01
bmi=w/(h*h)
bmi=int(bmi)
if(bmi<18.5):
    print("UNDER WEIGHT")
elif(bmi>=18.5 and bmi < 25):
    print("HEALTHY WEIGHT")
elif(bmi>=25.0 and bmi<30):
    print("OVERWEIGHT")
elif(bmi>=30.0):
    print("OBESITY")

