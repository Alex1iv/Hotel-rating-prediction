import re 

def get_address(arg:str):
    """Get country and address from the given string
    Args:
    -------
    arg (str): строка с адресом

    Returns:
    -------
    country, city: (str)
    """    
    arg = arg.split()

    def get_country():
        if arg[-1]=='Kingdom':
            country = arg[-2] + ' '+ arg[-1]
            
        else:
            country = arg[-1]
        return country
    country = get_country()

    def get_city():
        if arg[-1]=='Kingdom':
            city = arg[-5]     
        else:
            city = arg[-2]
        return city
    city = get_city()

    return(country, city)


def get_neutral_from_negative(arg:str)->str:
    """Categorize neutral feedback from positive

    Args:
        arg (str): DataFrame string

    Returns:
        _str_: either neutral or argument
    """    
    arg = arg.lower().replace(r'\w .+', '').replace('the ', '').replace('was', 'is').replace('were', 'are')\
        .replace('too | a bit', '').replace('too', 'is').replace('a bit ', '').replace('a little ', '').replace('very ', '').replace('is is', 'is') 

    neutral = ['no negative', 'na', 'nothing at all', 'nil', 'n a', 'none', 'none ', 'no complaints', 'no complaints ',\
        'nothing to dislike', 'nothing really', 'nothing really ', 'can t think of anything', 'absolutely nothing', \
        'absolutely nothing ', 'nothing not to like', 'nothing to dislike', 'nothing at all', 'nothing at all ', \
        'nothing to complain about', 'no', 'non', 'not much', 'there is nothing i didn t like', 'nothing in particular', \
        'nothing comes to mind', 'not applicable', 'there is nothing to dislike', 'not a thing', 'nothing to report', \
        'weather', 'no thing', 'no negatives']
    

    if arg in neutral or arg==' ' or arg=='nothing ' or arg=='nothing' or 'no complaints' in arg:    # counts neutral feedbacks
        return ' ' 

    else:
        return arg # the rest feedbacks are unchanged


def get_traveller(tag:str)->str:
    """Extract traveller type from the Tag
    
    """
    try:
        tag_list = tag.split(',')
        traveller_type = tag_list[1]
        traveller_type = re.sub(r'[\']', '', traveller_type)
        traveller_type = re.sub(r'^\s|\s$', '', traveller_type)
        return traveller_type
    
    except IndexError:
        return None
    
def get_trip_type(tag:str)->str:
    """Travel type extraction from the Tag
    """
    tag_list = tag.split(', ')
    trip_type = tag_list[0]
    
    if 'Leisure trip' in trip_type:
        return 'Leisure trip'
    elif 'Business trip' in trip_type:
        return 'Business trip'
    elif 'Couple' in trip_type:
        return 'Couple'
    elif 'Solo' in trip_type:
        return 'Solo traveler'
    elif 'Family' in trip_type:
        return 'Family'
    elif 'Group' in trip_type:
        return 'Group'
    elif 'pet' in trip_type:
        return 'With a pet'
    elif 'friends' in trip_type:
        return 'Group'
    else:
        return ' Other'


def get_stay_length(arg:str)->int:
    """Extraction of stay duartion from the tag
    """
    
    # Detect digits usin the pattern 'Stayed D'
    length = re.findall(r'(?<=Stayed )\d+', arg)
    
    # Check digits number
    if len(length) == 1:
        return int(length[0])
    else:
        return 0 # return 0 if there was no digits found
    

def get_room_type_prep(tag:str)->str:
    """Extration of the room type from the Tag
    """
    try:
        tag_list = tag.split(',')
        room_type = tag_list[2]
        room_type = re.sub(r'[\']', '', room_type)
        room_type = re.sub(r'^\s|\s$', '', room_type)
        return room_type
    
    except IndexError:
        return None
    
