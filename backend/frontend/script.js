async function signup(){

    const name =
    document.getElementById("name").value;

    const email =
    document.getElementById("signup-email").value;

    const password =
    document.getElementById("signup-password").value;

    const response = await fetch(
        "http://127.0.0.1:5000/api/auth/signup",
        {
            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                name,
                email,
                password,
                role:"admin"
            })
        }
    );

    const data = await response.json();

    document.getElementById("signup-message")
    .innerText = data.msg;

    document.getElementById("name").value = "";
    document.getElementById("signup-email").value = "";
    document.getElementById("signup-password").value = "";

    setTimeout(() => {

        window.location.href = "index.html";

    }, 1500);
}



async function login(){

    const email =
    document.getElementById("email").value;

    const password =
    document.getElementById("password").value;

    const response = await fetch(
        "http://127.0.0.1:5000/api/auth/login",
        {
            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                email,
                password
            })
        }
    );

    const data = await response.json();

    if(data.token){

        localStorage.setItem("token", data.token);

        window.location.href =
        "dashboard.html";

    }else{

        document.getElementById("message")
        .innerText = data.msg;
    }
}