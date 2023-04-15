#!/usr/bin/env python
# coding: utf-8

# ## Flask Web Application
# 

# In[1]:


from flask import Flask, render_template, request
app = Flask(__name__)

#flask routing
@app.route("/")
@app.route("/home")
def home():
    return render_template("Home.html")
    #return "This is my homepage..."


# In[2]:


@app.route("/login")
def login():
    return render_template("Login.html")


# In[3]:


@app.route("/logged")
def loggged():
    return render_template("Home2.html")


# In[4]:


@app.route("/logout")
def logout():
    return render_template("Login.html")


# In[5]:


@app.route("/about")
def about():
    return render_template("About.html")


# In[6]:


@app.route("/dashboard")
def dashboard():
    return render_template("Dashboard.html")


# In[7]:


@app.route("/database")
def database():
    return render_template("Database.html")


# In[8]:


@app.route("/submit", methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        user = request.form['name']
        #return f"Log in Successfully, Hello {user}"
        return render_template("Home2.html")
    else:
        user = request.args.get('name')
        return f"Log in Successfully, Hello {user}"

# Set the MongoDB connection parameters
#client = pymongo.MongoClient("mongodb+srv://christianfrago:DEAg7GDzHKQLUdeq@xtian.nbn4vd4.mongodb.net/?retryWrites=true&w=majority")
#db = client["<Diabetes>"]
#collection = db["Diabetes"]


# In[9]:


import pandas as pd
from pymongo import MongoClient
@app.route('/query')
def query():
    # Set up the MongoDB client
    client = MongoClient("mongodb+srv://christianfrago:DEAg7GDzHKQLUdeq@xtian.nbn4vd4.mongodb.net/?retryWrites=true&w=majority")
    db = client.Diabetes

    # Query the collection
    collection = db.Diabetes
    results = collection.find()
    data = list(results)

    # Convert the query results to a pandas DataFrame
    df = pd.DataFrame(data, columns=['preg','plas','pres','skin','test','mass','pedi','age','class'])
    #df = pd.DataFrame(data)
    html_table = df.to_html()

    # Render the HTML table in the template
    return render_template('Database.html', table=html_table)
    #return render_template('new.html')

    


# In[10]:


@app.route('/display')
def display():
    return render_template("Charts.html")


# In[ ]:


if __name__=='__main__':
    app.run()

