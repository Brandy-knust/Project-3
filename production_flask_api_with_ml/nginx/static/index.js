var form = d3.select("#form");

// Create event handlers for clicking the button or pressing the enter key
// button.on("click", runEnter);
form.on("submit", runEnter);
var predictedResult = '';
// Create the function to run for both events
function runEnter() {

    // Prevent the page from refreshing
    d3.event.preventDefault();

    var Pregnancies = d3.select("#Pregnancies").property("value");
    var Glucose = d3.select("#Glucose").property("value");
    var BloodPressure = d3.select("#BloodPressure").property("value");
    var SkinThickness = d3.select("#SkinThickness").property("value");
    var Insulin = d3.select("#Insulin").property("value");
    var BMI = d3.select("#BMI").property("value");
    var DiabetesPedigreeFunction = d3.select("#DiabetesPedigreeFunction").property("value");
    var Age = d3.select("#Age").property("value");
    d3.json(`/predict/${Pregnancies}/${Glucose}/${BloodPressure}/${SkinThickness}/${Insulin}/${BMI}/${DiabetesPedigreeFunction}/${Age}`).then(d => {
        d3.select("#result").text(`the model predicts your ${d}`);
        predictedResult = d;
    });




}

function correct() {
    d3.event.preventDefault();
    var ans=["negative", "positive"] 
    outcome = ans.indexOf(predictedResult)
    updateData(outcome)
}


function wrong() {
    d3.event.preventDefault();
    var ans=[ "positive","negative"] 
    outcome = ans.indexOf(predictedResult)
    updateData(outcome)
}
function updateData(outcome) {

    var Pregnancies = d3.select("#Pregnancies").property("value");
    var Glucose = d3.select("#Glucose").property("value");
    var BloodPressure = d3.select("#BloodPressure").property("value");
    var SkinThickness = d3.select("#SkinThickness").property("value");
    var Insulin = d3.select("#Insulin").property("value");
    var BMI = d3.select("#BMI").property("value");
    var DiabetesPedigreeFunction = d3.select("#DiabetesPedigreeFunction").property("value");
    var Age = d3.select("#Age").property("value");
    d3.json(`/add/${Pregnancies}/${Glucose}/${BloodPressure}/${SkinThickness}/${Insulin}/${BMI}/${DiabetesPedigreeFunction}/${Age}/${outcome}`).then(d=>console.log(d));

}

d3.select('#yes').on("click",correct)
d3.select('#no').on("click",wrong)
