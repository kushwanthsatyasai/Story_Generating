import React, { useState } from "react";
import "../styles/storyInput.css";

function StoryInput() {
  const [storyPrompt, setStoryPrompt] = useState("");
  const [generatedStory, setGeneratedStory] = useState("");

  const handleGenerate = async () => {
    try {
      const response = await fetch("http://localhost:8000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: storyPrompt }),
      });
      const data = await response.json();
      setGeneratedStory(data.story);
    } catch (error) {
      console.error("Error generating story:", error);
    }
  };

  return (
    <div className="story-input-container">
      <h1>Generative AI Story Creator</h1>
      <textarea
        placeholder="Enter your story idea..."
        value={storyPrompt}
        onChange={(e) => setStoryPrompt(e.target.value)}
      />
      <button onClick={handleGenerate}>Generate Story</button>
      {generatedStory && (
        <div>
          <h3>Generated Story:</h3>
          <p>{generatedStory}</p>
        </div>
      )}
    </div>
  );
}

export default StoryInput;
