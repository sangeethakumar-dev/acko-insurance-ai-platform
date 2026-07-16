async function showClaimForm() {

    const response = await fetch("forms/claimForm.html");

    const html = await response.text();

    chatMessages.insertAdjacentHTML("beforeend", html);

    chatMessages.scrollTop =
        chatMessages.scrollHeight;

    document
        .getElementById("claimForm")
        .addEventListener(
            "submit",
            submitClaim
        );

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

    e.preventDefault();

    const form = document.getElementById("claimForm");

    showLoading();

    const formData = new FormData();

    // ================= IMAGES =================
    console.log(document.querySelectorAll("#claim_images").length);

    const imageFiles =
        form.elements["images"].files;

        console.log(imageFiles);
        console.log(imageFiles.length);

    formData.append("images", imageFiles[0]);


    // ================= CUSTOMER DETAILS =================

    formData.append(
        "customer_name",
        form.elements["customer_name"].value
    );

    // ================= POLICY DETAILS =================

    formData.append(
        "policy_type",
        form.elements["policy_type"].value
    );

    formData.append(
        "policy_age",
        form.elements["policy_age"].value
    );

    formData.append(
        "annual_premium",
        form.elements["annual_premium"].value
    );

    formData.append(
        "vehicle_age",
        form.elements["vehicle_age"].value
    );

    formData.append(
        "idv",
        form.elements["idv"].value
    );

    // ================= COVERAGE DETAILS =================

    formData.append(
        "previous_claims",
        form.elements["previous_claims"].value
    );

    formData.append(
        "ncb",
        form.elements["ncb"].value
    );

    formData.append(
        "zero_dep",
        form.elements["zero_dep"].value
    );

    formData.append(
        "engine_protection",
        form.elements["engine_protection"].value
    );

    // ================= LOCATION =================

    formData.append(
        "state",
        form.elements["state"].value
    );

    formData.append(
        "age_group",
        form.elements["age_group"].value
    );

    formData.append(
        "city_tier",
        form.elements["city_tier"].value
    );

    for (const pair of formData.entries()) {
    console.log(pair[0], pair[1]);
}

    try{

        console.log(formData);

        const response = await fetch(

            `${BASE_URL}/claim/analyze`,

            {

                method: "POST",

                body: formData

            }

        );

        console.log("Status:", response.status);

        console.log("Status:", response.status);

        const data = await response.json();

        console.log(data);

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

        ${data.analysis.summary}

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