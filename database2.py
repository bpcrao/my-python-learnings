import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="root", host="127.0.0.1", port="5432")
cur = con.cursor()
cur.execute("INSERT INTO public.resource(id, name, permission, authority_name) VALUES (1111,'test', 2, 'test' )")
con.commit()
con.close()
