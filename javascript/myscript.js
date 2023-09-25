var firstName = prompt("First Name please: ")
var lastName = prompt("Last Name please: ")
var age = prompt("How old you are?: ")
var height = prompt("What is your height?: ")
var petName = prompt("whats your pet name? ")
alert("Thank you so much for the information!")

var nameCond = null;
var ageCond = null;
var heightCond = null;
var petCond = null;


// name condition
if (firstName[0] === lastName[0]){
    nameCond = true;
} else {
    nameCond = false;
}

//age condition
if (age>20 && age<30){
    ageCond = true;
}else{
    ageCond = false;
}

// height condition
if (height >= 170) {
    heightCond = true;
}else{
    heightCond = false;
}

//pet name

if (petName[petName.length - 1] === "y"){
    petCond = true;
}else{
    petCond = false;
}

//check all condition
if (nameCond && ageCond && heightCond && petCond){
    console.log("Welcome SPY!!!!");
} else {
    console.log("nothing to see here!!!!");
}