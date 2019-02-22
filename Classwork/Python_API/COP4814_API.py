#This lecture was developed by Dr Gregory Reis using NASA API available at: https://api.nasa.gov/ and http://open-notify.org/
#September 2018
#Libraries:
import json
import requests

#define a function to save to a json file
#the two arguments are: the data to be saved and the name for the json file (don't forget to include .json)
def save_to_file(data,file_name):
    with open(file_name,'w') as write_file:
        json.dump(data,write_file,indent=4)
        print('The file {0} was successfully created.'.format(file_name))

#define a function to read from a json file
#the only argument is: the name of the json file which you want to read
#the return of the function is the the variable to which you assigned the json file
def read_from_file(file_name):
    with open(file_name,'r') as read_file:
        file=json.load(read_file)
        print('You successfully read from {0}.'.format(file_name))
        return file

#####################################################################################################################
#############Example 1 - How many humans are in space right now?:
print('\n')
print('#############Example 1 - How many humans are in space right now?: \n')

#We will request data from the following URL:
url1 = "http://api.open-notify.org/astros.json"

#Let's make a query this API and save the output to astronauts_json:
astronauts_json=requests.get(url1).json()

#next, we should save this data into a json file
#for that, let's create a name for the json file:
astronauts_file_name='astronauts.json'

#let's now save it to a json file:
save_to_file(astronauts_json,astronauts_file_name)

#Good! Now you should see your json file in the folder of this project =D
#let's now read this data from the json file that we just created and save to a variable:
astronauts_in_space=read_from_file(astronauts_file_name)

#At this point, you already know that Python read the json file as a dictionary type, so to confirm that it did that:
print('The type of the astronauts_in_space is: ', type(astronauts_in_space))

#You should have seen 'dict' as the type. Awesome.
#Now you are ready to access the values stored in this dictionary
#To print the keys of this dictionary:
print('The keys are: ',astronauts_in_space.keys())

#To print the values under key 'people':
print('The people in space are: ',astronauts_in_space['people'])

#To print how many people are in space:
print('There are {0} people in space now.'.format(astronauts_in_space['number']))

print('\n')
#To print only the names:
print('The names of the people in space are: ')
for i in astronauts_in_space['people']:
    print(i['name'])

print('\n')
#To print the names in alphabetical order:
print('The names of people in space (in alphabetical order of their first name): ')
for j in sorted(astronauts_in_space['people'],key=lambda i:i['name']):
    print(j['name'])

#####################################################################################################################
#############Signing up for NASA's API:
print('\n')
print('#############Signing up for NASA\'s API: \n')

#I believe we are ready to see the picture of the day by NASA.
#But before we move to the next two examples, we need to have an API key for the requests
#Please visit https://api.nasa.gov/
#Scroll down to 'Get Your API Key' - use your FIU email
#You should get a key
#Now you need to create a .json file and paste your API key in it
#Done?
#If not, then go ahead and create a json file that stores that API key
#If yes, then:
#Let's access this API key by reading it from the json file you just created
#Just call the "read_from_file" function above providing the name of the json file that contains your API key:
api_key=read_from_file("api_key.json")

#since you read from a json file and saved to the variable api_keys, api_keys is a dictionary =D
#To confirm this, please print the type of api_keys:
print('The type of my_api_key is: ',type(api_key))

#now, from this dictionary, you need to read you API key
#remember that the API key is a value which is accessed through a dictionary key
#in this example the access key to the API key value is nasa_api_key (check the api_keys.json)
#so let's access the value of API key using the access key nasa_api_key and save to a variable:
my_nasa_api_key=api_key['nasa_api_key']

#again:
## api_keys is the name of the dictionary that you read from a json file
## nasa_api_key is the key of the dictionary that access the value of your API key
## my_nasa_api_key is the variable to sabe the value of your API key

#my_nasa_api_key is your API key as a string =D
print('My API key provided by NASA is: ',my_nasa_api_key)

#####################################################################################################################
#############Example 2 - Astronomy Picture of the Day (APOD) API:
print('\n')
print('#############Example 2 - Astronomy Picture of the Day (APOD) API: \n')

