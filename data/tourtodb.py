from data.models import db, Tour
from data import data


def data_to_db():
    for tour in data.tours.values():
        tour_db = Tour(**tour)
        db.session.add(tour_db)

    db.session.commit()
    print("Дані успішно перенесено")