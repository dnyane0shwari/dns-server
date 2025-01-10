function resolveDomain() {
    let domain = document.getElementById("domain").value;

    fetch("/resolve", {
        method: "POST",
        body: new URLSearchParams({ "domain": domain }),
        headers: { "Content-Type": "application/x-www-form-urlencoded" }
    })
    .then(response => response.json())
    .then(data => {
        let resultDiv = document.getElementById("result");
        if (data.status === "success") {
            resultDiv.innerHTML = "<b>Resolved IP Addresses:</b> " + data.ip_addresses.join(", ");
        } else {
            resultDiv.innerHTML = "<b>Error:</b> " + data.message;
        }
    })
    .catch(error => console.error("Error:", error));
}