#We will request data from the following URL:
#Notice that the link is cut right after the equal sign related to the api_key
#This is because your API key is unique, no one else has that same value
#Therefore we need to concatenate the following links to your API key
url2='https://api.nasa.gov/planetary/apod?api_key='

#let's concatenate the above url with your API key
url_planetary=url2+my_nasa_api_key

#now let's make a query this API and save the output to variable planetary_json:
#planetary_json=requests.get(url_planetary).json()

#next, we should save this data into a json file
#for that, let's create a name for the json file:
planetary_json_file_name='planetary.json'

#let's now save it to a json file:
#save_to_file(planetary_json,planetary_json_file_name)

#Good! Now you should see your json file in the folder of this project =D
#let's now read this data from the json file that we just created and save to a variable:
picture_of_day_nasa=read_from_file(planetary_json_file_name)

#At this point, you already know that Python read the json file as a dictionary type, so to confirm that it did that:
print('The type of the picture_of_day_nasa is: ', type(picture_of_day_nasa))

#You should have seen 'dict' as the type. Awesome.
#Now you are ready to access the values stored in this dictionary
#To print the keys of this dictionary:
print('The keys are: ',picture_of_day_nasa.keys())

#To print the title of the picture of the day:
print('The title of the picture of the day is: ', picture_of_day_nasa['title'])

#To print the data of the picture of the day:
print('The date of the picture of the day is: ', picture_of_day_nasa['date'])

#To print the url of the picture of the day:
print('The url of the picture of the day is: ', picture_of_day_nasa['url'])

#I believe we are ready to see some beautiful images of Mars. Ready? Let's move to example 3.

#####################################################################################################################
#############Example 3 - Mars Rover Photos API:
print('\n')
print('#############Example 3 - Mars Rover Photos API: \n')

#We will request data from the following URL:
#Notice that the link is cut right after the equal sign related to the api_key
#This is because your API key is unique, no one else has that same value
#Therefore we need to concatenate the following links to your API key
url2="https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key="

#let's concatenate the above url with your API key
url_mars=url2+my_nasa_api_key

#now let's make a query this API and save the output to variable mars_json:
#mars_json=requests.get(url_mars).json()

#next, we should save this data into a json file
#for that, let's create a name for the json file:
mars_json_file_name='mars_pictures.json'

#let's now save it to a json file:
#save_to_file(mars_json,mars_json_file_name)

#Good! Now you should see your json file in the folder of this project =D
#let's now read this data from the json file that we just created and save to a variable:
mars_pictures=read_from_file(mars_json_file_name)

#At this point, again, you already know that Python read the json file as a dictionary type, so to confirm that it did that:
print('The type of the mars_pictures is: ', type(mars_pictures))

#You should have seen 'dict' as the type. Awesome.
#Now you are ready to access the values stored in this dictionary
#To print the keys of this dictionary:
print('The keys are: ',mars_pictures.keys())

#There is only one key, right? What does this key hold? Let's print its type:
print(type(mars_pictures['photos']))

#It's a list, a list of what? Of dictionaries and each dictionary contains all the information for one picture
#Let's print the keys of the first dictionary:
print('The keys are: ', mars_pictures['photos'][0].keys())

#To print how many pictures (or how many dictionaries since each dictionary refers to one picture):
print('There are {0} pictures available! :)'.format(len(mars_pictures['photos'])))

#To print the url to one of these pictures:
print('The url for one of the pictures is: ',mars_pictures['photos'][5]['img_src'])

#To print the name of the camera of the first picture:
print('The camera used for the first picture is named: ',mars_pictures['photos'][0]['camera']['name'])

#To print the camera full name for all pictures:
for i in mars_pictures['photos']:
    print(i['camera']['full_name'])

#To print the url of pictures taken from a specific camera:
print('The urls for pictures taken from this camera are:')
for j in mars_pictures['photos']:
    if j['camera']['name']=='FHAZ':
        print(j['img_src'])

#Once you request data from the API and saved to a json file, you don't need to do these two things again
#Therefore, don't forget to comment lines 122, 129, 169 and 176; otherwise, everytime you run this code, it will make a new request
#Good news! You made it!
#Questions? Email me or stop by during office hours. I will be happy to go over the code with you. =D