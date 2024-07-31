function print(information){
    alert(information)
}

function read_register_informations(){
    const name = document.getElementById("organization_name").value;
    const email = document.getElementById("organization_email").value;
    const password = document.getElementById("organization_password").value;
    const focus=document.querySelector('input[name="focus"]:checked').value;
    const description = document.getElementById("organization_description").value;

    return [name, email, password, focus, description];
}

function main(){
    let info=read_register_informations();
    print(info);
}
