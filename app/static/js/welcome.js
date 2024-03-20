// Wait for the document to be ready
$(document).ready(function () {
    // Get the button element with class "btn-scroll-top"
    let btnScrollTop = $(".btn-scroll-top");

    // Attach a scroll event listener to the window
    $(window).scroll(function () {
        // Call the scrollFunction when scrolling occurs
        scrollFunction();
    });

    // Trigger the scroll event when the page loads
    $(window).trigger('scroll');

    // Define the scrollFunction
    function scrollFunction() {
        // Check if the scroll position is greater than or equal to 82 pixels
        if ($(document).scrollTop() >= 82) {
            // Show the btnScrollTop button
            btnScrollTop.show();
        } else {
            // Hide the btnScrollTop button
            btnScrollTop.hide();
        }
    }

    // Attach a click event listener to the btnScrollTop button
    btnScrollTop.click(function (event) {
        // Prevent the default click behavior
        event.preventDefault();
        // Scroll to the top of the page
        $("html").scrollTop(0);
        // Clear the window location hash
        window.location.hash = "";
        // Replace the current history state with an empty state
        history.replaceState(null, null, ' ');
    });
});