// =============================
// Docker Cleanup Dashboard
// script.js
// =============================

// Dashboard Search Function

document.addEventListener("DOMContentLoaded", function () {

    const searchInput =
        document.getElementById("searchInput");

    if (searchInput) {

        searchInput.addEventListener("keyup", function () {

            let filter =
                searchInput.value.toLowerCase();

            let rows =
                document.querySelectorAll(
                    "#imageTable tbody tr"
                );

            rows.forEach(row => {

                let text =
                    row.textContent.toLowerCase();

                row.style.display =
                    text.includes(filter)
                        ? ""
                        : "none";

            });

        });

    }

});


// =============================
// History Search
// =============================

document.addEventListener("DOMContentLoaded", function () {

    const historySearch =
        document.getElementById("historySearch");

    if (historySearch) {

        historySearch.addEventListener("keyup", function () {

            let filter =
                historySearch.value.toLowerCase();

            let rows =
                document.querySelectorAll(
                    "#historyTable tbody tr"
                );

            rows.forEach(row => {

                let text =
                    row.textContent.toLowerCase();

                row.style.display =
                    text.includes(filter)
                        ? ""
                        : "none";

            });

        });

    }

});


// =============================
// Confirm Cleanup
// =============================

document.addEventListener("DOMContentLoaded", function () {

    const cleanupBtn =
        document.querySelector(".cleanup-btn");

    if (cleanupBtn) {

        cleanupBtn.addEventListener("click", function (e) {

            const confirmDelete =
                confirm(
                    "Are you sure you want to remove all unused Docker images?"
                );

            if (!confirmDelete) {
                e.preventDefault();
            }

        });

    }

});


// =============================
// Delete Image Confirmation
// =============================

document.addEventListener("DOMContentLoaded", function () {

    const deleteButtons =
        document.querySelectorAll(".delete-btn");

    deleteButtons.forEach(button => {

        button.addEventListener("click", function (e) {

            const confirmDelete =
                confirm(
                    "Delete this Docker image?"
                );

            if (!confirmDelete) {
                e.preventDefault();
            }

        });

    });

});


// =============================
// Live Clock
// =============================

document.addEventListener("DOMContentLoaded", function () {

    const clock =
        document.getElementById("liveClock");

    if (!clock) return;

    function updateClock() {

        const now = new Date();

        clock.innerHTML =
            now.toLocaleString();

    }

    updateClock();

    setInterval(updateClock, 1000);

});


// =============================
// Auto Fade Alerts
// =============================

document.addEventListener("DOMContentLoaded", function () {

    const alerts =
        document.querySelectorAll(".alert");

    alerts.forEach(alert => {

        setTimeout(() => {

            alert.style.transition =
                "opacity 0.8s";

            alert.style.opacity = "0";

            setTimeout(() => {

                alert.remove();

            }, 800);

        }, 3000);

    });

});


// =============================
// Table Row Hover Animation
// =============================

document.addEventListener("DOMContentLoaded", function () {

    const rows =
        document.querySelectorAll("tbody tr");

    rows.forEach(row => {

        row.addEventListener("mouseenter", () => {

            row.style.transition =
                "all 0.2s ease";

            row.style.transform =
                "scale(1.01)";

        });

        row.addEventListener("mouseleave", () => {

            row.style.transform =
                "scale(1)";

        });

    });

});


// =============================
// Welcome Message
// =============================

document.addEventListener("DOMContentLoaded", function () {

    console.log(
        "Docker Cleanup Dashboard Loaded Successfully"
    );

});