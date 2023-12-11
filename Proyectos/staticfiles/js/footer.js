const expandButton = document.getElementById('expand-button');
const footerContent = document.getElementById('footer-content');

expandButton.addEventListener('click', () => {
    if (footerContent.style.display === 'none') {
        footerContent.style.display = 'block';
        expandButton.innerHTML = '<span>▲</span>';
    } else {
        footerContent.style.display = 'none';
        expandButton.innerHTML = '<span>▼</span>';
    }
});
