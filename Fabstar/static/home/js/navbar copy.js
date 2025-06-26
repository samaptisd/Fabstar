document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.querySelector('.toggle-button');
    const navLinks = document.querySelector('.nav-links');
    const services = document.querySelector('.services > a'); // Target the link directly

    toggleButton.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });

    // Prevent default to stop link action and toggle submenu display
    services.addEventListener('click', function(e) {
        // Check if in mobile view
        if (window.innerWidth <= 768) {
            e.preventDefault(); // Stop the link from activating
            this.parentElement.classList.toggle('active');
        }
    });
});