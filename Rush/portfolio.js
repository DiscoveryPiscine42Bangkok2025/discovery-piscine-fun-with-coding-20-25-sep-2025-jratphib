document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".navbar a:not(#back-btn)").forEach(link => {
        link.addEventListener("click", e => {
            e.preventDefault();
            const targetId = link.getAttribute("href");
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                const portfolioScreen = document.getElementById('portfolio');
                const offsetTop = targetElement.offsetTop - 100;

                portfolioScreen.scrollTo({
                    top: offsetTop,
                    behavior: "smooth"
                });
            }
        });
    });
});
