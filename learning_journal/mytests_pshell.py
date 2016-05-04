"""
unit Tests using pshell
"""

from sqlalchemy import engine_from_config
engine = engine_from_config(registry.settings, 'sqlalchemy.')
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
from learning_journal.models import Entry
session.query(Entry).all()

query = session.query(Entry)
type(query)

q1 = session.query(Entry)
for row in q1:
    print(row)
    print(type(row))

q2 = session.query(Entry.id, Entry.title, Entry.body, Entry.created, Entry.edited)
for id, title, body, created, edited in q2:
	print(id)	
	print(type(id))
	print(title)
	print(type(title))
	print(body)
	print(type(body))
	print(created)
	print(type(created))
	print(edited)
	print(type(edited))

session.query(Entry).get(1)
session.query(Entry).get(10)

new_model = Entry(id=1, title='first example', body='todo')
session.add(new_model)
new_model = Entry(id=2, title='second example', body='toto')
session.add(new_model)
session.commit()

session = Session()
session.query(Entry).count()

"""
Print all
"""
[(model.id, model.title, model.body, model.created, model.edited) for model in session.query(Entry)]

session.query(Entry).order_by(Entry.id.desc()).all()

"""
test classmethod all and by_id
"""
Entry.all(session)
Entry.by_id(session, 1)

[(model.id, model.title, model.body, model.created, model.edited) for model in Entry.all(session)]

