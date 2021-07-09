# Project-3

# Prediction of Audience Score by Using Machine Learning

## About the Model:
This machine learning model predicts the expected audience rating/score from "www.rottentomatoes.com" that a potential movie will obtain after selecting:
* Up to three different movie directors,
* Movie genre
* Planned production company
* Expected movie rating.
 
The predictive model uses a deep learning algorithm (neural network) with 4 layers and 4500 nodes. The algorithm yields a "Mean Squared Error" of ~25. The model accuracy is around 10 points of rating (above or below) from actual values.

## Potential Applicability:
This model could be used for:
* Investment decisions before funding a movie to further correlate with expected profits.
* Likelihood of a movie to become a "blockbuster" based on the categories selected.
* Create permutations of possible directors and production companies to guarantee higher level of audience rating.
* "Just for fun". 

<b>Team Members:</b>
Brandy Knust
Tyler Nguyen
Adolfo Prieto
Oscar Sanguino

<b>Notes</b>:
* The data set used contains more than 4000 movie titles from the last 80+ years.
* GitHub link contains all the files.
* HTML file is found in the "production_flask_api_with_ml" directory. 
* In oder to download the data and feed the html and *.js file the app.py file must be run first. This file is found in the "production_flask_api_with_ml" directory
* Model which was saved as "model.h5" can be used in other projects related to our project.


<b>Rough Breakdown of Tasks:</b>
* Data identification
* Data extraction 
* Data cleanup (Pandas)
* Data aggregation (Pandas, Flask, Tensorflow, Sklearn)
* Data analysis
* Data visualization (D3, JavaScript, HTML)
* Summary
* Documentation
* Presentation
