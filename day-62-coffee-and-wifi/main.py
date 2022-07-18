from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location_url = StringField('Cafe Location on Google Maps(URL)', validators=[DataRequired(), URL()])
    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee_Rating', validators=[DataRequired()],
                                choices=[('✘', '✘'), ('☕', '☕'), ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕'),('☕☕☕☕', '☕☕☕☕'), ('☕☕☕☕☕', '☕☕☕☕☕')])
    wifi_rating = SelectField('Wifi Strength Rating', validators=[DataRequired()],
                              choices=[('✘', '✘'),('💪', '💪'),('💪💪', '💪💪'),('💪💪💪', '💪💪💪'),('💪💪💪💪', '💪💪💪💪'),('💪💪💪💪💪', '💪💪💪💪💪')])
    power_outlet_rating = SelectField('Power Socket Availability', validators=[DataRequired()],
                                      choices=[('✘', '✘'),('🔌', '🔌'),('🔌🔌', '🔌🔌'),('🔌🔌🔌', '🔌🔌🔌'),('🔌🔌🔌🔌', '🔌🔌🔌🔌'),('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = form.cafe.data
        cafe_url = form.location_url.data
        open_time = form.open_time.data
        close_time = form.closing_time.data
        coffee_rating = form.coffee_rating.data
        wifi_rating = form.wifi_rating.data
        power_rating = form.power_outlet_rating.data
        element_list = [cafe_name.title(), cafe_url, open_time, close_time, coffee_rating, wifi_rating, power_rating]
        with open("cafe-data.csv", "a+", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(element_list)
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
