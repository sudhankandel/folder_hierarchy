function toggleSubMenu(event, folderId) {
    event.preventDefault();

    const subMenu = document.getElementById(folderId);
    const iconContainer = event.target.closest('li').querySelector('.icon-container');
    const folderIcon = iconContainer.querySelector('.folder-icon');
    const spinnerIcon = iconContainer.querySelector('.spinner-icon');
    const dash = event.target.closest('li').querySelector('.dash');

    if (!subMenu || !folderIcon || !spinnerIcon || !dash) {
        console.error('Submenu, folder icon, spinner icon, or dash not found.');
        return;
    }

    // Show spinner and hide folder icon
    folderIcon.style.display = 'none';
    spinnerIcon.style.display = 'inline-block';

    setTimeout(() => {
        if (subMenu.classList.contains('open')) {
            closeAllSubMenus(subMenu);
            folderIcon.innerHTML = '<i class="fas fa-folder"></i>'; // Closed folder
            subMenu.classList.remove('open');
            dash.style.width = '10px'; // Reset dash length
        } else {
            openSubMenu(subMenu);
            folderIcon.innerHTML = '<i class="fas fa-folder-open"></i>'; // Open folder
            subMenu.classList.add('open');
            dash.style.width = '20px'; // Expand dash length
        }
        // Restore folder icon after loading
        spinnerIcon.style.display = 'none';
        folderIcon.style.display = 'inline-block';
    }, 500); // Duration of spinner display
}

function closeAllSubMenus(menu) {
    // Close the current submenu
    menu.classList.remove('open');
    
    // Recursively close all nested submenus
    const subMenus = menu.querySelectorAll('.sub-menu.open');
    subMenus.forEach(subMenu => {
        closeAllSubMenus(subMenu); // Recursive call
    });

    // Update the folder icon to closed state
    const folderIcon = menu.previousElementSibling.querySelector('.folder-icon');
    if (folderIcon) {
        folderIcon.innerHTML = '<i class="fas fa-folder"></i>'; // Closed folder
    }
}

function openSubMenu(menu) {
    // Update the folder icon to open state
    const folderIcon = menu.previousElementSibling.querySelector('.folder-icon');
    if (folderIcon) {
        folderIcon.innerHTML = '<i class="fas fa-folder-open"></i>'; // Open folder
    }
}
