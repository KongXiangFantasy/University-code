let ZMW_Img = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUZqldvVYWm7oMkAAzxetrst5aLQmSXKqMVXcKYgI9Hlh9V58YPvoq3NKOksjABuxIUOA&usqp=CAU";
let EUR_Img = "https://upload.wikimedia.org/wikipedia/commons/0/0b/Euro_Series_Banknotes_%282019%29.jpg";
let CNY_Img = "https://i2.wp.com/asiatimes.com/wp-content/uploads/2021/05/Digital-Yuan-Currency-China-.jpg?fit=1600%2C1051&ssl=1";
let USD_Img = "https://www.interchangefinancial.com/wp-content/uploads/2020/08/US-Dollars.jpg";
let TTD_Img = "https://upload.wikimedia.org/wikipedia/en/4/4f/Series_2020_TTD_Polymer_Design.png";
let None = "https://static.thenounproject.com/png/2222628-200.png";




function displayResults(data) {
	let currencyName = $("#currencyName").val();
	let USD = (1/(data.rates[currencyName])).toFixed(2);
	$("#resultUSD").html(USD);
	let CNY = (USD*(data.rates["CNY"])).toFixed(2);
	$("#resultCNY").html(CNY);
	let EUR = (USD*(data.rates["EUR"])).toFixed(2);
	$("#resultEUR").html(EUR);
	let TTD = (USD*(data.rates["TTD"])).toFixed(2);
	$("#resultTTD").html(TTD)
	let ZMW = (USD*(data.rates["ZMW"])).toFixed(2);
	$("#resultZMW").html(ZMW)
	let ratingImageURL = None;
	/*
	let Currency_Name = data.currencyName;
	let CNY = data.rates.CNY;
	let Currency_Name = data.currencyName;
	let Currency_Name = data.currencyName;
	let Currency_Name = data.currencyName;
	$("#resultUSD").html(Currency_Name);
	$("#resultCNY").html(CNY);
	$("#resultEUR").html(EUR);
	$("#resultTTD").html(TTD);
	$("#resultUSZ").html(USZ);
	*/
	let max = 100;
	if (USD < max) {
		USD = max
		ratingImageURL = USD_Img;
		}
	
	if (CNY < max) {
		CNY = max
		ratingImageURL = CNY_Img;
	} 
		
	if (TTD < max) {
		TTD = max
		ratingImageURL = TTD_Img;
	}
		
	if (ZMW < max) {
		ZMW = max
		ratingImageURL = ZMW_Img;
	}
		
	if (EUR < max) {
		ZMW = max
		ratingImageURL = EUR_Img;
	}
	$("#ratingImg").attr("src", ratingImageURL);
}

function submit() {
	$("#output").show();
	const settings = {
	"async": true,
	"crossDomain": true,
	"url": "https://exchangerate-api.p.rapidapi.com/rapid/latest/USD",
	"method": "GET",
	"headers": {
		"x-rapidapi-host": "exchangerate-api.p.rapidapi.com",
		"x-rapidapi-key": "66c19c90ffmsh587ffc799464d48p130d7fjsn84eb50387322"
	}
};

$.ajax(settings).done(function (response) {
	console.log(response);
	displayResults(response);
});
}

function clean() {
	document.getElementById("currencyName").value = '';
}