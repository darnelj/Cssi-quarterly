var x3= document.getElementById('email').value;
var atposition=x3.indexOf("@");
var dotposition=x3.lastIndexOf(".");if (atposition<1 || dotposition<atposition+2 || dotposition+2>=x3.length){	alert('Please enter a valid email');	return false;}