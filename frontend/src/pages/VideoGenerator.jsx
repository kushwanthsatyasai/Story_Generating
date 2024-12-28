import React, { useState } from "react";
import { generateVideo } from "../services/mediaService";

const VideoGenerator = () => {
    const [prompt, setPrompt] = useState("");
    const [videoPath, setVideoPath] = useState(null);

    const handleGenerate = async () => {
        const result = await generateVideo(prompt);
        setVideoPath(result.video_path);
    };

    return (
        <div>
            <h2>Video Generator</h2>
            <textarea value={prompt} onChange={(e) => setPrompt(e.target.value)} />
            <button onClick={handleGenerate}>Generate Video</button>
            {videoPath && (
                <video controls src={`http://localhost:3000/${videoPath}`} />
            )}
        </div>
    );
};

export default VideoGenerator;
