


function Drop(){

console.log("salma")
const dropdown = document.querySelector("#dropdown-btn");
var i;
console.log(dropdown)


// for (i = 0; i < dropdown.length; i++) {
dropdown.addEventListener("click", () =>{
// this.classList.toggle("active");
console.log("hello")
var dropdownContent = dropdown.nextElementSibling;
// console.log(dropdownContent)
if (dropdownContent.style.display === "block") {
  dropdownContent.style.display = "none";
} else {
  dropdownContent.style.display = "block";
}
});
  // }
  }