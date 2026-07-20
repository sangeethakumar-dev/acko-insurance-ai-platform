

async function showClaimForm() {

    const response = await fetch("forms/claimForm.html");

    const html = await response.text();

    chatMessages.insertAdjacentHTML("beforeend", html);

    chatMessages.scrollTop =
        chatMessages.scrollHeight;

        
    const form = document.getElementById("claimForm");

console.log("FORM FOUND:", form);

form.onsubmit = function(e){


    e.preventDefault();

    console.log("SUBMIT EVENT FIRED");

    submitClaim(e);

    return false;
};

console.log("Submit listener attached");


    // ================= IMAGE VALIDATION =================

    const imageInput =
        document.getElementById("claim_images");

    imageInput.addEventListener(
        "change",
        function () {

            const files = this.files;

            if (files.length > 6) {

                alert(
                    "You can upload a maximum of 6 images."
                );

                this.value = "";

                return;
            }

            if (files.length === 0) {

                alert(
                    "Please upload at least one damage image."
                );

                return;
            }

            const allowedTypes = [
                "image/jpeg",
                "image/jpg",
                "image/png"
            ];

            for (let file of files) {

                if (!allowedTypes.includes(file.type)) {

                    alert(
                        "Only JPG, JPEG and PNG images are allowed."
                    );

                    this.value = "";

                    return;
                }

            }

        }

    );

}

