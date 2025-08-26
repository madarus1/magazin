const checkbox = document.getElementById("checkbox_delivery")
const deliveru_box = document.getElementById("delivery_box")

function toggle_deliveru_box(){
    deliveru_box.style.display = checkbox.checked ? 'flex' : 'none'
    console.log("Всё хорошо")
}

window.addEventListener("DOMContentLoaded", toggle_deliveru_box)

checkbox.addEventListener("change", toggle_deliveru_box)