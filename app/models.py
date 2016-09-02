from app import db

class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    dob = db.Column(db.String(10))
    identifier = db.Column(db.String(120))

    def __repr__(self):
        return '<Subject %r>' % (self.id)

class Interactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    type = db.Column(db.Integer)
    behaviourDescription = db.Column(db.String(200))
    location = db.Column(db.String(200))
    url = db.Column(db.String(200))

    def __repr__(self):
        return '<Interaction %r>' % (self.id)