from datetime import datetime

def convert_to_yyyy_mm_dd(date_string):
    date_obj = datetime.strptime(date_string, '%Y-%m-%d')
    return date_obj.date()

#createFecha('2022','05','22')