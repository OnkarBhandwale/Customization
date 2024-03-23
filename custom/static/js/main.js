$(document).ready(function () {
    // Add smooth scrolling to all links
    $("a").on("click", function (event) {
        // Make sure this.hash has a value before overriding default behavior
        if (this.hash !== "") {
            // Prevent default anchor click behavior
            event.preventDefault();

            // Store hash
            var hash = this.hash;

            // Using jQuery's animate() method to add smooth page scroll
            // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
            $("html, body").animate(
                {
                    scrollTop: $(hash).offset().top,
                },
                800,
                function () {
                    // Add hash (#) to URL when done scrolling (default click behavior)
                    window.location.hash = hash;
                }
            );
        } // End if
    });
});
document.getElementById("verifyEmailBtn").addEventListener("click", function() {
    // Send a request to the backend to initiate email verification
    fetch('/verify_email/', {
        method: 'POST',  // Or 'GET' depending on your backend implementation
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            // Include any necessary data in the request body
        })
    })
    .then(response => {
        if (response.ok) {
            alert("Verification email sent successfully!");
        } else {
            alert("Failed to send verification email. Please try again later.");
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert("An error occurred while sending the verification email.");
    });
});
