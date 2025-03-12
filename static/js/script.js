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
          // Remove active class from all items
          menuItems.forEach(i => i.classList.remove("active"));
          
          // Add active class to the clicked item
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




function showRoleForm() {
  document.getElementById("roleForm").style.display = "flex";
}
function showRoleEditForm(name, desc, id) {
  document.getElementById("roleEditForm").style.display = "flex";
  document.getElementById("editRoleName").value = name;
  document.getElementById("editRoleDesc").value = desc;
  document.getElementById("editRoleForm").action = "/editrole/" + id;
}

function hideRoleForm() {
  document.getElementById("roleForm").style.display = "none";
  document.getElementById("roleEditForm").style.display = "none";
}





//Employee
function showEmpForm() {
  document.getElementById("empForm").style.display = "flex";
}
function hideempForm() {
  document.getElementById("empForm").style.display = "none";
  document.getElementById("empEditForm").style.display = "none";
}

function showEmpEditForm(id,fname,lname,email,mob,dept,role) {
  document.getElementById("empEditForm").style.display = "flex";
  document.getElementById("editFname").value = fname;
  document.getElementById("editLname").value = lname;
  document.getElementById("editEmail").value = email;
  document.getElementById("editmob").value = mob;
  document.getElementById("editDept").value = dept;
  document.getElementById("editRole").value = role;
  document.getElementById("editEmpForm").action = "/editemp/" + id;
}


