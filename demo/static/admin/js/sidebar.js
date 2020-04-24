let main = document.getElementById('main');
let toggleSidebar = document.getElementById('toggleSidebar');
toggleSidebar.addEventListener('click', function() {
    let sidebarOpened = localStorage.getItem('sidebar');
    localStorage.setItem('sidebar', !(sidebarOpened === 'true'));
    main.classList.toggle('shifted');
});
if (localStorage.getItem('sidebar') == 'true') {
    main.classList.add('shifted');
}
