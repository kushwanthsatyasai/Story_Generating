import React, { useState } from "react";
import { generateStoryboard } from "../services/mediaService";

const StoryboardGenerator = () => {
    const [prompt, setPrompt] = useState("");
    const [storyboardPath, setStoryboardPath] = useState(null);

    const handleGenerate = async () => {
        const result = await generateStoryboard(prompt);
        setStoryboardPath(result.storyboard_path);
    };

    return (
        <div>
            <h2>Storyboard Generator</h2>
            <textarea value={prompt} onChange={(e) => setPrompt(e.target.value)} />
            <button onClick={handleGenerate}>Generate Storyboard</button>
            {storyboardPath && <img src={`http://localhost:3000/${storyboardPath}`} alt="Storyboard" />}
        </div>
    );
};

export default StoryboardGenerator;
