
function searchFilter() {
    var lev = document.getElementById("lev").value;
    var table = document.getElementById("searchtable");
    var tr = table.getElementsByTagName("tr");
    for (let i = 1; i < tr.length; i++) {
        var td = tr[i].getElementsByTagName("td");
        if(lev == "All"){
            tr[i].style.display = "";
        }
        else if (td[2].innerHTML == lev) {
            tr[i].style.display = "";
        }
        else {
            tr[i].style.display = "none";
        }
    }
}

// the Assign department buttton only appear to the the student in level 3
var table = document.getElementById("searchtable");
for (let i in table.rows) {
    let row = table.rows[i];
    if (row.cells[2].innerText == 3) {
        var button = document.createElement("button");
        button.type = "button";
        button.innerHTML = "Assign department";
        row.cells[3].innerHTML = "<button onclick=\"window.location.href='assign.html';\">Assign department</button>";
    }
}