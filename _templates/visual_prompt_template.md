# VISUAL PROMPT TEMPLATE (NANO BANANA) - v2.0

## INSTRUCTIONS FOR LLM
1.  **Analyze Scene:** Check `character_profiles.json` for current character state (e.g., is Robotiko damaged?).
2.  **Video Logic:** Define if this shot needs "Standard", "Start/End Keyframes", or "Extension".
3.  **Consistency:** Always use the defined Style Suffix.

## STYLE SUFFIX (DO NOT MODIFY)
`hyper-realistic, 70s progressive rock album art style, Frank Frazetta meets Syd Mead, Kodachrome film stock, heavy film grain, cinematic lighting, volumetric fog, 8k resolution, masterpiece`

---
## GENERATED PROMPTS FOR EPISODE {EPISODE_NUMBER}

### SECTION: [Insert Section Name]

#### Scene {SCENE_NUMBER}
* **Timestamp:** [MM:SS]
* **Action:** [Detailed description of the moment]
* **Character(s):** [List characters present]
* **Video Tech Need:** [Standard / Start-End Keyframes / Extension]
* **Image Reference Path:** `_assets/cast/[filename]` (or N/A)
* **Text Prompt:**
    > [PROMPT HERE], [STYLE SUFFIX]