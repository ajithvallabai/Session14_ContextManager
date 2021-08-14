import session14
import pytest
import os

README_CONTENT_CHECK_FOR = [    
    "yield",
    "iterator",
    "popular car",
    "update status",
    "ssn"    
]
def test_goal1():
    data1 = session14.excel_data("Personal", 'data/personal_info.csv')
    data2 = session14.excel_data("Employment", 'data/employment.csv')
    data3 = session14.excel_data("UpdateStatus", 'data/update_status.csv')
    data4 = session14.excel_data("Vechiles", 'data/vehicles.csv')
    assert next(data1).ssn == "100-53-9824", "Please check your implementation"
    assert next(data1).ssn == "101-71-4702", "Please check your implementation"
    assert next(data2).ssn == "100-53-9824", "Please check your implementation"
    assert next(data2).ssn == "101-71-4702", "Please check your implementation"
    assert next(data3).ssn == "100-53-9824", "Please check your implementation"
    assert next(data3).ssn == "101-71-4702", "Please check your implementation"
    assert next(data4).ssn == "100-53-9824", "Please check your implementation"
    assert next(data4).ssn == "101-71-4702", "Please check your implementation"
    print("Goal 1 is satisfied. We are able to fetch all 4 datasets as iterators")


def test_goal2():
    data1 = session14.excel_data("Personal", 'data/personal_info.csv')
    data2 = session14.excel_data("Employment", 'data/employment.csv')
    data3 = session14.excel_data("UpdateStatus", 'data/update_status.csv')
    data4 = session14.excel_data("Vechiles", 'data/vehicles.csv')
    result = session14.combined_data((data1, data2, data3, data4))    
    out = next(result)
    assert out.ssn == "100-53-9824", "Please check your implementation"
    assert out.vehicle_make == "Oldsmobile", "Please check your implementation"
    assert out.employee_id == "29-0890771", "Please check your implementation"
    assert out.created == "2016-01-24T21:19:30Z", "Please check your implementation"
    print(out)
    print("Goal 2 is satisfied. We are able to combine all 4 datasets")

def test_goal3():
    data1 = session14.excel_data("Personal", 'data/personal_info.csv')
    data2 = session14.excel_data("Employment", 'data/employment.csv')
    data3 = session14.excel_data("UpdateStatus", 'data/update_status.csv')
    data4 = session14.excel_data("Vechiles", 'data/vehicles.csv')

    result = session14.combined_data((data1, data2, data3, data4))
    combined_data = session14.updated_set(result)
    total_extract = []
    for each in combined_data:
        total_extract.append(each)        
    assert len(total_extract) == 871, "Please check your implementation"
    print("Goal 3 is satisfied. We are able to extract datas that is after (3/1/2017 and its length is 871")


def test_goal4():
    data1 = session14.excel_data("Personal", 'data/personal_info.csv')
    data2 = session14.excel_data("Employment", 'data/employment.csv')
    data3 = session14.excel_data("UpdateStatus", 'data/update_status.csv')
    data4 = session14.excel_data("Vechiles", 'data/vehicles.csv')

    combined_result = session14.combined_data((data1, data2, data3, data4))
    popular_car = session14.find_popular_car(combined_result)    
    assert popular_car["male"] == ["Ford"], "Please check your implementation"
    assert popular_car["female"] == ["Ford","Chevrolet"], "Please check your implementation"
    print("Popular car among men",popular_car["male"])
    print("Popular car among women",popular_car["female"])
    print("Goal 4 is satisfied")


## Readme file - 2 test case

def test_readmeexists():
    assert os.path.isfile("README.md"), "README.md file missing!"
    print("Readme file exists")

def test_readmeproperdescription():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"
    print("Readme file contains proper description")
    