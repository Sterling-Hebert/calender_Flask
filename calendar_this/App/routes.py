from flask import Blueprint, render_template, redirect
# import datetime
from datetime import datetime
import os
import sqlite3
from .forms import AppointmentForm


bp = Blueprint("main", __name__, url_prefix="/")
DB_FILE = os.environ.get("DB_FILE")

@bp.route("/", methods=["GET", "POST"])
def main():
    form = AppointmentForm()
    if form.validate_on_submit():
        print("We got a hit!!!!")
        params = {
        'name': form.name.data,
        'start_datetime': datetime.combine(form.start_date.data, form.start_time.data),
        'end_datetime': datetime.combine(form.end_date.data, form.end_time.data),
        'description': form.description.data,
        'private': form.private.data
        }
        print(params['description'], "Hit!")
        print(params)
        with sqlite3.connect(DB_FILE) as conn:
            curs=conn.cursor()
            curs.execute(
                f"""
                INSERT INTO appointments (name, start_datetime, end_datetime, description, private)
                VALUES
                ('{params['name']}', '{params['start_datetime']}', '{params['end_datetime']}', '{params['description']}', '{params['private']}');
                """
            )
        return redirect("/")




    with sqlite3.connect(DB_FILE) as conn:
        curs=conn.cursor()
        curs.execute(
        """
        SELECT id, name, start_datetime, end_datetime
        FROM appointments
        ORDER BY start_datetime;
        """
        )
        data = curs.fetchall()
        rows = [list(row) for row in data]

        for row in rows:
            date_str = row[2]
            print(date_str, "Date string", row)
            datetime_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            print("Start flag ,++++++++++++++")
            time_str = datetime_obj.strftime('%H:%M')
            row[2] = time_str
        for row in rows:
            date_str = row[3]
            print("Start flag ,------------dfadsf")
            datetime_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            time_str = datetime_obj.strftime('%H:%M')
            row[3] = time_str

        print(rows, "<=================")

    return render_template("main.html", rows=rows, form = form)
