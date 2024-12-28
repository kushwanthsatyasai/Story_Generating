const API_URL = "http://localhost:8000";

export const generateVideo = async (prompt) => {
    const response = await fetch(`${API_URL}/generate-video`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt }),
    });
    return response.json();
};

export const generateStoryboard = async (prompt) => {
    const response = await fetch(`${API_URL}/generate-storyboard`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt }),
    });
    return response.json();
};

