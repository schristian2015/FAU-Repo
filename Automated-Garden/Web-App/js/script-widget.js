

//WATER
var waterPumpStatus = document.getElementById("waterpump_status");
var container_waterdrop = document.getElementById("container-waterdrop");
//LIGHT
var lightStatus = document.getElementById("light_status");
var target_light_lamp = document.getElementById("light-lamp");
//AC
var acStatus = document.getElementById("ac_status");
var container_ac_COLD =document.getElementById('container-ac-cold');
var container_ac_HOT =document.getElementById('container-ac-hot');


function waterSVG(){
  if(waterPumpStatus.innerText == "OFF"){
    container_waterdrop.style.display = "none";
  }
  else{
    container_waterdrop.style.display = "block";
  }
}
/*
function lightSVG(){
  if(lightStatus.innerText == "OFF"){
    
  }
  else {
    tarte
  }
}*/
function lightSVG(){
  if(lightStatus.innerText == "ON"){
    target_light_lamp.style.display = "block";
  }
  else{
    target_light_lamp.style.display = "none";
  }
}
function acSVG(){
  if(acStatus.innerText == "HOT"){
    container_ac_COLD.style.display = 'none';
    container_ac_HOT.style.display = 'block';
  }
  else if(acStatus.innerText == "COLD"){
    container_ac_COLD.style.display = 'block';
    container_ac_HOT.style.display = 'none';
  }
  else if(acStatus.innerText == "OFF"){
    container_ac_COLD.style.display = 'none';
    container_ac_HOT.style.display = 'none';
  }
}
function runSVG(){
  lightSVG();
  waterSVG();
  acSVG();
}