async function submitClaim(e){

    try{

    console.log("submitClaim() called");

    console.log("1. submitClaim started");

    e.preventDefault();

    console.log("2. preventDefault done");


    const form = document.getElementById("claimForm");

    console.log(form);

    console.log("A");

    console.log("3. form found", form);

if (!form) {
    alert("FORM NOT FOUND");
    return;
}

    //showLoading();

    console.log("4. loading shown");

    console.log("STEP 1");

    const formData = new FormData();

    console.log("B");

    console.log("5. formData created");

    console.log("STEP 2");

    // ================= IMAGES =================
    console.log(document.querySelectorAll("#claim_images").length);

    const imageFiles =
        form.elements["images"].files;

        console.log(imageFiles);
console.log(imageFiles.length);

        console.log("C");

        console.log("Image count:", imageFiles.length);

        if (imageFiles.length === 0) {
    alert("No image selected");
    return;
}

        console.log("6. imageFiles", imageFiles);

        console.log("STEP 3");
console.log(imageFiles);

        console.log(imageFiles);

        console.log("D");
        console.log(imageFiles.length);

    formData.append("images", imageFiles[0]);

    console.log("Image appended");

    console.log("E");

    console.log("7. image appended");

    console.log("STEP 4");


    // ================= CUSTOMER DETAILS =================

    formData.append(
        "customer_name",
        form.elements["customer_name"].value
    );

    console.log("F");

    // ================= POLICY DETAILS =================

    console.log("policy_type element =", form.elements["policy_type"]);

    formData.append(    
        "policy_type",
        form.elements["policy_type"].value
    );

    console.log("G");

    console.log(form.elements["policy_age"]);

    formData.append(
        "policy_age",
        form.elements["policy_age"].value
    );

    console.log("H");

    console.log(form.elements["annual_premium"]);

    formData.append(
        "annual_premium",
        form.elements["annual_premium"].value
    );

    console.log("I");

    console.log(form.elements["vehicle_age"]);

    formData.append(
        "vehicle_age",
        form.elements["vehicle_age"].value
    );

    console.log("J");

    console.log(form.elements["idv"]);

    formData.append(
        "idv",
        form.elements["idv"].value
    );

    console.log("K");

    // ================= COVERAGE DETAILS =================

    console.log(form.elements["previous_claims"]);

    formData.append(
        "previous_claims",
        form.elements["previous_claims"].value
    );

    console.log("L");

    console.log(form.elements["ncb"]);

    formData.append(
        "ncb",
        form.elements["ncb"].value
    );

    console.log("M");

    console.log(form.elements["zero_dep"]);

    formData.append(
        "zero_dep",
        form.elements["zero_dep"].value
    );

    console.log("N");

    console.log(form.elements["engine_protection"]);

    formData.append(
        "engine_protection",
        form.elements["engine_protection"].value
    );

    console.log("O");

    // ================= LOCATION =================

    console.log(form.elements["state"]);

    formData.append(
        "state",
        form.elements["state"].value
    );

    console.log("P");

    console.log(form.elements["age_group"]);

    formData.append(
        "age_group",
        form.elements["age_group"].value
    );

    console.log("Q");

    console.log(form.elements["city_tier"]);
    
    formData.append(
        "city_tier",
        form.elements["city_tier"].value
    );

    console.log("R");

    for (const pair of formData.entries()) {
    console.log(pair[0], pair[1]);
}

        console.log(formData);

        console.log("STEP 5");
        
        console.log("BEFORE FETCH");

        const response = await fetch(

            `${BASE_URL}/claim/analyze`,

            {

                method: "POST",

                body: formData

            }

        );

        console.log("AFTER FETCH");

    console.log("STEP 6");
        console.log("Status:", response.status);

        console.log("Status:", response.status);

        if (!response.ok) {
    throw new Error("Backend Error");
}

        const data = await response.json();

        console.log("FULL RESPONSE");
        console.log(data);

        alert(JSON.stringify(data));

        console.log("========== CLAIM RESPONSE ==========");
        console.log(data);
        console.log("REPORT:");
        console.log(data.report);
        console.log("====================================");

        console.log(response.status);


        console.log(data);

                removeLoading();

        addBotMessage(`

<div class="premium-card">

    <div class="premium-top">

        <div>

            <div class="premium-title">

                ACKO CLAIM ASSESSMENT

            </div>

            <div class="premium-vehicle">

                <div class="vehicle-name">

                    ${data.analysis.brand || ""}
                    ${data.analysis.model || ""}

                </div>

                <div class="vehicle-info">

                    ${data.analysis.vehicle_type || ""}
                    •
                    ${data.analysis.color || ""}

                </div>

            </div>

        </div>

        <div class="premium-date">

            Claim Analysis Completed

        </div>

    </div>

    <div class="premium-box">

        <div class="premium-label">

            RECOMMENDED CLAIM PAYOUT

        </div>

        <div class="premium-price">

            ₹${data.claim.recommended_payout.toLocaleString()}

        </div>

        <div class="premium-month">

            Estimated Repair :
            ₹${data.claim.repair_cost.toLocaleString()}

        </div>

    </div>

    <table class="premium-table">

        <tr>

            <td>Claim Number</td>

            <td>${data.claim_number}</td>

        </tr>

        <tr>

            <td>Coverage</td>

            <td>${data.claim.coverage}</td>

        </tr>

        <tr>

            <td>Damage Type</td>

            <td>${data.analysis.damage_type}</td>

        </tr>

        <tr>

            <td>Severity</td>

            <td>${data.analysis.severity} / 10</td>

        </tr>

        <tr>

            <td>Fraud Risk</td>

            <td>${data.fraud.fraud_risk}</td>

        </tr>

        <tr>

            <td>Manual Review</td>

            <td>

                ${data.claim.manual_review ? "Required" : "Not Required"}

            </td>

        </tr>

    </table>

    <div class="premium-summary">

        <b>AI Damage Summary</b>

        <br><br>

        ${data.report || "No AI report available."}

        <br><br>

        <b>Affected Parts</b>

        <br>

        ${(data.analysis.affected_parts || []).join(", ")}

        <br><br>

        <b>Remarks</b>

        <br>

        ${(data.claim.remarks || []).join("<br>")}

    </div>

</div>

`);

    }

    catch(err){

        console.error("submitClaim ERROR:", err);

        alert(err.message);

        removeLoading();

        console.log(err);

        addBotMessage(`

<div class="premium-card">

    <div class="premium-top">

        <div>

            <div class="premium-title">

                CLAIM ANALYSIS FAILED

            </div>

            <div class="premium-vehicle">

                Something went wrong while processing your claim.

            </div>

        </div>

    </div>

    <div class="premium-summary">

        Please verify the following:

        <br><br>

        • Upload only JPG, JPEG or PNG images.

        <br>

        • Upload a maximum of 6 images.

        <br>

        • Ensure all mandatory fields are filled.

        <br>

        • Make sure the FastAPI server is running.

        <br>

        • Try again after a few seconds.

    </div>

</div>

`);

    }

}