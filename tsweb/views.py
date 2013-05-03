from tsweb import app
from tsweb.database import db_session
from tsweb.models import Descriptor
from tsweb.search import search_for
from flask import Flask, request, session, g, redirect, url_for, \
  abort, render_template, flash

@app.route('/')
def ugly_search_page():
  total = db_session.query(Descriptor).count()
  return render_template('ugly_search.html', total=total)

@app.route('/search', methods=['GET'])
def search_results():
  expr = request.values.get('expr')
  return render_template('search_results.html', expr=expr, descriptors=search_for(expr), try_date=request.values.get('trydate'))

#@app.route('/add', methods=['POST'])
#def add_entry():
#  if not session.get('logged_in'):
#  abort(401)
#  entry = Entry(request.form['title'], request.form['text'])
#  db_session.add(entry)
#  db_session.commit()
#  flash('New entry was succesfully posted')
#  return redirect(url_for('show_entries'))
#
#@app.route('/remove/<entryid>')
#def remove_entry(entryid):
#  if not session.get('logged_in'):
#  abort(401)
#
#  entry = Entry.query.filter_by(id = entryid).first()
#
#  db_session.delete(entry);
#  db_session.commit();
#  flash('Entry with Title:' + entry.title + ' was removed')
#  return redirect(url_for('show_entries'))
#
#@app.route('/login', methods=['GET', 'POST'])
#def login():
#  error = None
#  if request.method == 'POST':
#  if request.form['username'] != app.config['USERNAME']:
#    error = 'Invalid Username'
#  elif request.form['password'] != app.config['PASSWORD']:
#    error = 'Invalid password'
#  else:
#    session['logged_in'] = True
#    flash('You were logged in')
#    return redirect(url_for('show_entries'))
#  return render_template('login.html', error=error)
#
#@app.route('/logout')
#def logout():
#  session.pop('logged_in', None)
#  flash('You were logged out')
#  return redirect(url_for('show_entries'))
