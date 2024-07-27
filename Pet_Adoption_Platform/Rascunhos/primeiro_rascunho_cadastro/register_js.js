function show_pet_input(){
    let pet_input_div=document.querySelector(".pet_information");
    if(pet_input_div.style.display=="block"){
        pet_input_div.style.display="none";}
    else{
        pet_input_div.style.display="block";}
}

function print_register_information(information){
    alert(`Informações coletadas:\nBoas-vindas, ${information[0]}
        \nemail ${information[1]}
        \npassword ${information[2]}
        \npet name ${information[3]}
        \npet ${information[4]}
        \npet breed ${information[5]}
        \npet age ${information[6]}`);
}

function read_register_informations(){
    let user_name = document.getElementById("user_name").value;
    let user_email = document.getElementById("user_email").value;
    let user_passsword = document.getElementById("user_password").value;
    let pet_owner_check=document.querySelector(".pet_owner_check");
    let pet_name = document.getElementById("pet_name").value;
    let pet_species = document.getElementById("pet_species").value;
    let pet_breed = document.getElementById("pet_breed").value;
    let pet_age = document.getElementById("pet_age").value;

    let register_information=[user_name, user_email, user_passsword, pet_name, pet_species, pet_breed, pet_age];
    print_register_information(register_information)

}