def get_room_type(description:str)->str:
    """ Unification of room types
    """
    description_list = description.split(' ')
    
    if 'Double' in description_list:
        return 'Double Room'
    elif 'Single' in description_list:
        return 'Single Room'
    elif 'Triple' in description_list:
        return 'Triple Room'
    elif 'Family' or 'children' in description_list:
        return 'Family Room'
    elif 'King' or 'Queen' in description_list:
        return 'King Room'
    elif 'Twin' in description_list:
        return 'Twin Room'
    elif 'Apartment' in description_list:
        return 'Apartment'
    elif 'Standard' in description_list:
        return 'Standard Room'
    elif 'Deluxe' in description_list:
        return 'Deluxe Room'
    elif 'Rooms' or 'rooms' in description_list:
        return 'Several Rooms'
    elif 'Suite' in description_list:
        return 'Suite'
    elif 'Stayed' in description_list:
        return 'Other'
    else:
        return description
    
    
# def get_sort_features(data:pd.DataFrame):
#     """Функция определения типа признаков в датафрейме
#     Args:
#     ------
#     data (pd.DataFrame): датафрейм в формате Pandas
#     """    
#     categorical_columns_names = list() 
#     numerical_columns_names = list() 

#     for i in data.columns:
#         numeric_formats = [np.int16, np.int32, np.int64, np.float16, np.float32, np.float64]  # список числовых типов 'int64' или 'float64'
#         if data[i].dtypes in numeric_formats: 
#             numerical_columns_names.append(i)
#         else:
#             categorical_columns_names.append(i)
            
#     #print(f'There are {len(categorical_columns_names)} categorical features:')
    
#     #for count, value in enumerate(categorical_columns_names, start=1): # list features from 1
#        # print(count, value)
#     return categorical_columns_names, numerical_columns_names

        
# def get_negative_reasons(arg:str)->str:
#     """Категорирование негативных отзывов

#     Args:
#         arg (str): строка датафрейма

#     Returns:
#         _type_: _description_
#     """    
#     arg = arg.lower().replace(r'\w .+', '').replace('the ', '').replace('was', 'is').replace('were', 'are').replace('too | a bit', '').replace('too', 'is').replace('a bit ', '').replace('a little ', '').replace('very ', '').replace('is is', 'is') 

#     neutral = ['no negative', 'na', 'nothing at all', 'nil', 'n a', 'none', 'none ', 'no complaints', 'no complaints ',\
#         'nothing to dislike', 'nothing really', 'nothing really ', 'can t think of anything', 'absolutely nothing', \
#         'absolutely nothing ', 'nothing not to like', 'nothing to dislike', 'nothing at all', 'nothing at all ', \
#         'nothing to complain about', 'no', 'non', 'not much', 'there is nothing i didn t like', 'nothing in particular', \
#         'nothing comes to mind', 'not applicable', 'there is nothing to dislike', 'not a thing', 'nothing to report', \
#         'weather', 'no thing', 'no negatives']
    
#     unidentified = ['all', 'everything']
    
#     positive = ['i liked everything', 'liked everything', 'nothing it is perfect', 'having to leave', 'leaving', 'all good', 'all is good', 'everything is perfect', ' lovely', 'everything is good', 'everything is great', 'everything is fine', 'nothing everything is perfect' , 'nothing all good', 'as above', 'see above' ]
    
#     service = ['staff', 'service', ]
    
#     room_price = ['price','expensive', 'pricey','cost']
    
#     food_price = ['price of breakfast', 'expensive breakfast', 'breakfast expensive', 'breakfast is expensive', 'breakfast too expensive', 'breakfast not included', 'breakfast is poor' ]
    
#     menu = ['breakfast', 'poor breakfast','breakfast could be better', ]
    
#     room_properties = ['room', 'pillows', 'bathroom', 'size of room', 'room size', 'room is hot', 'room is cold']
    
#     parking = ['no parking', 'parking']
    
#     noise = ['noisy', 'noise', 'loud']
    

#     if arg in positive or ('lovely' or 'no complaints') in arg or 'all good' in arg:         # count positive feedbacks if any
#         return 'positive'

