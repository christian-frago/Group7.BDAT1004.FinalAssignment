#!/usr/bin/env python
# coding: utf-8

# ## Flask Web Application
# 

# In[1]:


from flask import Flask, render_template
app = Flask(__name__)

#flask routing
@app.route("/")
@app.route("/home")
def home():
    return "This is my homepage..."

@app.route("/html")
def html():
    return render_template("new.html")

if __name__=='__main__':
    app.run()


# In[ ]:




