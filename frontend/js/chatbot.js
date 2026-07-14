console.log("chatbot.js loaded successfully");

// ===========================================
// ELEMENTS
// ===========================================

const homeBtn = document.getElementById("homeBtn");

const clearChatBtn = document.getElementById("clearChatBtn");

const sendBtn = document.getElementById("sendBtn");

const userInput = document.getElementById("userInput");

const chatMessages = document.getElementById("chatMessages");

const policyCard = document.getElementById("policyCard");

const claimCard = document.getElementById("claimCard");

const quoteCard = document.getElementById("quoteCard");

const healthCard = document.getElementById("healthCard");

// ===========================================
// HOME
// ===========================================

homeBtn.onclick = () => {

    window.location.href = "home.html";

};

// ===========================================
// CLEAR CHAT
// ===========================================

clearChatBtn.onclick = () => {

    chatMessages.innerHTML = "";

};
    
// ===========================================
// QUICK ACTIONS
// ===========================================

policyCard.onclick = showPolicyChat;

claimCard.onclick = showClaimForm;

quoteCard.onclick = showQuoteSelection;

healthCard.onclick = showHealthQuoteForm;


// ===========================================
// All The Functions
// ===========================================

function showPolicyChat(){

    userInput.focus();

    userInput.placeholder =
    "Ask any policy related question...";

    addBotMessage(
        "👋 Ask me anything about your insurance policy, coverage, exclusions, renewal, premium or claims."
    );


function showClaimForm(){

    chatMessages.innerHTML += `

    <div class="bot-message">

        <div class="avatar">🤖</div>

        <div class="message">

        <h3>🚗 File Insurance Claim</h3>

        <form id="claimForm">

            <input type="text" id="customerName" placeholder="Customer Name" required>

            <select id="policyType">
                <option>Bike</option>
                <option>Car</option>
            </select>

            <input type="text" id="policyAge" placeholder="Policy Age">

            <input type="number" id="annualPremium" placeholder="Annual Premium">

            <input type="text" id="previousClaims" placeholder="Previous Claims">

            <input type="text" id="ncb" placeholder="NCB">

            <input type="text" id="zeroDep" placeholder="Zero Dep">

            <input type="text" id="engineProtection" placeholder="Engine Protection">

            <input type="text" id="state" placeholder="State">

            <input type="text" id="ageGroup" placeholder="Age Group">

            <input type="text" id="cityTier" placeholder="City Tier">

            <label><b>Upload Damage Images</b></label>

            <input
                type="file"
                id="claimImages"
                accept="image/*"
                multiple
            >

            <button type="submit">
                Submit Claim
            </button>

        </form>

        </div>

    </div>

    `;

    chatMessages.scrollTop =
    chatMessages.scrollHeight;

}

}

function showQuoteSelection(){

    chatMessages.innerHTML += `

    <div class="bot-message">

        <div class="avatar">🤖</div>

        <div class="message">

            <h3>Select Insurance Type</h3>

            <br>

            <button id="bikeBtn" class="chat-option-btn">

                🏍 Bike Insurance

            </button>

            <br><br>

            <button id="carBtn" class="chat-option-btn">

                🚘 Car Insurance

            </button>

        </div>

    </div>

    `;

    chatMessages.scrollTop =
    chatMessages.scrollHeight;

    document.getElementById("bikeBtn").onclick =
    showBikeQuoteForm;

    document.getElementById("carBtn").onclick =
    showCarQuoteForm;

}

function showBikeQuoteForm(){

chatMessages.innerHTML += `

<div class="bot-message">

<div class="avatar">🤖</div>

<div class="message">

<h3>🏍 Bike Insurance Quote</h3>

<form id="bikeQuoteForm">

<input type="number" placeholder="Vehicle Age">

<input type="number" placeholder="Engine CC">

<input type="text" placeholder="Brand">

<input type="text" placeholder="Fuel Type">

<input type="number" placeholder="Previous Claims">

<button>

Predict Premium

</button>

</form>

</div>

</div>

`;

chatMessages.scrollTop=
chatMessages.scrollHeight;

}

