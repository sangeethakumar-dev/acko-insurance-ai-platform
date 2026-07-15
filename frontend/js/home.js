document.getElementById("chatbotBtn").onclick = () => {

    window.location.href = "home.html";

};

const customerName = localStorage.getItem("customerName");

if(customerName){

    document.getElementById("welcomeUser").innerHTML =

        `Welcome Back ${customerName} 👋`;

}

// ===================================
// AI ASSISTANT
// ===================================

document.getElementById("chatbotBtn").onclick = () => {

    window.location.href = "chatbot.html";

};

document.getElementById("exploreBtn").onclick = () => {

    document.getElementById("services").scrollIntoView({

        behavior:"smooth"

    });

}; 

// ===================================
// LOGOUT
// ===================================
document.getElementById("logoutBtn").onclick = () => {

    localStorage.clear();

    window.location.href="index.html";

};

// ===================================
// QUICK ACTIONS
// ===================================

document.getElementById("quoteCard").onclick = () => {
    window.location.href = "chatbot.html?form=bike";
};

document.getElementById("healthCard").onclick = () => {
    window.location.href = "chatbot.html?form=health";
};

document.getElementById("claimCard").onclick = () => {
    window.location.href = "chatbot.html?form=claim";
};