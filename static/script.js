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











