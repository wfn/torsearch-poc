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

