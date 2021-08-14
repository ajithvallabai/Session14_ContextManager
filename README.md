### Assignment - Session 14 - Context Manager

Google Colab link - [here](https://colab.research.google.com/drive/1LmQqN6XqAfef4nJ0014kBKswD_sMo96o?usp=sharing)

### Goal 1

```
def read_file(file_name):
    with open(file_name) as f:
        rows = csv.reader(f, delimiter=',', quotechar='"')
        yield from rows

def excel_data(name, filename):
    data = read_file(filename)
    header = namedtuple(name ,next(data))
    for each in data:
        yield header(*each)
```
We have to form a iterator for each dataset. so with read_file we are using a context manager and creating a generator. from it we are taking the first data as header .Next we are using forloop and yield to form a iterator.When we feed name of the namedttuple and file location 

### Goal 2

```
def combine_data_iter(*data_tup):
    combined_datas = {}    
    for each in data_tup:        
        list_key = each._asdict()        
        combined_datas.update(list_key)        
    head = namedtuple("combined_data",combined_datas.keys())
    yield head(*combined_datas.values())

def combined_data(data):
    for each in zip(*data):
        yield from combine_data_iter(*each)
```

For combining four named tuples and generate a iterator, we are forming a iterator combined_data(). In combined_data we are using a helper function combine_data_iter() . In combine_data_iter() we are iterating all 4 tuples parallelly as got from the zip function. We are using ._asdict() to convert named tuple to dictionary . In dictionary keys with same name will get combined and all keys should be unique so it ssn number will be present only once at the result. form the dictionary we are forminga new named tuple with combined_data as tuple name.


### Goal 3

```
def updated_set(gen_data):
    anchor_date = datetime.datetime(2017, 3, 1, 0, 0, 00)
    result_data = []
    for each in gen_data:
        d1 = datetime.datetime.strptime(each.last_updated,"%Y-%m-%dT%H:%M:%SZ")
        if d1 > anchor_date:            
            yield each
```

From the coimbined data we are forming a iterator and it will return a data only when the update status is greater than (3/1/2017) . Thus we are accomplishing 3rd goal.


### Goal 4

```
def find_popular_car(gen_data):
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
```

From the combined data we are iterating over the list and we are forming seperate dictionary counter for "male" and "female" to calculate popular car.At last we are finiding the keys that is having maxmium values and returing it in a dictionary. 
