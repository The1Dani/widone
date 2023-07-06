let checkbox = (id, break_id) => 
{
    let checkbox = document.getElementById(id);
    let break_div = document.getElementById(break_id)
    if (checkbox.checked) {
        break_div.style.display = "table-row";
    }
    else {
        document.getElementById("log-duration").value = ' ';
        break_div.style.display = "none";
    }
}
