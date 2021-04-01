function loader_func () {
    document.getElementById('submit-button').innerHTML = '<div class="loader"></div>';
    // document.getElementById('submit-form').style.visibility = "hidden";
    // document.innerHTML = '<div class="loader"></div>';

}

document.getElementById('submit-button').addEventListener('click', loader_func);