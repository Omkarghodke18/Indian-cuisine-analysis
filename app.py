from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the CSV file into a DataFrame
df = pd.read_csv('D:\\Indian_cuisine_Analysis\\Flask API\\Price_data.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    dish_info = None
    if request.method == 'POST':
        dish_name = request.form['dish_name']
        # Search for the dish in the DataFrame
        dish_info = df[df['name'].str.lower() == dish_name.lower()]
        if not dish_info.empty:
            dish_info = dish_info.to_dict(orient='records')[0]  # Convert to dictionary for easy access
        else:
            dish_info = "Dish not found."

    return render_template('index.html', dish_info=dish_info)

if __name__ == '_main_':
    app.run(debug=True)