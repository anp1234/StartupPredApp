

document.getElementById("myForm").addEventListener("submit", function (event) {
  // Get the value of each input field
  var input1 = document.getElementById("name").value;
  var input2 = document.getElementById("category").value;
  var input3 = document.getElementById("founded_at").value;
  var input4 = document.getElementById("closed_at").value;
  var input5 = document.getElementById("country").value;
  var input6 = document.getElementById("lat").value;
  var input7 = document.getElementById("long").value;
  var input8 = document.getElementById("funding_rounds").value;
  var input9 = document.getElementById("total_funding").value;
  var input10 = document.getElementById("first_funding").value;
  var input11= document.getElementById("last_funding").value;
  var input12 = document.getElementById("milestones").value;
  var input13 = document.getElementById("first_milestone").value;
  var input14= document.getElementById("last_milestone").value;
  
  // Check if any of the input fields are empty
  if (input1 === "" || input2 === "" || input3 === "" || input4 === ""|| input5 === "" || input6 ===""|| input7 === "" ||input8 === "" || input9===""|| input10===""|| input11===""|| input12===""|| input13===""|| input14===""){
    // Prevent the form from being submitted
    event.preventDefault();

    // Display an alert message
    alert("Please fill in all fields");
  }
});
