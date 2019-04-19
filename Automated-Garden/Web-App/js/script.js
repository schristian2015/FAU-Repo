var countdown = 0;

function refresh() {
    runSVG();	
    getTemperature();
	getWaterLevel();
	getStatusLight();
	getPeltGen();
	getPumpStatus();
}
function checkTime(i) {
	if (i < 10) {
		i = "0" + i;
	}
	return i;
}
//Timer Start
function startTime() {
	var today = new Date();
	var h = today.getHours();
	var m = today.getMinutes();
	var s = today.getSeconds();
	// add a zero in front of numbers <10 \\
	
	m = checkTime(m);
	s = checkTime(s);
	document.getElementById('time').innerHTML = h + ":" + m + ":" + s;
	t = setTimeout(function () {
		startTime();
	}, 500);
}
//initalize
startTime();

//refresh intervale Function


//Await GET SQL data
async function getPlant() {
	return fetch('./php/getPlant.php').then(response => response.json());
}
//Log SQL data in Table
async function getLogs() {
	$('.table-heading').html(`<tr>
        <th>Time</th>
        <th>Temperature</th>
        <th>Light Status</th>
        <th>Water pump</th>
        <th>Water level</th>
        <th>AC Status</th>
    </tr>`);
	let logs = await fetch('./php/getLogs.php').then(response => response.json());
	let table = logs.map(log => {
		let peltgen;
		switch(log.peltgen) {
			case "1": peltgen = "COLD"; break;
			case "2": peltgen = "HOT"; break;
			default: peltgen = "OFF"; break;
		};
		let waterlevel;
		switch(log.waterlevel) {
			case "1": waterlevel = "LOW"; break;
			case "2": waterlevel = "GOOD"; break;
			case "3": waterlevel = "FULL"; break;
			default: waterlevel = "EMPTY"; break;
		}
		let tableInfo = `<tr >
							<td>${log.timestamp}</td>
							<td>${log.temperature}</td>
							<td>${log.lightstatus == "0" ? "OFF": "ON" }</td>
							<td>${log.waterpump == "0" ? "OFF": "ON" }</td>
							<td>${waterlevel}</td>           
							<td>${peltgen}</td>
						</tr>`;
		return tableInfo;
    });
    $(".table-information").append(table);
}
//Temperature Widget
//Temperature gauge display status via dial
async function getTemperature() {
	let plant = await getPlant();
	let check = plant.temperature;
	$('#temp_status').html(check);

}
//Water Level Widget
//On and OFF status water level switches
async function getWaterLevel() {
	// ternary statements 
	let plant = await getPlant();
	
	let check;
	switch (plant.waterlevel) {
	case "1":
		check = '<div class="circle LOW"></div><div class="status">LOW</div>'; break;
	case "2":
		check = '<div class="circle GOOD"></div><div class="status">GOOD</div>'; break;	
	case "3":
		check = '<div class="circle FULL"></div><div class="status">FULL</div>'; break;	
	default:
		check = '<div class="circle EMPTY"></div><div class="status">EMPTY</div>'; break;
	}
	$('#water_status').html(check);
	
}

//Water Pump stats Widget
//On and OFF state Light switches
async function getPumpStatus() {
	let plant = await getPlant();
	let check = plant.water_pump == "0" ? '<div class="circle OFF"></div><div class="status">OFF</div>' :
											'<div class="circle ON"></div><div class="status">ON</div>'  ;
	$('#waterpump_status').html(check);
	
}
//Light Status Widget 
//On and OFF State Light Switches
async function getStatusLight() {
	let plant = await getPlant();
	let check = plant.light_status == "0" ? '<div class="circle OFF"></div><div class="status">OFF</div>' :
										    '<div class="circle ON"></div><div class="status">ON</div>';
	$('#light_status').html(check);

}
// AC UNIT(Peltier Gen){...peltGen} //Controls Airflow
async function getPeltGen() {
	let plant = await getPlant();
	let check;

	switch (plant.peltgen) {
	case "1":
		check = '<div class="circle COLD"></div><div class="status">COLD</div>'; break;
	case "2":
		check = '<div class="circle HOT"></div><div class="status">HOT</div>'; break;	
	default:
		check = '<div class="circle OFF"></div><div class="status">OFF</div>'; break;
	}
	$('#ac_status').html(check);
}
