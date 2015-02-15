"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""
from flask import request, render_template, flash, url_for, redirect, g,session

from flask_cache import Cache

from application import app, db
from .forms import SearchForm, Autocomplete
from .models import BadModel, User

from flask.ext.login import login_user, current_user, login_required

@app.before_request
def before_requests():
    g.SearchForm =SearchForm()
    g.Autocomplete = Autocomplete()




def index():
#    addUser(55,'44','1')
    return render_template('list_example')

# def home():
#     return redirect(url_for('list_examples'))


def say_hello(username):
    """Contrived example to demonstrate Flask's url routing capabilities"""
    return 'Hello %s' % username



def list_examples():
    """List all examples"""
#    print(g.SearchForm.validate_on_submit(), request.method =='POST','validation on submit check')
    if g.SearchForm.validate_on_submit():       
        return redirect(url_for('search_results', query=g.SearchForm.search.data))
    return render_template('list_examples.html')



from .badSearch import badResult


def search_results(query):
    data = BadModel
    for li in data.query():
        li.put().delete()
    i = 0
    for li in badResult(query):
        #print(li)
        data(
	    id = i,
            text = li
            ).put()
        i=i+1
    result = data.query()
    

    return render_template('search_result.html',query=result)


from flask import jsonify

NAMES=["abc","abcd","abcde","abcdef"]

def autocomplete():
    search = request.args.get('term')
    app.logger.debug(search)

    return jsonify(json_list=NAMES)



from .oauth import facebook


def login():
    return facebook.authorize(callback=url_for('oauth_authorized',
        next=request.args.get('next') or url_for('index'), _external=True))




@facebook.authorized_handler
def oauth_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    session['facebook_token'] = (resp['access_token'], '')
    me = facebook.get('/me')
    social_id = 'facebook$' + me.data['id']
    username = me.data['name']
    email = me.data['email']
    if social_id is None:
        flash("Authentication failed")
        return redirect(url_for('index'))
    addUser(social_id = social_id , nickname = username, email = email)
    user  = findUser(social_id)
    if not user:
        user = User(social_id = social_id , nickname = username, email = email)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('index'))
    # flash('You were signed in as id = %s, name = %s, redirect = %s' % \
    #   (me.data['id'],me.data['name'],request.args.get('nexe')))
    # return redirect(next_url) 


@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('facebook_token')


def findUser(social_id):
    return User.query.filter_by(social_id = social_id).first()


def addUser(social_id,nickname,email):
    user = User(social_id = social_id , nickname = nickname, email = email)
    db.session.add(user)
    db.session.commit()



