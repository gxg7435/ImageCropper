import mysql.connector
import requests
import json
import pandas as pd

def makeConnection():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root"
  )
  return mydb

def createDB(mydb):
  mycursor = mydb.cursor()
  mycursor.execute("CREATE DATABASE ImageCropper")

def useDB(mydb):
  mycursor = mydb.cursor(buffered=True)
  mycursor.execute("use imagecropper")
  return mycursor

def getData(id):
  url = 'http://data.tmsapi.com/v1.1/programs/' + id + '?api_key=kqtwdcapd2a5hth6aqw4h65f'
  content = requests.get(url).content
  dataset = json.loads(content.decode('utf-8'))
  print(dataset)
  dfObj = pd.DataFrame(list(dataset.items()))
  #print(dfObj)
  return dataset

def createTable(mycursor):
  mycursor.execute('create table programs(rootId int primary key,'
                   'tmsId varchar(50), title varchar(50), episodeTitle varchar(50),'
                   'releaseYear int, releaseDate date, shortDescription varchar(50),'
                   'longDescription varchar(100), seasonNum int)')


def insertData(mycursor,dataset,mydb):
   if('seasonNum' not in dataset):
     dataset['seasonNum'] = 0

   val = (dataset['rootId'],dataset['tmsId'],dataset['title'],dataset['episodeTitle'],dataset['releaseYear'],dataset['releaseDate'],dataset['shortDescription'],dataset['longDescription'],dataset['seasonNum'],)
   sql = "INSERT INTO programs (rootId,tmsId,title,episodeTitle,releaseYear,releaseDate,shortDescription,longDescription,seasonNum) " \
         "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

   mycursor.execute(sql, val)
   mydb.commit()

def fetchData(mycursor):
  mycursor.execute("select * from programs")
  for row in mycursor.fetchall():
    print(row)

def modify_table(dataset,mycursor,mydb):
    casts = dataset['cast']
    temp = [None for i in range(3)]
    if(len(casts) >= 3):
      for i in range(3):
        temp[i] = casts[i]['name']
    else:
      for i in range(0,len(casts)):
        temp[i] = casts[i]['name']
    print(temp)

    mycursor.execute('alter table programs add (castOne varchar(50),castTwo varchar(50),castThree varchar(50))')
    sql = "UPDATE programs SET castOne = %s,castTwo = %s,castThree = %s WHERE rootId = %s"
    val = (temp[0], temp[1], temp[2], dataset['rootId'])

    mycursor.execute(sql, val)
    mydb.commit()

def main():
  imageIds = ['15171223','16381191','15481959','17462348']
  mydb = makeConnection()

  createDB(mydb)
  mycursor = useDB(mydb)
  createTable(mycursor)

  for val in imageIds:
    dataset = getData(val)
    insertData(mycursor,dataset,mydb)
    modify_table(dataset, mycursor, mydb)
  fetchData(mycursor)

if __name__ == '__main__':
  main()

