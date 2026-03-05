const counterElement = document.getElementById('counter');
const apiUrl = "https://0cyv3fxnne.execute-api.us-east-1.amazonaws.com/update_visitor_count"; // KEEP YOUR REAL URL HERE

async function updateCounter() {
    try {
        // Check if user already visited in this session
        let count = sessionStorage.getItem('visitorCount');

        if (count) {
            // User already visited -> Show stored count (Don't call API)
            counterElement.innerHTML = count;
            console.log("Using cached visitor count:", count);
        } else {
            // New visit -> Call API
            const response = await fetch(apiUrl);
            const data = await response.json();
            
            // Save new count to session & display it
            sessionStorage.setItem('visitorCount', data);
            counterElement.innerHTML = data;
            console.log("New visitor count from API:", data);
        }

    } catch (error) {
        console.error("Error fetching count:", error);
        counterElement.innerHTML = "??";
    }
}

updateCounter();