function showCarQuoteForm(){

chatMessages.innerHTML += `

<div class="bot-message">

<div class="avatar">🤖</div>

<div class="message">

<h3>🚘 Car Insurance Quote</h3>

<form id="carQuoteForm">

<input type="number" placeholder="Vehicle Age">

<input type="text" placeholder="Brand">

<input type="text" placeholder="Fuel Type">

<input type="number" placeholder="Engine Capacity">

<input type="number" placeholder="Previous Claims">

<button>

Predict Premium

</button>

</form>

</div>

</div>

`;

chatMessages.scrollTop=
chatMessages.scrollHeight;

}

function showHealthQuoteForm(){

chatMessages.innerHTML += `

<div class="bot-message">

<div class="avatar">🤖</div>

<div class="message">

<h3>❤️ Health Insurance Quote</h3>

<form id="healthQuoteForm">

<input type="number" placeholder="Age">

<select>

<option>Male</option>

<option>Female</option>

</select>

<input type="number" placeholder="BMI">

<select>

<option>Smoker</option>

<option>Non Smoker</option>

</select>

<input type="number" placeholder="Children">

<input type="text" placeholder="Region">

<button>

Predict Premium

</button>

</form>

</div>

</div>

`;

chatMessages.scrollTop=
chatMessages.scrollHeight;

}



// ===========================================
// SEND MESSAGE
// ===========================================

function addUserMessage(text){

    chatMessages.innerHTML += `

    <div class="user-message">

        <div class="message">

            ${text}

        </div>

    </div>

    `;

    chatMessages.scrollTop =
    chatMessages.scrollHeight;

}

// ===========================================
// BOT MESSAGE
// ===========================================

function addBotMessage(text){

    chatMessages.innerHTML += `

    <div class="bot-message">

        <div class="avatar">

            🤖

        </div>

        <div class="message">

            ${text}

        </div>

    </div>

    `;

    chatMessages.scrollTop =
    chatMessages.scrollHeight;

}

// ===========================================
// LOADING
// ===========================================

function showLoading(){

    chatMessages.innerHTML += `

    <div
        class="bot-message"
        id="loading"
    >

        <div class="avatar">

            🤖

        </div>

        <div class="message">

            Thinking...

        </div>

    </div>

    `;

}

function removeLoading(){

    const loading =
    document.getElementById("loading");

    if(loading){

        loading.remove();

    }

}

// ===========================================
// SEND MESSAGE
// ===========================================

async function sendMessage(){

    const question =
    userInput.value.trim();

    if(question==="") return;

    addUserMessage(question);

    userInput.value="";

    const lower =
    question.toLowerCase();

    // ===============================
    // ROUTER
    // ===============================

    if(

        lower.includes("claim")

        ||

        lower.includes("damage")

        ||

        lower.includes("accident")

    ){

        addBotMessage(

            "Redirecting you to Claim Service..."

        );

        setTimeout(()=>{

            window.location.href="claim.html";

        },1200);

        return;

    }

    if(

        lower.includes("quote")

        ||

        lower.includes("premium")

    ){

        addBotMessage(

            "Redirecting you to Premium Quotation..."

        );

        setTimeout(()=>{

            window.location.href="quote.html";

        },1200);

        return;

    }

    if(

        lower.includes("health")

    ){

        addBotMessage(

            "Opening Health Insurance..."

        );

        setTimeout(()=>{

            window.location.href="quote.html?type=health";

        },1200);

        return;

    }

    // ===============================
    // GEMINI CHAT
    // ===============================

    showLoading();

    try{

        const response =
        await fetch(

            `${BASE_URL}/chat`,

            {

                method:"POST",

                headers:{

                    "Content-Type":"application/json"

                },

                body:JSON.stringify({

                    user_query:question

                })

            }

        );

        const data =
        await response.json();

        removeLoading();

        addBotMessage(

            data.response

        );

    }

    catch(error){

        removeLoading();

        addBotMessage(

            "Unable to connect to AI Server."

        );

        console.log(error);

    }

}

// ===========================================
// BUTTON
// ===========================================

sendBtn.onclick = sendMessage;

// ===========================================
// ENTER KEY
// ===========================================

userInput.addEventListener(

    "keypress",

    function(e){

        if(e.key==="Enter"){

            sendMessage();

        }

    }

);