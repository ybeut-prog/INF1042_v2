import datetime
maintenant = datetime.datetime.now()
dans_100_heures = maintenant + datetime.timedelta(hours=100)
print("Dans 100 heures, nous serons le :", dans_100_heures)