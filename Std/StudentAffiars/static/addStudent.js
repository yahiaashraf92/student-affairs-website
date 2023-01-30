//check for input validation 
function department(){
    if(document.getElementById("level").value == '4'){
        document.getElementById("department").innerHTML = "<label for=\"department\"> <mark>Department</mark></label> department:<select class=\"form-input\" name=\"Departments\" id=\"departments\" ><option>Choose one </option><option>CS</option><option>AI</option><option>IS</option><option>IT</option><option>DS</option></select><br><br></br>";
        document.getElementById("department").style = "margin-bottom: -45px; margin-top: -15px; padding:10px"
    }
    else{
        document.getElementById("department").innerHTML = ""
        document.getElementById("department").style = "margin-bottom: 0px; margin-top: 0px; padding: 0px"
    }
}
