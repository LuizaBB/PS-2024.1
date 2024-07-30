function print(information){
    alert(information)
}

function read_register_informations(){
    let organization_name = document.getElementById("organization_name").value;
    let organization_email = document.getElementById("organization_email").value;
    let organization_password = document.getElementById("organization_password").value;
    let organization_focus=document.getElementById("organization_focus").value;
    let organization_description = document.getElementById("organization_description").value;

    let register_information=[organization_name, organization_email, organization_password, organization_focus, organization_description];
    return register_information;
}
function main(){
    let info=read_register_informations();
    print(info);
}
