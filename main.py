from datetime import datetime, date, time
import json

with open(file_dump.json, 'w', encoding = 'utf-8') as f:
  json.dump([], f)

def dump_file(old_function):
  def new_function(*args, **kwargs):
    date = str(datetime.date.now())
    time = str(datetime.time.now())
    file_load = f'Дата: {date}, Время: {time}, Название функции: {old_function.__name__}, Args: {str(args)}, Kwargs: {str(kwargs)}'
    print(file_load)
    with open(file_dump, 'a', encoding = 'utf-8') as f:
      json.dump(file_load, f, ensure_ascii = False, indent = 4)


    


  

