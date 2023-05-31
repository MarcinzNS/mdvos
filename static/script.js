document.addEventListener('DOMContentLoaded', function() {
    
    var themeToggle = document.getElementById('theme-toggle');
    var body = document.body;

    body.classList.add('light');
  
    themeToggle.addEventListener('click', function() {
        console.log('Kliknięto przycisk');
        body.classList.toggle('dark');
        body.classList.toggle('light');
    });
  });
  