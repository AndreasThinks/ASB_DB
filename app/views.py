from flask import render_template, session, redirect, request, flash, url_for, send_file
from app import app, db
from .forms import LoginForm, SearchForm
from .models import Subjects, Interactions
import csv


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    subjects = Subjects.query.all()
    subject_list = []
    for subject in subjects:
        subject_attributes = [subject.firstName, subject.surname, subject.dob, subject.identifier]
        subject_list.append(subject_attributes)
    if form.validate_on_submit():
        subject_list = []
        '''for subject in subjects:
            subject_attributes = [subject.firstName, subject.surname, subject.dob, subject.identifier]
            subject_list.append(subject_attributes)'''
        if form.firstName.data != "":
            subjects = Subjects.query.filter_by(firstName=form.firstName.data)
        if form.surname.data !="":
            subjects = Subjects.query.filter_by(surname=form.surname.data)
        if form.dob.data !="":
            subjects = Subjects.query.filter_by(dob=form.dob.data)
        if form.identifier.data !="":
            subjects = Subjects.query.filter_by(identifier=form.identifier.data)
        for subject in subjects:
            subject_attributes = [subject.firstName, subject.surname, subject.dob, subject.identifier]
            subject_list.append(subject_attributes)
        return render_template("search_subject.html", subjects=subject_list)
    return render_template("index.html",
                           subjects = subject_list,
                           title='Home',
                           form=form)


@app.route('/search_subject', methods=['GET', 'POST'])
def search_subject():
    return render_template("search_subject.html")

@app.route('/add_subject', methods=['GET', 'POST'])
def add_subject():
    form = SearchForm()
    if form.validate_on_submit():
        firstName = form.firstName.data
        surname = form.surname.data
        dob = form.dob.data
        identifier = form.identifier.data
        subject = Subjects(firstName=firstName, surname = surname, dob = dob, identifier = identifier)
        db.session.add(subject)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("add_subject.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])