from selenium.webdriver.common.by import By

BASE_URL            =       "https://useinsider.com/"

COOKIES             =       (By.ID, "wt-cli-accept-all-btn")
COMPANY             =       (By.CSS_SELECTOR, "ul li:nth-child(6)")
OPEN_COMPANY        =       (By.CSS_SELECTOR, ".dropdown.nav-item.show > a#navbarDropdownMenuLink")
CAREERS             =       (By.CSS_SELECTOR, ".new-menu-dropdown-layout-6-mid-container a:nth-of-type(2)")