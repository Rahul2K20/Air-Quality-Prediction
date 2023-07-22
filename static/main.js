document.querySelector("form").addEventListener("submit", function(event){
    event.preventDefault();
    this.style.opacity = 0; 
    setTimeout(() => {
        this.submit();
    }, 500); 
});

function goBack() {
    window.location.href = '/';
}
