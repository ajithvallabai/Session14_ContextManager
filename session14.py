import csv
from collections import namedtuple
import datetime

def read_file(file_name) -> 'tuple' :
    """
    Reads a file and returns data one by one
    :param file_name: name of the file
    :param type: string
    :return rows: each row form csv file     
    """
    with open(file_name) as f:
        rows = csv.reader(f, delimiter=',', quotechar='"')
        yield from rows

def excel_data(name, filename) -> 'namedtuple' :
    """
    Forms a named tuple and returns each data
    :param name: tuple name
    :param type: string
    :param file_name: name of the file
    :param type: string
    :return namedtuple:  namedtuple   
    """
    data = read_file(filename)
    header = namedtuple(name ,next(data))
    for each in data:
        yield header(*each)

def combine_data_iter(*data_tup) -> 'namedtuple':
    """
    Combins given tuples and forms a new tuple and then returns a data
    :param data_tup: set of tuples
    :param type: tuple    
    :return namedtuple:  namedtuple   
    """
    combined_datas = {}    
    for each in data_tup:        
        list_key = each._asdict()        
        combined_datas.update(list_key)        
    head = namedtuple("combined_data",combined_datas.keys())
    yield head(*combined_datas.values())

def combined_data(data) -> 'namedtuple':
    """
    Using zip combined the tuple and returns a new tuple
    :param data: set of tuples
    :param type: tuple    
    :return namedtuple: namedtuple   
    """
    for each in zip(*data):
        yield from combine_data_iter(*each)


def updated_set(gen_data) -> 'namedtuple':
    """
    Yielding each data if the updated status is greater than (3/1/2017)
    :param gen_data: combined data
    :param type: tuple    
    :return namedtuple: namedtuple 
    """
    anchor_date = datetime.datetime(2017, 3, 1, 0, 0, 00)
    result_data = []
    for each in gen_data:
        d1 = datetime.datetime.strptime(each.last_updated,"%Y-%m-%dT%H:%M:%SZ")
        if d1 > anchor_date:            
            yield each

def find_popular_car(gen_data) -> 'dict':
    """
    Getting the combined data and forming a counter with it to find the popular car
    in men and women
    :param gen_data: combined data
    :param type: tuple    
    :return dict: dict of male and female key 
    """
    male_popular_car = {}
    female_popular_car = {}
    for each in gen_data:
        if each.gender == "Male":
            if each.vehicle_make in male_popular_car:
                male_popular_car[each.vehicle_make] += 1
            else:
                male_popular_car[each.vehicle_make] = 1
        elif each.gender == "Female":
            if each.vehicle_make in female_popular_car:
                female_popular_car[each.vehicle_make] += 1
            else:
                female_popular_car[each.vehicle_make] = 1    
    male_pop = [k for k, v in male_popular_car.items() if v == max(male_popular_car.values())]
    female_pop = [k for k, v in female_popular_car.items() if v == max(female_popular_car.values())]
    result = {"male": male_pop, "female":female_pop}    
    return result