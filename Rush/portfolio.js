document.addEventListener("DOMContentLoaded", () => {
    // Smooth scroll for all anchor links within the portfolio screen
    document.querySelectorAll(".navbar a:not(#back-btn)").forEach(link => {
        link.addEventListener("click", e => {
            e.preventDefault();
            const targetId = link.getAttribute("href");
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                // Get the main portfolio screen container
                const portfolioScreen = document.getElementById('portfolio');

                // Calculate the target position with an offset for the fixed navbar
                const offsetTop = targetElement.offsetTop - 100;

                // Perform the smooth scroll
                portfolioScreen.scrollTo({
                    top: offsetTop,
                    behavior: "smooth"
                });
            }
        });
    });
});
