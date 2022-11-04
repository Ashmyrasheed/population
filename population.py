import requests
import json
import mysql.connector
try:
    mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'populationdb')
    mycursor = mydb.cursor()
except mysql.connector.Error as e:
    print("sql connection error")
mycursor = mydb.cursor()
data = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population").text
data_info = json.loads(data)
for i in data_info["data"]:
       year =str("ID Year")
       Population =str(i['Population'])
        
       sql = "INSERT INTO `population` (`IDNation`,`Nation`,`IDYear`,`Population`,`SlugNation`) VALUES ('"+i['ID Nation']+"','"+i['Nation']+"','"+year+"','"+Population+"','"+i['Slug Nation']+"')"
       mycursor.execute(sql)
       mydb.commit()
       print("data inserted successfully")