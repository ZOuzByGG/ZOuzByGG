const notificationButton = document.querySelector('.notification-button');
const notificationMenu = document.querySelector('.notification-menu');

notificationButton.addEventListener('click', () => {
    notificationMenu.style.display = (notificationMenu.style.display === 'block') ? 'none' : 'block';
});