var employee = {
    name : "jhon smith"
    job: "programmer";
    age: 31;
    nameLength: function(){
        console.log(this.name.length);
    }
}

var employee = {
    name: "jhon smith",
    job:"programmer",
    age:31,
    report: function(){
        alert("Name is "+ this.name + " job is: " + this.job + "Age is " + this.age)
    }

}

var carInfo = {
    make: "Toyota",
    year: 1990,
    model: "carmy",
    carAlert : function(){
        alert("We've got a car here!")
    }
};


//#random color generator
//
var header = document.querySelector("h2")
header.style.color = '#007BFF'
function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function changeHeaderColor(){
    colorInput = getRandomColor()
    header.style.color  = colorInput;
}
setInterval("changeHeaderColor()", 500);

var p = document.querySelector('p')