#     elif ('everything' or 'all') and ('great' or 'good' or 'excellent' or 'perfect' or 'fine' or 'lovely') in arg:         # count positive feedbacks if any
#         return 'positive' 
 
           
#     elif arg in neutral or arg==' ' or arg=='nothing ' or arg=='nothing' or 'no complaints' in arg:    # count neutral feedbacks
#         return 'neutral' 

#     elif arg in unidentified:
#         return 'negative' #'unidentified_bad'
    
#     elif arg in room_properties or \
#         ('bed' or 'bathroom' or 'sheets') in arg or \
#         ('room' or 'rooms' or 'bed' or 'beds' or 'bathroom') in arg and ('small' or 'size' or 'big' or 'hot' or 'cold' or 'is tiny') in arg:
        
#         return 'bad_room_properties'
    
#     elif arg in service or 'stuff' in arg:
#         return 'poor_service'
    
#     elif arg in menu or arg=='food':
#         return 'poor_menu'
    
#     elif 'gym' in arg:
#         return 'no_gym'
    
#     elif 'location' in arg:
#         return 'bad_location'
    
#     elif ('wifi' or 'internet') in arg:
#         return 'internet_problems'
    
#     elif arg in noise or ('noise' or 'noisy') in arg:
#         return 'noise'

#     elif arg in room_price:
#         return 'high_room_price'
        
#     elif arg in food_price or 'breakfast' and ('price' or 'expensive' or 'not included' or 'poor') in arg :
#         return 'high_food_price'
    
#     elif arg in parking or 'parking' in arg:
#         return 'poor_parking'
       
#     else:
#         return 'negative' #'other_negative_reasons'   # the rest feedbacks are other
    
    
# def get_positive_reasons(arg):
#     arg = arg.lower().replace(r'\w .+', '').replace('the ', '').replace('was', 'is').replace('were |are very ', 'are').replace('too | a bit', '').replace('is very|is too|is a bit|', 'is').replace(r'gerat|friendly|is excellent|comfy | comfy', 'good').replace('comfy', 'good').replace('is good|is excellent|is perfect', 'good')
    
#     neutral = ['no positive', 'nothing', 'not much']
    
#     location = ['great location', 'good location', 'location is great','excellent location', 'position']
    
#     positive = ['everything', 'everything is perfect', 'all', 'everything is good', 'every thing', 'everything is excellent', 'all good', 'everything is great', 'excellent', 'prefect', 'perfect ','all of it']
    
#     clean = ['clean','cleanliness', 'very clean','clean room' ]

#     room_properties = ['bed', 'nice room']
    
#     if arg in neutral:    # count neutral feedbacks
#        return 'neutral' 

#     elif arg in location or 'location' in arg:  # 
#         return 'positive' #'location'
    
#     elif 'staff' in arg:
#        return 'positive' #'staff'
    
#     elif arg in room_properties or 'bed' in arg or 'room' in arg:
#        return 'positive' #'room_properties'
   
#     elif 'service' or 'staff' in arg:
#        return 'positive' #'service'
    
#     elif 'breakfast' in arg:
#        return 'positive' #'breakfast'
  
#     elif arg in positive:
#         return 'positive' #'positive'
    
#     elif arg in clean:
#         return 'positive' #'clean'
    
#     else:
#         return arg   # the rest are negative feedbacks
    
    
# def get_address(arg:str):
#     """Get country and address from the given string
#     Args:
#     -------
#     arg (str): строка с адресом

#     Returns:
#     -------
#     country, city: (str)
#     """    
#     arg = arg.split()

#     def get_country():
#         if arg[-1]=='Kingdom':
#             country = arg[-2] + ' '+ arg[-1]
            
#         else:
#             country = arg[-1]
#         return country
#     country = get_country()

#     def get_city():
#         if arg[-1]=='Kingdom':
#             city = arg[-5]     
#         else:
#             city = arg[-2]
#         return city
#     city = get_city()

#     return(country, city)