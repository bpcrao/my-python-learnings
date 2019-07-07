import records

db = records.Database("postgresql://postgres:root@localhost/postgres")
rows = db.query('SELECT * FROM public.jhi_user')

for row in rows:
    print(row)

