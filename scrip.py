import json
import os
import fileinput
import datetime
from dateutil.parser import *
# dir_name=r'C:\Users\neeraj.shukla\Downloads\sqldata\sqldata'
dir_name=r'C:\Users\Neeraj\Desktop\abc\sqldata'

# conn=psycopg2.connect("
#                     dbname=sales
#                     host=redshifttest-xyz.cooqucvshoum.us-west-2.redshift.amazonaws.com
#                     port=5439
#                       user=master
#                     password=secret
#                     ")




def handleDate(dateVal):
    if dateVal == "today":
        dateVal = datetime.datetime.now().date()
        dateVal = dateVal.strftime('%m-%d-%Y')
        return dateVal
    elif dateVal == "tommorow":
        dateVal = datetime.datetime.now().date()
        DD = datetime.timedelta(days=1)
        dateVal = dateVal + DD
        dateVal = dateVal.strftime('%m-%d-%Y')
        return dateVal
    elif dateVal == "yesterday" :
        dateVal = datetime.datetime.now().date()
        DD = datetime.timedelta(days=1)
        dateVal = dateVal - DD
        dateVal = dateVal.strftime('%m-%d-%Y')
        return dateVal
    else :
        return dateVal


def data_convert():

    """ Loading the configurational data """
    with open("sqldata/ConfigurationJson.json") as f:
        file = f.read()
        loaded_json = json.loads(file)
        """ Extracting the attribute and it's value"""
        for x in loaded_json:
            data = loaded_json[x]
            for file_number in range(len(data)):
                file_detail = data[file_number]
                file_name = file_detail["fileName"]
                attribute_list = file_detail['AttributeList']
                file_loc = os.path.join(dir_name,file_name)
                query = get_query(file_loc ,attribute_list )
                print(query)





def get_query(file_loc , attribute_list):
    with open(file_loc) as f:
        content = f.read()
        print(content)
        for attr_num in range(len(attribute_list)):
                attribute = attribute_list[attr_num]
                att_name = attribute['name']
                att_value = attribute['Value']
                att_value = handleDate(att_value)
                if att_name in content:
                    content = content.replace(att_name , att_value)
        return content


# def script(conn , query ):
#     try :
#         cur = con.cursor()
#         cur.execute("query")
#         cur.close()



if __name__=="__main__" :
    data_convert()
    # print(data)
#     handleDate("tommorow")
