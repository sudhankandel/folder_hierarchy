function toggleSubMenu(event, folderId) {
    event.preventDefault();

    const subMenu = document.getElementById(folderId);
    const iconContainer = event.target.closest('li').querySelector('.icon-container');
    const folderIcon = iconContainer.querySelector('.folder-icon');
    const spinnerIcon = iconContainer.querySelector('.spinner-icon');

    if (!subMenu || !folderIcon || !spinnerIcon) {
        console.error('Submenu, folder icon, or spinner icon not found.');
        return;
    }

    // Show spinner and hide folder icon
    folderIcon.style.display = 'none';
    spinnerIcon.style.display = 'inline-block';

    setTimeout(() => {
        if (subMenu.style.display === "block") {
            closeAllSubMenus(subMenu);
            folderIcon.innerHTML = '<i class="fas fa-folder"></i>'; // Closed folder
        } else {
            openSubMenu(subMenu);
            folderIcon.innerHTML = '<i class="fas fa-folder-open"></i>'; // Open folder
        }
        // Restore folder icon after loading
        spinnerIcon.style.display = 'none';
        folderIcon.style.display = 'inline-block';
    }, 200); // Duration of spinner display
}

function closeAllSubMenus(menu) {
    // Close the current submenu
    menu.style.display = 'none';

    // Recursively close all nested submenus
    const subMenus = menu.querySelectorAll('.sub-menu');
    subMenus.forEach(subMenu => {
        closeAllSubMenus(subMenu); // Recursive call


          // Update the folder icon to closed state
    const folderIcon = menu.previousElementSibling.querySelector('.folder-icon');
    console.log(folderIcon)
    if (folderIcon) {
        folderIcon.innerHTML = '<i class="fas fa-folder"></i>';
    }


    });

  
}

function openSubMenu(menu) {
    menu.style.display = 'block';
}
