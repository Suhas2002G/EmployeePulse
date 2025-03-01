// Add functionality to set active class on navbar links
document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    navLinks.forEach(link => {
      link.addEventListener('click', function(e) {
        // Prevent default behavior if using as single page application
        e.preventDefault();

        // Remove active class from all links
        navLinks.forEach(nav => nav.classList.remove('active'));

        // Set active class to clicked link
        this.classList.add('active');

        // Example: Logging the selected page; can be replaced with dynamic content loading
        const page = this.getAttribute('data-page');
        console.log(`Navigating to ${page} page`);
      });
    });
  });






//Sidebar
  document.addEventListener("DOMContentLoaded", function () {
    const menuItems = document.querySelectorAll(".side-item");
    
    menuItems.forEach(item => {
        item.addEventListener("click", function () {
            document.querySelector(".side-item.active")?.classList.remove("active");
            this.classList.add("active");
        });
    });
});





function showForm() {
  document.getElementById("deptForm").style.display = "flex";
}

function showEditForm(name, desc, id) {
  document.getElementById("deptEditForm").style.display = "flex";
  document.getElementById("editDeptName").value = name;
  document.getElementById("editDeptDesc").value = desc;
  document.getElementById("editDeptForm").action = "/edit/" + id;
}

function hideForm() {
  document.getElementById("deptForm").style.display = "none";
  document.getElementById("deptEditForm").style.display = "none";
}

