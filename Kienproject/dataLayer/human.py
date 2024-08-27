from models import info

def people_list():

    people = [
        info.info(1, "PHI VINH KIEN", "/"),
        info.info(2, "HOANG HAI ANH", "history"),
        info.info(3, "NGUYEN DUC MINH", "people"),
        info.info(4, "NGUYEN LAM TUE", "#areas"),
        info.info(5, "TRINH LE HA ANH", "about"),    
        info.info(5, "NGUYEN THI MINH PHUONG", "about"),    
    ]
    return people
    