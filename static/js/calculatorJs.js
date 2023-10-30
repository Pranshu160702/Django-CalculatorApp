// Preventing Form Resubmission
if ( window.history.replaceState ) {
    window.history.replaceState( null, null, window.location.href );
}

// Setting the value for django variable input
function valueSet() {
    document.getElementById("f_value").value = document.calc.txt.value;
}