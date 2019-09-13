
var num = prompt('구구단 몇 단을 보실랍니까요? Type a number between 1 to 9: ');

// Make sure right input has been entered
if (num == '' || isNaN(num)) {

	alert('Please enter proper input. An integer btw 1 to 9.');
} else if(num < 1 || num > 10) {
	alert('Please note that only an integer btw 1 to 9 is valid.');
} else {

	for (var i = 1; i < 10; i++) {
		document.write(num + ' * ' + i + ' = ' + num*i+'<br>');
	}
}
