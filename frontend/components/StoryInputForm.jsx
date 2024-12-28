// frontend/src/components/StoryInputForm.jsx
import React, { useState } from 'react';
import { generateStory } from '../services/api';

const StoryInputForm = () => {
    const [input, setInput] = useState({ title: '', description: '', genre: '', character_details: {}, desired_output_format: '' });

    const handleSubmit = async (e) => {
        e.preventDefault();
        const result = await generateStory(input);
        console.log(result); // Display generated output
    };

    return (
        <form onSubmit={handleSubmit}>
            {/* Inputs for title, description, etc. */}
            <button type="submit">Generate Story</button>
        </form>
    );
};

export default StoryInputForm;
