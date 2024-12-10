class multipleFunctions():
    def Subfields():
            print("Sub-fields in AI are:")
            print("Machine Learning")
            print("Neural Networks")
            print("Vision")
            print("Robotics")
            print("Speech Processing")
            print("Natural Language Processing")
            
    def OddEven():
            num=int(input("Enter a number: "))
            if(num%2==0):
                print(num,"is Even number")
            else:
                print(num,"is Odd number")
                
    def Eligible():
            gender=input("Your Gender: ")
            age=int(input("Your Age: "))
            if(gender=='Male' and age<21):
                print("NOT ELIGIBLE")
            elif(gender=='Female' and age<18):
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
                
    def percentage():
            Subject1= 98
            Subject2= 87
            Subject3= 95
            Subject4= 95
            Subject5= 93
            print("Subject1= 98")
            print("Subject2= 87")
            print("Subject3= 95")
            print("Subject4= 95")
            print("Subject5= 93")
            Total=Subject1+Subject2+Subject3+Subject4+Subject5
            print("Total: ",Total)
            Percent=(Total/500)*100
            print("Percentage: ",Percent)
            
    def triangle():
            Height=32
            Breadth=34
            Area=(Height*Breadth)/2
            print("Height:32")
            print("Breadth:34")
            print("Area formula: (Height*Breadth)/2")
            print("Area of triangle: ",Area)
            Height1=2
            Height2=4
            Breadth=4
            Perimeter=Height1+Height2+Breadth
            print("Height1:2")
            print("Height2:4")
            print("Breadth:4")
            print("Perimeter formula: Height1+Height2+Breadth")
            print("Perimeter of Triange: ",Perimeter)
