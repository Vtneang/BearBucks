let user = document.getElementById("user");
let stuff = document.getElementById("data");
let myform = document.getElementById("myform");
let new_date = document.getElementById("date");
let new_name = document.getElementById("name");
let new_cate = document.getElementById("category");
let new_amount = document.getElementById("amount");
function generateTablehead(table, data) {
	let head = table.createTHead();
	let row = head.insertRow();
  	for (let key of data) {
	    let th = document.createElement("th");
	    let text = document.createTextNode(key);
	    th.appendChild(text);
	    row.appendChild(th);
	}
}

function generateTable(table, data) {
	count = 0;
	while (data.length < 9) {
		data.push({Name: "...", Amount: "...", Category: "...", Date: "..."});
	}
	for (let element of data) {
		if (count == 9) {
			break;
		}
		let row = table.insertRow();
		for (key in element) {
			let cell = row.insertCell();
			let text = document.createTextNode(element[key]);
			cell.appendChild(text);
		}
		count += 1;
	}
}
function setup() {
	x = user.textContent;
	let idk = stuff.innerHTML.split();
	let trail = []
	if (idk[0] != "[]") {
		for(let i of idk) {
			let i_stuff = i.split(" ");
			let name = i_stuff[1];
			let amount = i_stuff[3];
			let category = i_stuff[5];
			let date = i_stuff[7];
			trail.push({Name: name.slice(1, name.length - 2), Amount: amount.slice(1,amount.length - 2), Category: category.slice(1,category.length - 2), Date: date.slice(1,date.length - 3)});
		}
	}
	let table = document.querySelector("table");
	generateTable(table, trail);
	let data = Object.keys(trail[0]);
	generateTablehead(table, data);
	myform.addEventListener('submit', function(e) {
	e.preventDefault();
	trail.unshift({Name: new_name.value, Amount: new_amount.value, Category: new_cate.value, Date: new_date.value});
	table.innerHTML = "";
	generateTable(table, trail);
	let data = Object.keys(trail[0]);
	generateTablehead(table, data);
})
}

window.onload = setup;
