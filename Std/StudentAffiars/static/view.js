//filteration for the student based on the level and the department
function filter() {
    var lev = document.getElementById("levelfilter").value;
    var dep = document.getElementById("departmentlevel").value;
    var table = document.getElementById("viewStudent");
    var tr = table.getElementsByTagName("tr");
    for (let i = 1; i < tr.length; i++) {
        var td = tr[i].getElementsByTagName("td");
        if (td[2].innerHTML == lev && td[3].innerHTML == dep) {
            tr[i].style.display = "";
        }
        else if (lev == "All" && td[3].innerHTML == dep) {
            tr[i].style.display = "";
        }
        else if (dep == "All" && td[2].innerHTML == lev) {
            tr[i].style.display = "";
        }
        else if (dep == "All" && lev == "All") {
            tr[i].style.display = "";
        }
        else {
            tr[i].style.display = "none";
        }
    }

}


function newsearch(){
    window.location.replace("search.html");
}

function savechanges(){
    alert("changes saved");
}

//add students info to the table
function viewStudent() {
    var table = document.getElementById("viewStudent");
    // while there is data insert in the table
    var row = table.insertRow();
    row.innerHTML = "<td>mohamed mohamed</td><td>20201855</td><td>4</td><td>CS</td><td><input type=\"radio\" name=\"Activity6\" value=\"Active\" checked>Active <input type=\"radio\" name=\"Activity5\" value=\"Inactive\">Inactive </td>"
    row.style.textAlign = "center";
}

function changeActive(id){
    let it = document.getElementById(id).value;
    if (id[0] == 'A')
        id = id.substring(1);
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function () {
        var data =this.responseText;
        if (data=="done"){
            alert("status changed")
        }
    };
    xhttp.open("POST", "changeActive");
    const csrftoken = getCookie('csrftoken');
    xhttp.setRequestHeader("X-CSRFToken", csrftoken);
    xhttp.send(
      JSON.stringify({
        stat : it,
        Ident : id,
      })
    );

}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

