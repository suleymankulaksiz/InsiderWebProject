from selenium.webdriver.common.by import By

SEE_ALL_QA_JOBS_BUTTON                      =      (By.LINK_TEXT, "See all QA jobs")
FILTER_LOCATION                             =      (By.ID, "select2-filter-by-location-container")
FILTER_DEPARTMENT                           =      (By.ID, "select2-filter-by-department-container")
LOCATION_TEXT                               =      (By.CSS_SELECTOR,"#select2-filter-by-department-container")
JOB_TITLE                                   =      (By.CSS_SELECTOR, "[class='position-title font-weight-bold']")
JOB_LOCATION_ADRESS                         =      (By.CSS_SELECTOR,".position-location.text-large")
LOCATION_TEXT_AREA                          =      (By.XPATH, '//li[text()="Istanbul, Turkey"]')
DEPARTMENT_NAME                             =      (By.CSS_SELECTOR,"[class='position-department text-large font-weight-600 text-primary']")
LOCATION_INFO                               =      (By.CSS_SELECTOR,"[class='position-location text-large']")
VIEW_ROLE_BUTTON                            =      (By.CSS_SELECTOR,'a.btn.btn-navy.rounded.pt-2.pr-5.pb-2.pl-5')
JOB_AREA                                    =      (By.CSS_SELECTOR,"[class='position-list-item-wrapper bg-light']")