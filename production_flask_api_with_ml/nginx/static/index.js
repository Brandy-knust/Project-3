var form = d3.select("#form");

// Create event handlers for clicking the button or pressing the enter key
// button.on("click", runEnter);
form.on("submit", runEnter);
var predictedResult = '';
// Create the function to run for both events
function runEnter() {

    // Prevent the page from refreshing
    d3.event.preventDefault();

    var genre = d3.select("#genre").property("value");
    var director = d3.select("#director").property("value");
    var content_rating = d3.select("#content_rating").property("value");
    var production_company = d3.select("#production_company").property("value");
    var runtime = d3.select("#runtime").property("value");
    // var BMI = d3.select("#BMI").property("value");
    // var DiabetesPedigreeFunction = d3.select("#DiabetesPedigreeFunction").property("value");
    // var Age = d3.select("#Age").property("value");
    d3.json(`/predict/${genre}/${director}/${content_rating}/${production_company}/${runtime}`).then(d => {
        console.log(`this is the route /predict/${genre}/${director}/${content_rating}/${production_company}/${runtime}`)
        d3.select("#result").text(`the model predicts your ${d}`);
        predictedResult = d;
    });

}

var director = []

d3.json("/directors").then((data) => {
    console.log(data)

    var checkbox = d3.selectAll('#Director_Checks');
    counter = 0;
    data.forEach(function (director) {
        divel = checkbox.append('div')
        .classed('col-md-3', true);
        divel.append('input')
        .property('value', director)
        .property('name', director)
        .property('id', `cb${counter}`)
        .property('type', 'checkbox')
        .classed('form-check-input', true);
        divel.append('label')
        .text(director)
        .property('for', `cb${counter}`)
        .classed('form-check-label', true);
        counter = counter+1; 
    });

});

function correct() {
    d3.event.preventDefault();
    var ans=[] 
    outcome = ans.indexOf(predictedResult)
    updateData(outcome)
}


// function wrong() {
//     d3.event.preventDefault();
//     var ans=[ "positive","negative"] 
//     outcome = ans.indexOf(predictedResult)
//     updateData(outcome)
// }
// function updateData(outcome) {

//     var Pregnancies = d3.select("#Pregnancies").property("value");
//     var Glucose = d3.select("#Glucose").property("value");
//     var BloodPressure = d3.select("#BloodPressure").property("value");
//     var SkinThickness = d3.select("#SkinThickness").property("value");
//     var Insulin = d3.select("#Insulin").property("value");
//     var BMI = d3.select("#BMI").property("value");
//     var DiabetesPedigreeFunction = d3.select("#DiabetesPedigreeFunction").property("value");
//     var Age = d3.select("#Age").property("value");
//     d3.json(`/add/${Pregnancies}/${Glucose}/${BloodPressure}/${SkinThickness}/${Insulin}/${BMI}/${DiabetesPedigreeFunction}/${Age}/${outcome}`).then(d=>console.log(d));

// }

// d3.select('#yes').on("click",correct)
// d3.select('#no').on("click",wrong)
