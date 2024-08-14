
url_organization_database="organization_database.txt"
URL_pet_database="../databases/pet_database"
URL_tutor_database="../databases/tutor_database"

def write_database():
    with open(url_organization_database, "a") as database_file:
        database_file.write("teste")