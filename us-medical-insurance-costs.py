print("\n  \n")
#import insurance csv file for dictionary
import csv
import collections

#create lists
insurance_export_list = []
id_list = []

#importing csv file to get data
with open('C:\\Users\\seani\\AppData\\Local\\Temp\\Temp1_python-portfolio-project-starter-files.zip\\python-portfolio-project-starter-files\\insurance_csv_project.csv') as insurance_csv_file:
    temp_insurance_dict = csv.DictReader(insurance_csv_file)
    for i in temp_insurance_dict:
        insurance_export_list.append(i)

for i in range(len(insurance_export_list)):
    id_list.append(i)

#give each person an id for unique identifier and close csv file since data is extracted
insurance_dict = {key:value for key,value in zip(id_list, insurance_export_list)}

#function declaration
def average_age():  
    total_age = 0
    for id in id_list:
        total_age += int(insurance_dict[id]["age"])
    average_age = round(float((total_age) / (len(id_list))), 3)
    return average_age

def gender_split():
    female = 0
    male = 0
    for id in id_list:
        if insurance_dict[id]["sex"] == "female":
            female += 1
        elif insurance_dict[id]["sex"] == "male":
            male += 1
        else:
            return 'Error'
    female_as_percent = float(100) * float(female/len(id_list))
    male_as_percent = float(100) - female_as_percent
    return female, male, female_as_percent, male_as_percent

def average_bmi():
    total_bmi = 0
    for id in id_list:
        total_bmi += float(insurance_dict[id]["bmi"])
    average_bmi = round(float((total_bmi) / (len(id_list))), 3)
    return average_bmi

def age_range():
    min_age = int(insurance_dict[0]["age"])
    max_age = int(0)
    for id in id_list:
        if int(insurance_dict[id]["age"]) > max_age:
            max_age = int(insurance_dict[id]["age"])
        elif int(insurance_dict[id]["age"]) < min_age:
            min_age = int(insurance_dict[id]["age"])
    unique_age_list = []
    for id in id_list:
        if insurance_dict[id]["age"] not in unique_age_list:
            unique_age_list.append(insurance_dict[id]["age"])
    if (1 + max_age - min_age) == len(unique_age_list):
        is_unique_age = True
    else:
        is_unique_age = False
    return min_age, max_age, is_unique_age

def age_count():
    age_dict = {}
    for id in id_list:
        age_dict_key = insurance_dict[id]["age"]
        if age_dict_key not in age_dict:
            age_dict[age_dict_key] = 1
        elif age_dict_key in age_dict:
            age_dict[age_dict_key] += 1
    return age_dict

def from_direction():
    south_west_count = 0
    south_east_count = 0
    north_west_count = 0
    north_east_count = 0
    for id in id_list:
        if 'north' in insurance_dict[id]["region"]:
            if 'west' in insurance_dict[id]["region"]:
                north_west_count += 1
            else:
                north_east_count += 1
        elif 'west' in insurance_dict[id]["region"]:
            south_west_count += 1
        else:
                south_east_count += 1
    return south_west_count, south_east_count, north_west_count, north_east_count

#getting variables from functions
female_insurance_users, male_insurance_users, female_insurance_users_as_percent, male_insurance_users_as_percent = gender_split()
lowest_age, highest_age, unique_ages = age_range()
age_dictionary = age_count()
south_west_users, south_east_users, north_west_users, north_east_users = from_direction()

#summarizing results with print statements
#categories (6) - age(str), sex(int), bmi(float), children(int), smoker(str), region(str), charges(float)
print("The average age for someone in our insurance database is about " + str(average_age()) + " years old.")
print("There are {female_insurance_users} female insurance users in our database. \nThere are {male_insurance_users} male insurance users in our database. \nFemales make up {female_insurance_users_as_percent}% of our insurance database. \nMales make up {male_insurance_users_as_percent}% of our insurance database.".format(female_insurance_users=female_insurance_users,male_insurance_users=male_insurance_users,female_insurance_users_as_percent=round(female_insurance_users_as_percent,3),male_insurance_users_as_percent=round(male_insurance_users_as_percent,3)))
print("The average bmi of our clients is " + str(average_bmi()) + ".")
print("Our insurance company currently covers individuals from the ages of {lowest_age} to {highest_age} years old.".format(lowest_age=lowest_age,highest_age=highest_age))
if unique_ages == True:
    for id in range(lowest_age, highest_age+1):
        print("There are {number_of_people} people in our insurance data that are {age} years old.".format(number_of_people = age_dictionary[str(id)], age = id))
print("{south_west_users} users in our database are from the South West. \n{south_east_users} users in our database are from the South East. \n{north_west_users} users in our database are from the North West. \n{north_east_users} users in our database are from the North East.".format(south_west_users=south_west_users,south_east_users=south_east_users,north_west_users=north_west_users,north_east_users=north_east_users))
