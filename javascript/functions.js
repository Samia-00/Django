function addNum(num1,num2){
    console.log(num1+num2);
}


function helloSomeone(name= "frankie"){
    console.log("Hello "+name);
}

function formal(name = "Sami",title = "Sir"){
    console.log(title+ " "+name);
}

function timesFive(numInput){
    var result = numInput * 5
    return result
}

var v = "GLOBAL V"
var stuff = "GLOBAL STUFF"

function fun(stuff){
    console.log(v);
    stuff = "Reassign stuff inside function"
    console.log(stuff);
}

fun();
console.log(stuff)

function monkeyTrouble(aSmile, bSmile){
    return (aSmile && bSmile) || (!aSmile && !bSmile)
}

function stringTimes(str,n){
    var returnStr = "";
    var i = 0;
    while(i<n){
    returnStr += str
    i++
    }
    return returnStr
}

function luckySum(a,b,c){
    if(a == 13){
    return 0
    }
    if (b == 13){
    return a
    }
    if (c == 13){
    return a+b
    }
    return a+b+c
}

function caught_speeding(speed, is_birthday){
    if(is_birthday){
        speed = speed - 5;
    }
    if ( speed <= 60 ){
        return 0;
    }
    if(60 < speed <= 80){
        return 5;
    }
    return 44;
}

function makeBricks(small, big, goal){
    return goal%5 >= 0 && goal%5 -small <=0 && small + 5*big >= goal;
}