var counter = 1;
    var limit = 3;
	function addInput(divName){
    	 document.getElementById("roomno").innerHTML = "Room " + counter + " : ";
     	counter = counter + 1;
    }
    
    window.onload = addInput()