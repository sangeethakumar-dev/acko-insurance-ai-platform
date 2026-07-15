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

}

///////////////////////////////////////////////////////////


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

async function showBikeQuoteForm(){

    const response = await fetch("forms/bikeQuoteForm.html");

    const html = await response.text();

    chatMessages.insertAdjacentHTML("beforeend", html);

    chatMessages.scrollTop =
        chatMessages.scrollHeight;

    document
        .getElementById("bikeQuoteForm")
        .addEventListener(
            "submit",
            submitBikeQuote
        );

    const bikeData = {

Honda:{
models:["Activa 6G","Shine","SP125","Hornet 2.0"]
},

TVS:{
models:["Apache RTR 160","Apache RTR 200","Jupiter","NTorq"]
},

Hero:{
models:["Splendor Plus","Xtreme 160R","Pleasure+"]
},

Bajaj:{
models:["Pulsar N160","Pulsar NS200","CT110"]
},

Yamaha:{
models:["FZ-X","R15 V4","RayZR"]
},

"Royal Enfield":{
models:["Classic 350","Hunter 350","Meteor 350"]
}

};

const make=document.getElementById("vehicle_make");
const model=document.getElementById("vehicle_model");

console.log(make);
console.log(model);

make.onchange=function(){

model.innerHTML = `
<option value="" selected disabled>
    Select Vehicle Model
</option>
`;

if(!bikeData[this.value]) return;

bikeData[this.value].models.forEach(m=>{

model.innerHTML += `<option>${m}</option>`;

});

model.value = "";

};

make.value = "";

    const variant=document.getElementById("variant");

    console.log(variant);

    const variants={

"Activa 6G":[
"Standard",
"Deluxe",
"H-Smart"
],

"Shine":[
"Drum",
"Disc"
],

"SP125":[
"Drum",
"Disc"
],

"Hornet 2.0":[
"Standard",
"Repsol Edition"
],

"Apache RTR 160":[
"Single Disc",
"Dual Disc"
],

"Apache RTR 200":[
"Race Edition",
"Dual ABS"
],

"Jupiter":[
"ZX",
"Classic"
],

"NTorq":[
"Race XP",
"Super Squad"
],

"Splendor Plus":[
"Self",
"Xtec"
],

"Xtreme 160R":[
"Standard",
"Connected"
],

"Pleasure+":[
"LX",
"VX"
],

"Pulsar N160":[
"Single ABS",
"Dual ABS"
],

"Pulsar NS200":[
"Standard",
"Bluetooth Edition"
],

"CT110":[
"Kick",
"Electric Start"
],

"FZ-X":[
"Standard",
"Chrome"
],

"R15 V4":[
"Metallic",
"MotoGP Edition"
],

"RayZR":[
"Street Rally",
"Disc"
],

"Classic 350":[
"Redditch",
"Halcyon",
"Signals"
],

"Hunter 350":[
"Retro",
"Metro"
],

"Meteor 350":[
"Fireball",
"Stellar",
"Supernova"
]

};

model.onchange=function(){

variant.innerHTML = `
<option value="" selected disabled>
    Select Variant
</option>
`;

if(!variants[this.value]) return;

variants[this.value].forEach(v=>{

variant.innerHTML += `<option>${v}</option>`;

});

};

model.dispatchEvent(new Event("change"));

}


