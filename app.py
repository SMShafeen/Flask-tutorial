from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Mumbai, India',
    'salary': 'RS. 10,00,000',
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Hyderabad, India',
    'salary': 'RS. 15,00,000',
  },
  {
    'id': 3,
    'title': 'Forntend Engineer',
    'location': 'Remote',
    'salary': 'RS. 12,00,000',
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Bengaluru, India',
    'salary': 'RS. 13,00,000',
  },
  {
    'id': 5,
    'title': 'Software Engineer',
    'location': 'San Francisco, USA',
    'salary': '$15,000',
  },
]

@app.route("/")
def hello():
  return render_template("home.html", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
