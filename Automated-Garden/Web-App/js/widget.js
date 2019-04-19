/*
<div id="widget" class="container">
  <div class="widgetButton"></div>    
   <div class="widgetButton"></div>    
</div>
*/
var plus = document.createElement('div');
plus.className =  "plus";

const widget = document.getElementById('widget')
const widgets = document.querySelectorAll('.widgetButton');

for(let i =0; i < widgets.length; i++){
  widgets[i].addEventListener('mouseover', ()=>{
    widgets[i].style.backgroundColor ="orange";
    widgets[i].appendChild(plus);
  });
widgets[i].addEventListener('mouseleave', ()=>{
    widgets[i].style.backgroundColor ="";
    widgets[i].removeChild(plus);
  });
  
}
