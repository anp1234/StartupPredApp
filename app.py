from flask import Flask,render_template,request,redirect,url_for
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder
import warnings
warnings.filterwarnings("ignore", message="InconsistentVersionWarning")


app = Flask(__name__)


with open('models/model3.pkl','rb') as f:
    model = pickle.load(f)


scaler = StandardScaler()

label_encoder = LabelEncoder()




##Create a home route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name=request.form['name']
        category = request.form['category']
        founded_at = int((request.form['founded_at']))
        closed_at = int((request.form['closed_at']))
        country = request.form['country']
        lat=(request.form['lat'])
        long=(request.form['long'])
        funding_rounds = (request.form['funding_rounds'])
        total_funding=(request.form['total_funding'])
        first_funding=(request.form['first_funding'])
        last_funding=(request.form['last_funding'])
        milestones=(request.form['milestones'])
        first_milestone=(request.form['first_milestone'])
        last_milestone=(request.form['last_milestone'])
        
        active_days=(closed_at-founded_at)*365
        
        
        
        print("Name:",name)
        print("Category:",category) 
        print("Founded at:",founded_at) 
        print("Closed at:",closed_at)  
        print("Country:", country) 
        print("Lat:",lat)
        print("Long:",long)   
        print("Funding Rounds:",funding_rounds) 
        print("Total Funding:",total_funding)  
        print("First Funding:",first_funding)
        print("Lastfunding:",last_funding)
        print("Milestones:",milestones)
        print("First Milestone:",first_milestone)
        print("Last Milestone:",last_milestone)
        print("Active Days:",active_days)
        
            
        
        input_data={
            'category_code':category,
            'founded_at':founded_at,
            'country_code':country,
            'first_funding_at':first_funding,
            'last_funding_at':last_funding,
            'funding_rounds':funding_rounds,
            'funding_total_usd':total_funding,
            'first_milestone_at':first_milestone,
            'last_milestone_at':last_milestone,
            'milestones':milestones,
            'lat':lat,
            'lng':long,
            'active_days':active_days
        }
        
        # Convert the random input to a DataFrame
        random_input_df = pd.DataFrame([input_data])
        
        # Preprocess the input data
        random_input_transformed = model.best_estimator_.named_steps['preprocessor'].transform(random_input_df)

        
        # Predict the output using the trained model
        predicted_output = model.best_estimator_.named_steps['model'].predict(random_input_transformed)[0]
        
        # Print the predicted output
        print(f"Predicted output for the random input: {predicted_output}")
        print(type(predicted_output))
        
        class_mapping = {0: 'Acquired', 1: 'IPO', 2: 'Closed', 3: 'Operating'}
        predicted_label = class_mapping[predicted_output]
        print("Predicted labels:", predicted_label)
        

        return render_template('predict.html',predicted_label=predicted_label)
        
        

if __name__ == '__main__':
    app.run(debug=True)
