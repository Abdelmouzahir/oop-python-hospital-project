from DoctorsManager import *
from PatientManager import *

main_menu = True
while main_menu == True:

    main_menu_selection = int(input("""
Welcome to Alberta Hospital (AH) Management system\n
Select from the following options, or select 0 to stop:
1 -\tDoctors
2 -\tPatients
3 -\tExit Program 
>>> """))
    
    if main_menu_selection == 1:
        doctorMenu()

    
    if main_menu_selection == 2:
       patientMenu()

    
    if main_menu_selection == 3:
        print("Thanks for using the program. Bye!")
        main_menu = False

    
    else:
        continue


