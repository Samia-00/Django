var ham = 0;
var cheese = 0;

var report = "blank";

if(ham>=10 && cheese >= 10){
    report = "Strong sales of both ham and cheese"
}else if (ham === 0 && cheese === 0){
report = "nothing sold!!"
}
else{
    report = "we had some sales of items"
}

console.log(report);