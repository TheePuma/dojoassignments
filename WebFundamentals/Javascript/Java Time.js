function time(){
var hour = 5;
var min = 30;
var period = "PM";
if (period =="AM"){
  if (min <30) {
    console.log("It's just after " + hour + " in the morning");
  }
  else {
    console.log("It's almost " + (hour + 1) + " in the morning");
  }
} 
else{
  if (min<30) {
    console.log("It's just after " +hour + " in the evening");
  }
  else {
    console.log("Its almost " + (hour + 1) + " in the evening.");
  } 
}
}

time();