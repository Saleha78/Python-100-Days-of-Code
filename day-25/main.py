import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
Black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(Grey_squirrel)
print(Black_squirrel)
print(red_squirrel)

squirrel_dict = {
    "Fur_color" : ["Grey", "Black", "Cinnamon"],
    "count":  [2473, 103, 392]
}

data = pandas.DataFrame(squirrel_dict)
data.to_csv("squirrel_count.csv")




# with open ("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)



# import csv
#
# with open("weather_data.csv") as csvfile:
#     data = csv.reader(csvfile)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#         print(row)
#
#   OR(both is doing same work)

# import pandas
# data = pandas.read_csv("./weather_data.csv")
# print(data["temp"])
#
# import pandas
#
# data = pandas.read_csv("./weather_data.csv")
# temp_list = data["temp"].to_list()
# average_temp = (sum(temp_list))/len(temp_list)
#
# print(f"average temperature :{average_temp:.2f}")
       #OR
# print(data["temp"].mean())

# print(data["temp"].max())

#Get data in columns
# print(data["condition"])
      #OR
# print(data.condition)

#Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# new_tem = monday.temp*9/5 + 32
# print(new_tem)

#create a dataframe from scratch
# data_dict = {
#     "student":["any","james","angela"],
#     "score":[76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# #creates new csv file in the project section
# data.to_csv("new_data.csv")











