from flask import render_template, request, redirect
from flask_wtf.csrf import CSRFProtect
from app import app, db
from app.models import Entry
from datetime import datetime

# Initialize CSRF protection
csrf = CSRFProtect(app)

@app.route('/')
@app.route('/index')
def index():
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        first_name = form.get('first_name')
        last_name = form.get('last_name')
        dob_str = form.get('dob')  # Get the date of birth as a string
        amount_due = form.get('amount_due')

        if first_name and last_name and dob_str and amount_due:  # Check if all fields are provided
            # Convert dob_str to a Python date object
            dob = datetime.strptime(dob_str, '%Y-%m-%d').date()

            entry = Entry(
                first_name=first_name,
                last_name=last_name,
                dob=dob,
                amount_due=amount_due
            )
            db.session.add(entry)
            db.session.commit()

        return redirect('/index')

    return "of the jedi"

@app.route('/update/<int:student_id>')
def updateRoute(student_id):
    entry = Entry.query.get(student_id)

    if not entry:
        return "Entry not found", 404

    return render_template('update.html', entry=entry)


@app.route('/update/<int:student_id>', methods=['POST'])
def update(student_id):
    entry = Entry.query.get(student_id)

    if not entry:
        return "Entry not found", 404

    if request.method == 'POST':
        form = request.form
        entry.first_name = form.get('first_name')
        entry.last_name = form.get('last_name')

        # Handle date of birth (dob) conversion
        dob_str = form.get('dob')
        try:
            entry.dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
        except ValueError:
            return "Invalid date format. Date must be in YYYY-MM-DD format.", 400

        entry.amount_due = form.get('amount_due')

        db.session.commit()
        return redirect('/index')

    return render_template('update.html', entry=entry, csrf_token=csrf.generate_csrf())

@app.route('/delete/<int:student_id>', methods=['DELETE', 'GET'])
def delete(student_id):
    entry = Entry.query.get(student_id)

    if not entry:
        return "Entry not found", 404

    db.session.delete(entry)
    db.session.commit()
    return redirect('/index')
