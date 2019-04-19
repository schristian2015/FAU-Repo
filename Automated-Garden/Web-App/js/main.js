const closeButton = document.getElementById('closeButton');
const tempWidget = document.getElementById('tempID');
const tempWidgetIcon = document.getElementById('tempWidgetID');
closeButton.addEventListener('click', ()=>{
    tempWidget.style.display= 'none'; 
    tempWidgetIcon.style.display = 'block';
});