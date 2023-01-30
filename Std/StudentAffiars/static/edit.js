
var inputElement = document.getElementById("Delete Student")
inputElement.addEventListener("click", function() {
    if (confirm("Do you want to delete this student?")) {
        document.getElementById("form").submit()
    } else {
        return false;
    }
})