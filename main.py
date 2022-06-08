import sqlite3
db=sqlite3.connect("veritabanı.db")
veriler=[
(12,45,89),
(45,68,72),
(56,77,35),
(98,34,15),
]

imlec=db.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS 'hayat boş ' (yas,kilo,boy)")
for veri in veriler:


    imlec.execute("INSERT INTO 'VR' VALUES (?,?,?)",veri)
db.commit()
db.close()