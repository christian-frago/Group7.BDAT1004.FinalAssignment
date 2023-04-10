{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8806425f",
   "metadata": {},
   "source": [
    "## Flask Web Application\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e4e95e11",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "from pymongo import MongoClient\n",
    "import pandas as pd\n",
    "import json\n",
    "\n",
    "from flask import Flask, render_template, request\n",
    "app = Flask(__name__)\n",
    "\n",
    "#flask routing\n",
    "@app.route(\"/\")\n",
    "@app.route(\"/home\")\n",
    "def home():\n",
    "    return render_template(\"Home.html\")\n",
    "    #return \"This is my homepage...\"\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a88c876b",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/login\")\n",
    "def login():\n",
    "    return render_template(\"Login.html\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "37999ac1",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/logout\")\n",
    "def logout():\n",
    "    return render_template(\"Login.html\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "be54c326",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/about\")\n",
    "def about():\n",
    "    return render_template(\"About.html\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fe3e16a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/dashboard\")\n",
    "def dashboard():\n",
    "    return render_template(\"Dashboard.html\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d28052f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/database\")\n",
    "def database():\n",
    "    return render_template(\"Database.html\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "be07e324",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/submit\", methods=['POST','GET'])\n",
    "def submit():\n",
    "    if request.method == 'POST':\n",
    "        user = request.form['name']\n",
    "        #return f\"Log in Successfully, Hello {user}\"\n",
    "        return render_template(\"Home.html\")\n",
    "    else:\n",
    "        user = request.args.get('name')\n",
    "        return f\"Log in Successfully, Hello {user}\"\n",
    "\n",
    "# Set the MongoDB connection parameters\n",
    "#client = pymongo.MongoClient(\"mongodb+srv://christianfrago:DEAg7GDzHKQLUdeq@xtian.nbn4vd4.mongodb.net/?retryWrites=true&w=majority\")\n",
    "#db = client[\"<Diabetes>\"]\n",
    "#collection = db[\"Diabetes\"]\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f4b92795",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/query')\n",
    "def query():\n",
    "    # Set up the MongoDB client\n",
    "    client = MongoClient(\"mongodb+srv://christianfrago:DEAg7GDzHKQLUdeq@xtian.nbn4vd4.mongodb.net/?retryWrites=true&w=majority\")\n",
    "    db = client.Diabetes\n",
    "\n",
    "    # Query the collection\n",
    "    collection = db.Diabetes\n",
    "    results = collection.find()\n",
    "    data = list(results)\n",
    "\n",
    "    # Convert the query results to a pandas DataFrame\n",
    "    df = pd.DataFrame(data, columns=['preg','plas','pres','skin','test','mass','pedi','age','class'])\n",
    "    #df = pd.DataFrame(data)\n",
    "    html_table = df.to_html()\n",
    "\n",
    "    # Render the HTML table in the template\n",
    "    return render_template('Database.html', table=html_table)\n",
    "    #return render_template('new.html')\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48fefbe5",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "if __name__=='__main__':\n",
    "    app.run()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
