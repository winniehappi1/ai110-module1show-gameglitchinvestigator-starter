# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? very simple to understand
- List at least two concrete bugs you noticed at the start  1 the number off attemps within each difficulties, and it does not properly say when to go higher or lower 2 it asks you to guess a number between 1 to 100 but ask you to guess -15
  (for example: "the secret number kept changing" or "the hints were backwards").

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). swapped hint messages
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). N/A

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? when i checked the output
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How? Yes buy giving suggestions and creating new functions

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app. Streamlit reruns the entire script from top to bottom every time 

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? Imagine you're building a web app with Streamlit, and every time your friend clicks a button or types something, the entire code restarts from the top; like hitting refresh on a webpage, but automatically triggered by their actions. That's a "rerun": the script runs again completely, which is great for reacting to inputs but means any regular variables get reset each time unless you save them somewhere special.


- What change did you make that finally gave the game a stable secret number?
I added a check using Streamlit's session state to store the secret number only once per game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? One strategy I want to reuse in future labs or projects is carefully checking for bugs and asking AI to explain why the error happened. This helps me understand the problem better and debug the code more effectively instead of just fixing it without learning the cause.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?  AI on a coding task is provide clearer and more detailed prompts from the beginning. When the instructions are specific , the AI can generate more accurate suggestions.
- In one or two sentences, describe how this project changed the way you think about AI generated code. This project showed me that AI-generated code can be helpful for debugging and suggesting solutions, but it still needs to be checked carefully. I learned that it is important to understand the code and verify the AI’s suggestions instead of relying on them completely.
