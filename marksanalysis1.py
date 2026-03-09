import csv
months=[]
sales=[]
expense=[]
profit=[]
file=r"C:\Users\LENOVO\OneDrive\Desktop\student.csv"
with open(file,'r') as ff:
     marksanalyse=csv.reader(ff)
     lis=list(marksanalyse)
     for x in lis[1:]:
          months.append(x[0])
          sales.append((int(x[1])))
          expense.append(int(x[2]))
          profit.append(int(x[3]))
print("total sales is",sum(sales))
import matplotlib.pyplot as p
p.plot(months,sales,marker="o")
p.title("MONHTHS VS SALES GRAPH",color="brown")
p.xlabel("months")
p.ylabel('sales')
p.show()
p.bar(months,expense,color='y')
p.xlabel("months")
p.ylabel("expense")
p.title("months vs expense")
p.show()
p.plot(months,sales,marker="o",label="sales")
p.plot(months,expense,marker="o",label='expense')
p.title("sales vs expense")
p.xlabel("months")
p.legend()
p.show()
p.scatter(sales,expense)
p.xlabel("Sales")
p.ylabel("expense")
p.title("SALES VS expense")
p.show()
p.pie(sales,labels=months,autopct="%1.1f%%")
p.title("sales by months",size=40)
p.show()
maxsale=max(sales)
print(maxsale)
maxindex=sales.index(maxsale)
print("months with highest sales is",months[maxindex])
minprofit=min(profit)
minprofitindex=profit.index(minprofit)
print("months with lowest profit is",minprofit)
print("AVERAGE SALES IS", sum(sales)/len(sales))
print("TOTAL EXPENSE IS", sum(expense))
mp=[]
for x,y in zip(months,profit):
     if y>10000:
          mp.append(x)
print("MONTHS WITH PROFIT GREATER THAN 10000 are",mp) 

          
     


     
     