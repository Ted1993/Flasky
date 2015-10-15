__author__ = 'xuqiangqiang'
# coding:utf-8

from flask import render_template,redirect,session,url_for
from . import main
from .forms import NameForm
from .. import  db
from ..models import User

@main.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['know'] = False
        else:
            session['know'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('main.index'))
    return  render_template('index.html',form=form,name=session.get('name'),know=session.get('know',False))


@main.route('/data2')
def ceshi():
    data = 'Dota2'
    return render_template('ceshi.html',name=data)