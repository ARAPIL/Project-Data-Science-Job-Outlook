import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/data_science.sqlite"

db = SQLAlchemy(app)

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")

# City
# Create our database model
class City(db.Model):
    __tablename__ = 'City'

    id = db.Column(db.Integer, primary_key=True)
    City = db.Column(db.String)
    Count = db.Column(db.Integer)

    def __repr__(self):
        return '<City %r>' % (self.name)


# # Create database tables
# @app.before_first_request
# def setup():
#     # Recreate database each time for demo
#     # db.drop_all()
#     db.create_all()


@app.route("/city")
def city_data():
   #  """Return     and   id"""

    # Query for the   data using pandas
    query_statement = db.session.query(City).\
        order_by(City.Count.desc()).statement
    df = pd.read_sql_query(query_statement, db.session.bind)
    df['Count'] = pd.to_numeric(df['Count'], errors='coerce')
    df = df.sort_values(by=['Count'], ascending=False)
    df = df.head(15)
    print(df)
    # Format the data for Plotly
    trace = {
        "x": df["City"].values.tolist(),
        "y": df["Count"].values.tolist(),
        "type": "bar"
        
    }
    return jsonify(trace)

# Company
# Create our database model
class Company(db.Model):
    __tablename__ = 'Company'

    id = db.Column(db.Integer, primary_key=True)
    Company = db.Column(db.String)
    Count = db.Column(db.Integer)

    def __repr__(self):
        return '<Company %r>' % (self.name)

@app.route("/company")
def company_data():
    """Return     and   id"""

    # Query for the   data using pandas
    query_statement = db.session.query(Company).\
        order_by(Company.Count.desc()).statement
    df = pd.read_sql_query(query_statement, db.session.bind)
    df['Count'] = pd.to_numeric(df['Count'], errors='coerce')
    df = df.sort_values(by=['Count'], ascending=False)
    df = df.head(15)
    print(df)
    # Format the data for Plotly
    trace = {
        "x": df["Company"].values.tolist(),
        "y": df["Count"].values.tolist(),
        "type": "pie"
    }
    return jsonify(trace)

@app.route("/bubble")
def bubble_data():
    """Return     and   id"""

    # Query for the   data using pandas
    query_statement = db.session.query(Company).\
        order_by(Company.Count.desc()).statement
    df = pd.read_sql_query(query_statement, db.session.bind)
    df['Count'] = pd.to_numeric(df['Count'], errors='coerce')
    df = df.sort_values(by=['Count'], ascending=False)
    df = df.head(15)
    print(df)
    # Format the data for Plotly
    # df = df.to_json(orient='records')
    new_dict = {
        "name": df["Company"].values.tolist(),
        "value": df["Count"].values.tolist()

    }

    return jsonify(new_dict)

# Education
# Create our database model
class Education(db.Model):
    __tablename__ = 'Education'

    id = db.Column(db.Integer, primary_key=True)
    Education = db.Column(db.String)
    Count = db.Column(db.Integer)

    def __repr__(self):
        return '<Education %r>' % (self.name)

@app.route("/education")
def education_data():
    """Return     and   id"""

    # Query for the   data using pandas
    query_statement = db.session.query(Education).\
        order_by(Education.Count.desc()).statement
    df = pd.read_sql_query(query_statement, db.session.bind)
    df['Count'] = pd.to_numeric(df['Count'], errors='coerce')
    df = df.sort_values(by=['Count'], ascending=False)
    df = df.head(15)
    print(df)
    # Format the data for Plotly
    trace = {
        "x": df["Education"].values.tolist(),
        "y": df["Count"].values.tolist(),
        "type": "bar"
    }
    return jsonify(trace)

# Experience
# Create our database model
class Experience(db.Model):
    __tablename__ = 'Experience'

    id = db.Column(db.Integer, primary_key=True)
    Experience = db.Column(db.String)
    Count = db.Column(db.Integer)

    def __repr__(self):
        return '<Experience %r>' % (self.name)

@app.route("/experience")
def experience_data():
    """Return experience and the count"""

    # Query for the   data using pandas
    query_statement = db.session.query(Experience).\
        order_by(Experience.Count.desc()).statement
    df = pd.read_sql_query(query_statement, db.session.bind)
    df['Count'] = pd.to_numeric(df['Count'], errors='coerce')
    df = df.sort_values(by=['Count'], ascending=False)
    df = df.head(15)
    print(df)
    # Format the data for Plotly
    trace = {
        "x": df["Experience"].values.tolist(),
        "y": df["Count"].values.tolist(),
        "type": "bar"
    }
    return jsonify(trace)

# Skill
# Create our database model
class Skill(db.Model):
    __tablename__ = 'Skill'

    id = db.Column(db.Integer, primary_key=True)
    Skills = db.Column(db.String)
    Count = db.Column(db.Integer)

    def __repr__(self):
        return '<Skill %r>' % (self.name)

@app.route("/skill")
def skill_data():
    """Return     and   id"""

    # Query for the   data using pandas
    query_statement = db.session.query(Skill).\
        order_by(Skill.Count.desc()).statement
    df = pd.read_sql_query(query_statement, db.session.bind)
    df['Count'] = pd.to_numeric(df['Count'], errors='coerce')
    df = df.sort_values(by=['Count'], ascending=False)
    df = df.head(15)
    print(df)
    
    # Format the data for Plotly
    trace_skill = {
        "x": df["Skills"].values.tolist(),
        "y": df["Count"].values.tolist(),
        "type": "scatter"
    }
    return jsonify(trace_skill)


if __name__ == '__main__':
    app.run(debug=True)
