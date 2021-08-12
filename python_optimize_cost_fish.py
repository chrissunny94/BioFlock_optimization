Number_of_fish = 1200
Fish_consumed = 0


print("Initial Number_of_fish:",Number_of_fish,"Fish_consumed:",Fish_consumed)


Weight_appriciation= 70 
#time= 3 #months
count = 183

Total_amount = 0

for month in range(3,10):
    print(month,"th month")
    if Fish_consumed<Number_of_fish:
        count = count - 10
        Fish_consumed = Fish_consumed + count
        Total_weight=(Weight_appriciation*(month)*count)/1000
        
        Cost_function=Total_weight*200
        Total_amount = Total_amount+Cost_function
        print("count:",count,"Total_weight:",Total_weight,"AvgWeight:",float(1000*Total_weight/count))
        print("Total_Fish_consumed:",Fish_consumed,"Cost soldat",float(Cost_function))


print("Total collection:",Total_amount)