async function submitBikeQuote(e){

    e.preventDefault();

    const form = document.getElementById("bikeQuoteForm");

    showLoading();

    const payload = {

        insurance_type: "bike",

        details: {

            customer_age: Number(form.elements["customer_age"].value),

            city: form.elements["city"].value,

            state: form.elements["state"].value,

            city_tier: Number(form.elements["city_tier"].value),

            city_risk_score: Number(form.elements["city_risk_score"].value),

            vehicle_make: form.elements["vehicle_make"].value,

            vehicle_model: form.elements["vehicle_model"].value,

            variant: form.elements["variant"].value,

            segment: form.elements["segment"].value,

            fuel_type: form.elements["fuel_type"].value,

            colour: form.elements["colour"].value,

            manufacturing_year: Number(form.elements["manufacturing_year"].value),

            vehicle_age_years: Number(form.elements["vehicle_age_years"].value),

            engine_cc: Number(form.elements["engine_cc"].value),

            idv: Number(form.elements["idv"].value),

            ncb_percent: Number(form.elements["ncb_percent"].value),

            claim_history_count: Number(form.elements["claim_history_count"].value),

            policy_type: form.elements["policy_type"].value,

            usage_type: form.elements["usage_type"].value,

            num_addons: Number(form.elements["num_addons"].value)

        }

    };

    console.log(payload);

    try{

        const response = await fetch(

            `${BASE_URL}/predict-quote`,

            {

                method:"POST",

                headers:{

                    "Content-Type":"application/json"

                },

                body:JSON.stringify(payload)

            }

        );

        console.log(response.status);

        const data = await response.json();

        let responseText = data.assistant_response;

responseText = responseText
.replace(/\*\*/g,"")
.replace(/\*/g,"")
.replace(/##/g,"")
.replace(/#/g,"")
.replace(/\n/g,"<br>"); 

        console.log(data);

        removeLoading();

addBotMessage(`

<div class="premium-card">

    <div class="premium-top">

        <div>

            <div class="premium-title">

                ACKO INSURANCE QUOTE

            </div>

            <div class="premium-vehicle">

                <div class="vehicle-name">

                    ${payload.details.manufacturing_year || ""}
                    ${payload.details.vehicle_make || ""}
                    ${payload.details.vehicle_model || ""}

                </div>

                <div class="vehicle-info">

                    ${payload.details.variant || ""}
                    •
                    ${payload.details.fuel_type || ""}

                </div>

            </div>

        </div>

        <div class="premium-date">

            Generated Today

        </div>

    </div>

    <div class="premium-box">

        <div class="premium-label">

            ESTIMATED ANNUAL PREMIUM

        </div>

        <div class="premium-price">

            ₹${data.predicted_premium.toLocaleString()}

        </div>

        <div class="premium-month">

            ≈ ₹${(data.predicted_premium/12).toFixed(0)} / month

        </div>

    </div>

    <table class="premium-table">

        <tr>

            <td>IDV</td>

            <td>₹${payload.details.idv}</td>

        </tr>

        <tr>

            <td>No Claim Bonus</td>

            <td>${payload.details.ncb_percent}%</td>

        </tr>

        <tr>

            <td>Add-ons</td>

            <td>${payload.details.num_addons}</td>

        </tr>

        <tr>

            <td>Registered State</td>

            <td>${payload.details.state}</td>

        </tr>

        <tr>

            <td>Policy</td>

            <td>${payload.details.policy_type}</td>

        </tr>

    </table>

    <div class="premium-summary">

        ${responseText}

    </div>

</div>

`);

    }

    catch(err){

        removeLoading();

        addBotMessage(

            "Prediction Failed."

        );

        console.log(err);

    }

}

async function showCarQuoteForm(){

    const response = await fetch("forms/carQuoteForm.html");

    const html = await response.text();

    chatMessages.insertAdjacentHTML("beforeend", html);

    chatMessages.scrollTop = chatMessages.scrollHeight;

    document
        .getElementById("carQuoteForm")
        .addEventListener(
            "submit",
            submitCarQuote
        );

    const carData = {

        Hyundai:{
            models:[
                "i20",
                "Creta",
                "Venue",
                "Verna"
            ]
        },

        "Maruti Suzuki":{
            models:[
                "Swift",
                "Baleno",
                "Brezza",
                "Dzire"
            ]
        },

        Tata:{
            models:[
                "Punch",
                "Nexon",
                "Altroz",
                "Harrier"
            ]
        },

        Mahindra:{
            models:[
                "XUV300",
                "XUV700",
                "Scorpio N",
                "Thar"
            ]
        },

        Honda:{
            models:[
                "Amaze",
                "City",
                "Elevate"
            ]
        },

        Toyota:{
            models:[
                "Glanza",
                "Urban Cruiser Hyryder",
                "Innova Hycross"
            ]
        },

        Kia:{
            models:[
                "Sonet",
                "Seltos",
                "Carens"
            ]
        },

        MG:{
            models:[
                "Astor",
                "Hector",
                "Comet EV"
            ]
        }

    };

    const make = document.getElementById("vehicle_make");
    const model = document.getElementById("vehicle_model");


    make.onchange = function(){

    // Reset Vehicle Model dropdown
    model.innerHTML = `
        <option value="" selected disabled>
            Select Vehicle Model
        </option>
    `;

    // Reset Variant dropdown
    variant.innerHTML = `
        <option value="" selected disabled>
            Select Variant
        </option>
    `;

    if(!carData[this.value]) return;

    carData[this.value].models.forEach(m=>{

        model.innerHTML += `<option>${m}</option>`;

    });

};

    make.dispatchEvent(new Event("change"));



    const variant = document.getElementById("variant");

    const variants = {

        "i20":[
            "Magna",
            "Sportz",
            "Asta"
        ],

        "Creta":[
            "E",
            "S",
            "SX",
            "SX(O)"
        ],

        "Venue":[
            "E",
            "S",
            "SX"
        ],

        "Verna":[
            "EX",
            "SX",
            "SX(O)"
        ],

        "Swift":[
            "LXi",
            "VXi",
            "ZXi"
        ],

        "Baleno":[
            "Sigma",
            "Delta",
            "Zeta",
            "Alpha"
        ],

        "Brezza":[
            "LXi",
            "VXi",
            "ZXi"
        ],

        "Dzire":[
            "LXi",
            "VXi",
            "ZXi"
        ],

        "Punch":[
            "Pure",
            "Adventure",
            "Accomplished"
        ],

        "Nexon":[
            "Smart",
            "Pure",
            "Creative",
            "Fearless"
        ],

        "Altroz":[
            "XE",
            "XM",
            "XZ"
        ],

        "Harrier":[
            "Smart",
            "Pure",
            "Fearless"
        ],

        "XUV300":[
            "W2",
            "W4",
            "W6",
            "W8"
        ],

        "XUV700":[
            "MX",
            "AX3",
            "AX5",
            "AX7"
        ],

        "Scorpio N":[
            "Z2",
            "Z4",
            "Z6",
            "Z8"
        ],

        "Thar":[
            "AX(O)",
            "LX"
        ],

        "Amaze":[
            "E",
            "S",
            "VX"
        ],

        "City":[
            "V",
            "VX",
            "ZX"
        ],

        "Elevate":[
            "SV",
            "V",
            "VX",
            "ZX"
        ],

        "Glanza":[
            "E",
            "S",
            "G",
            "V"
        ],

        "Urban Cruiser Hyryder":[
            "E",
            "S",
            "G",
            "V"
        ],

        "Innova Hycross":[
            "GX",
            "VX",
            "ZX"
        ],

        "Sonet":[
            "HTE",
            "HTK",
            "HTX",
            "GTX+"
        ],

        "Seltos":[
            "HTE",
            "HTK",
            "HTX",
            "GTX+"
        ],

        "Carens":[
            "Premium",
            "Prestige",
            "Luxury"
        ],

        "Astor":[
            "Sprint",
            "Shine",
            "Select",
            "Sharp"
        ],

        "Hector":[
            "Style",
            "Shine",
            "Smart",
            "Sharp"
        ],

        "Comet EV":[
            "Pace",
            "Play",
            "Plush"
        ]

    };

    model.onchange = function(){

    variant.innerHTML = `
        <option value="" selected disabled>
            Select Variant
        </option>
    `;

    if(!variants[this.value]) return;

    variants[this.value].forEach(v=>{

        variant.innerHTML += `<option>${v}</option>`;

    });

};

    make.dispatchEvent(new Event("change"));

}


async function submitCarQuote(e){

    e.preventDefault();

    const form = document.getElementById("carQuoteForm");

    showLoading();

    const payload = {

        insurance_type: "car",

        details: {

            customer_age: Number(form.elements["customer_age"].value),

            city: form.elements["city"].value,

            state: form.elements["state"].value,

            city_tier: Number(form.elements["city_tier"].value),

            city_risk_score: Number(form.elements["city_risk_score"].value),

            vehicle_make: form.elements["vehicle_make"].value,

            vehicle_model: form.elements["vehicle_model"].value,

            variant: form.elements["variant"].value,

            segment: form.elements["segment"].value,

            fuel_type: form.elements["fuel_type"].value,

            colour: form.elements["colour"].value,

            manufacturing_year: Number(form.elements["manufacturing_year"].value),

            vehicle_age_years: Number(form.elements["vehicle_age_years"].value),

            engine_cc: Number(form.elements["engine_cc"].value),

            idv: Number(form.elements["idv"].value),

            ncb_percent: Number(form.elements["ncb_percent"].value),

            claim_history_count: Number(form.elements["claim_history_count"].value),

            policy_type: form.elements["policy_type"].value,

            previous_insurer: form.elements["previous_insurer"].value,

            num_addons: Number(form.elements["num_addons"].value)

        }

    };

    console.log(payload);

    try{

        const response = await fetch(

            `${BASE_URL}/predict-quote`,

            {

                method:"POST",

                headers:{

                    "Content-Type":"application/json"

                },

                body:JSON.stringify(payload)

            }

        );

        console.log(response.status);

        const data = await response.json();

        let responseText = data.assistant_response;

        responseText = responseText
        .replace(/\*\*/g,"")
        .replace(/\*/g,"")
        .replace(/##/g,"")
        .replace(/#/g,"")
        .replace(/\n/g,"<br>");

        console.log(data);

        removeLoading();

        addBotMessage(`

<div class="premium-card">

    <div class="premium-top">

        <div>

            <div class="premium-title">

                ACKO INSURANCE QUOTE

            </div>

            <div class="premium-vehicle">

    <div class="vehicle-name">

        ${payload.details.manufacturing_year || ""}
        ${payload.details.vehicle_make || ""}
        ${payload.details.vehicle_model || ""}

    </div>

    <div class="vehicle-info">

        ${payload.details.variant || ""}
        •
        ${payload.details.fuel_type || ""}

    </div>

</div>

            </div>

        <div class="premium-date">

            Generated Today

        </div>

    </div>

    <div class="premium-box">

        <div class="premium-label">

            ESTIMATED ANNUAL PREMIUM

        </div>

        <div class="premium-price">

            ₹${Number(data.predicted_premium).toLocaleString()}

        </div>

        <div class="premium-month">

            ≈ ₹${(Number(data.predicted_premium)/12).toFixed(0)} / month

        </div>

    </div>

    <table class="premium-table">

        <tr>

            <td>IDV</td>

            <td>₹${payload.details.idv}</td>

        </tr>

        <tr>

            <td>No Claim Bonus</td>

            <td>${payload.details.ncb_percent}%</td>

        </tr>

        <tr>

            <td>Add-ons</td>

            <td>${payload.details.num_addons}</td>

        </tr>

        <tr>

            <td>Registered State</td>

            <td>${payload.details.state}</td>

        </tr>

        <tr>

            <td>Policy</td>

            <td>${payload.details.policy_type}</td>

        </tr>

        <tr>

            <td>Previous Insurer</td>

            <td>${payload.details.previous_insurer}</td>

        </tr>

    </table>

    <div class="premium-summary">

        ${responseText}

    </div>

</div>

`);

    }

    catch(err){

        removeLoading();

        addBotMessage("Prediction Failed.");

        console.log(err);

    }

}

// ===========================================
// SHOW HEALTH QUOTE FORM
// ===========================================

async function showHealthQuoteForm(){

    const response =
        await fetch("forms/healthQuoteForm.html");

    const html =
        await response.text();

    chatMessages.insertAdjacentHTML(
        "beforeend",
        html
    );

    chatMessages.scrollTop =
        chatMessages.scrollHeight;

    document
        .getElementById("healthQuoteForm")
        .addEventListener(
            "submit",
            submitHealthQuote
        );

}

async function submitHealthQuote(e){

    e.preventDefault();

    const form = document.getElementById("healthQuoteForm");

    showLoading();

    const payload = {

        insurance_type: "health",

        details: {

            plan_name: form.elements["plan_name"].value,

            plan_category: form.elements["plan_category"].value,

            age: Number(form.elements["age"].value),

            gender: form.elements["gender"].value,

            num_members: Number(form.elements["num_members"].value),

            city_tier: Number(form.elements["city_tier"].value),

            state: form.elements["state"].value,

            bmi_category: form.elements["bmi_category"].value,

            smoke: form.elements["smoke"].value === "Yes" ? 1 : 0,

            has_pre_existing: form.elements["has_pre_existing"].value === "Yes" ? 1 : 0,

            annual_checkup: form.elements["annual_checkup"].value === "Yes" ? 1 : 0,

            ncb_years: Number(form.elements["ncb_years"].value),

            sum_insured: Number(form.elements["sum_insured"].value),

            deductible: Number(form.elements["deductible"].value),

            num_addons: Number(form.elements["num_addons"].value),

            addons_list: form.elements["addons_list"].value,

            has_maternity: form.elements["has_maternity"].value === "Yes" ? 1 : 0,

            has_opd: form.elements["has_opd"].value === "Yes" ? 1 : 0,

            policy_tenure: Number(form.elements["policy_tenure"].value),

            prev_insurer: form.elements["prev_insurer"].value

        }

    };

    console.log("Health Payload");
    console.log(JSON.stringify(payload, null, 2));

    try{

        const response = await fetch(

            `${BASE_URL}/predict-quote`,

            {

                method:"POST",

                headers:{

                    "Content-Type":"application/json"

                },

                body:JSON.stringify(payload)

            }

        );

        console.log(response.status);

        const data = await response.json();

        let responseText = data.assistant_response;

        responseText = responseText
            .replace(/\*\*/g,"")
            .replace(/\*/g,"")
            .replace(/##/g,"")
            .replace(/#/g,"")
            .replace(/\n/g,"<br>");

        console.log(data);

                removeLoading();

        addBotMessage(`

<div class="premium-card">

    <div class="premium-top">

        <div>

            <div class="premium-title">

                ACKO HEALTH INSURANCE

            </div>

            <div class="premium-vehicle">

                <div class="vehicle-name">

                    ${payload.details.plan_name || ""}

                </div>

                <div class="vehicle-info">

                    ${payload.details.plan_category || ""}
                    •
                    ${payload.details.num_members || ""} Member(s)

                </div>

            </div>

        </div>

        <div class="premium-date">

            Generated Today

        </div>

    </div>

    <div class="premium-box">

        <div class="premium-label">

            ESTIMATED ANNUAL PREMIUM

        </div>

        <div class="premium-price">

            ₹${Number(data.predicted_premium).toLocaleString()}

        </div>

        <div class="premium-month">

            ≈ ₹${(Number(data.predicted_premium)/12).toFixed(0)} / month

        </div>

    </div>

    <table class="premium-table">

        <tr>

            <td>Age</td>

            <td>${payload.details.age} Years</td>

        </tr>

        <tr>

            <td>Gender</td>

            <td>${payload.details.gender}</td>

        </tr>

        <tr>

            <td>Sum Insured</td>

            <td>₹${Number(payload.details.sum_insured).toLocaleString()}</td>

        </tr>

        <tr>

            <td>Policy Tenure</td>

            <td>${payload.details.policy_tenure} Year(s)</td>

        </tr>

        <tr>

            <td>Add-ons</td>

            <td>${payload.details.num_addons}</td>

        </tr>

        <tr>

            <td>Previous Insurer</td>

            <td>${payload.details.prev_insurer}</td>

        </tr>

    </table>

    <div class="premium-summary">

        ${responseText}

    </div>

</div>

`);

    }

    catch(err){

        removeLoading();

        addBotMessage(

            "Prediction Failed."

        );

        console.log(err);

    }

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

    const question = userInput.value.trim();

    if(question === "") return;

    addUserMessage(question);

    userInput.value = "";

    showLoading();

    try{

        const response = await fetch(

            `${BASE_URL}/chat`,

            {

                method:"POST",

                headers:{

                    "Content-Type":"application/json"

                },

                body:JSON.stringify({

                    user_query: question

                })

            }

        );

        const data = await response.json();

        console.log("CHAT RESPONSE:", data);

        removeLoading();

        // ===================================
        // AI WORKFLOW DETECTION
        // ===================================

        if(data.workflow === "quote"){

        addBotMessage(data.message);

            if(data.insurance_type === "bike"){

            await showBikeQuoteForm();

            }

        else if(data.insurance_type === "car"){

            await showCarQuoteForm();

            }

        else if(data.insurance_type === "health"){

            await showHealthQuoteForm();

        }

        return;

}

// ===================================
// CLAIM WORKFLOW
// ===================================

if(data.workflow === "claim"){

    addBotMessage(data.message);

    await showClaimForm();

    return;

}

        // ===================================
        // NORMAL RAG CHAT
        // ===================================

        addBotMessage(data.response);

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

const bikeModels = {

    Honda: [

        "Activa 6G",

        "Dio 125",

        "Shine",

        "SP125"

    ],

    Hero: [

        "Splendor Plus",

        "HF Deluxe",

        "Xtreme 160R"

    ],

    TVS: [

        "Jupiter",

        "Apache RTR 160",

        "Apache RTR 200",

        "NTorq"

    ],

    Bajaj: [

        "Pulsar 150",

        "Pulsar NS200",

        "Dominar 400"

    ],

    Yamaha: [

        "FZ",

        "R15",

        "MT15"

    ],

    Suzuki: [

        "Access 125",

        "Gixxer"

    ],

    "Royal Enfield":[

        "Classic 350",

        "Meteor 350",

        "Hunter 350"

    ]

};