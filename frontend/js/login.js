console.log("login.js loaded successfully");

// =====================================
// ELEMENTS
// =====================================

const modal = document.getElementById("loginModal");

const loginBtn = document.getElementById("loginBtn");

const closeBtn = document.querySelector(".close");

const signin = document.getElementById("signinBtn");

const register = document.getElementById("registerBtn");

const loginForm = document.getElementById("loginForm");

const registerForm = document.getElementById("registerForm");

const customerBtn = document.getElementById("customerBtn");

const adminBtn = document.getElementById("adminBtn");

const successPopup = document.getElementById("successPopup");

const successTitle = document.getElementById("successTitle");

const successMessage = document.getElementById("successMessage");

const successOkBtn = document.getElementById("successOkBtn");

// =====================================
// OPEN LOGIN POPUP
// =====================================

loginBtn.onclick = () => {

    modal.style.display = "flex";

};

// =====================================
// CLOSE LOGIN POPUP
// =====================================

closeBtn.onclick = () => {

    modal.style.display = "none";

};

window.onclick = (e) => {

    if (e.target === modal) {

        modal.style.display = "none";

    }

};

// =====================================
// SIGN IN / REGISTER
// =====================================

signin.onclick = () => {

    signin.classList.add("active");

    register.classList.remove("active");

    loginForm.style.display = "block";

    registerForm.style.display = "none";

};

register.onclick = () => {

    register.classList.add("active");

    signin.classList.remove("active");

    loginForm.style.display = "none";

    registerForm.style.display = "block";

};

document.getElementById("togglePassword").onclick = () => {

    const input = document.getElementById("loginPassword");

    if(input.type === "password"){

        input.type = "text";

    }else{

        input.type = "password";

    }

};

// =====================================
// CUSTOMER / ADMIN
// =====================================

let isAdmin = false;

customerBtn.onclick = () => {

    isAdmin = false;

    customerBtn.classList.add("active");

    adminBtn.classList.remove("active");

};

adminBtn.onclick = () => {

    isAdmin = true;

    adminBtn.classList.add("active");

    customerBtn.classList.remove("active");

};

// =====================================
// CUSTOMER REGISTER
// =====================================

registerForm.addEventListener("submit", async (e) => {

    e.preventDefault();

    try {

        const response = await fetch(`${BASE_URL}/auth/register`, {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                customer_name: document.getElementById("customerName").value,

                email: document.getElementById("registerEmail").value,

                password: document.getElementById("registerPassword").value,

                phone: document.getElementById("phone").value,

                address: document.getElementById("address").value

            })

        });

        const data = await response.json();

        if (response.ok) {

            successTitle.innerText = "🎉 Welcome to ACKO";

            successMessage.innerText =
                "Account created successfully.";

            successPopup.style.display = "flex";

            successOkBtn.onclick = () => {

                successPopup.style.display = "none";

                registerForm.reset();

                signin.click();

            };

        }

        else {

            alert(data.detail);

        }

    }

    catch (err) {

        alert("Unable to connect to server.");

        console.log(err);

    }

});

// =====================================
// LOGIN
// =====================================

loginForm.addEventListener("submit", async (e) => {

    e.preventDefault();

    try {

        const endpoint = isAdmin

            ? "/auth/admin/login"

            : "/auth/customer/login";

        const response = await fetch(`${BASE_URL}${endpoint}`, {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                email: document.getElementById("loginEmail").value,

                password: document.getElementById("loginPassword").value

            })

        });

        const data = await response.json();

        console.log(data);

        if (response.ok) {

                localStorage.setItem(
                "customerName",
                data.customer_name
                );

                localStorage.setItem(
                "customerId",
                data.customer_id
                );

                localStorage.setItem("customerEmail", data.email);

            successTitle.innerText = "✅ Login Successful";

            successMessage.innerText =
                "Welcome back to ACKO Insurance.";

            successPopup.style.display = "flex";

            successOkBtn.onclick = () => {

                successPopup.style.display = "none";

                modal.style.display = "none";


                if (isAdmin) {

                    window.location.href = "dashboard.html";

                }

                else {

                    window.location.href = "home.html";

                }

            };

        }

       else{

            successTitle.innerText = "❌ Login Failed";

            successMessage.innerText = "Invalid email or password.";

            successPopup.style.display = "flex";

            successOkBtn.onclick = () => {

                successPopup.style.display = "none";

                document.getElementById("loginEmail").value = "";

                document.getElementById("loginPassword").value = "";

                document.getElementById("loginEmail").focus();

};

}

    }

    catch (err) {

        alert("Unable to connect to server.");

        console.log(err);

    }

});