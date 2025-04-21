document.addEventListener("DOMContentLoaded", function () {
    const toggleSwitch = document.getElementById("darkModeToggle");
    
    // Apply dark mode if previously enabled
    if (localStorage.getItem("darkMode") === "enabled") {
      document.body.classList.add("dark-mode");
      if(toggleSwitch) toggleSwitch.checked = true;
    }
  
    // Listen for toggle switch changes
    if(toggleSwitch) {
      toggleSwitch.addEventListener("change", function () {
        if (toggleSwitch.checked) {
          document.body.classList.add("dark-mode");
          localStorage.setItem("darkMode", "enabled");
        } else {
          document.body.classList.remove("dark-mode");
          localStorage.setItem("darkMode", "disabled");
        }
      });
    }
  });