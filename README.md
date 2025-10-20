# Code Challenges Repository

Welcome to the Code Challenges repository! This repo contains programming problems to sharpen your skills in algorithms and problem solving.
Each challenge includes a clear problem description and a sample solution to help guide your learning.

> The Challenges are not sorted by category, tags or difficulty
> Read the `task.md` to see more information about the task
 
---

## Repository Structure

```bash
code-challenges/
├── challenges/
│   ├── challenge-001/
│   │   ├── task.md         # Problem description
│   │   └── solution.py     # Sample solution
│   └── ...
├── README.md               # You're here!
```

## Getting Started

You can fork this repository to keep it updated and track your progress, or simply clone it if you just want a local copy.

### Fork the Repository (Recommended)

1. Click the "Fork" button at the top right of the GitHub Repo
2. This creates your own copy of the Repo under your GitHub account
3. You can pull updates from the original repo whenever new challenges are added:

```bash
git remote add upstream https://github.com/JulesInCyber/CodeChallenges.git
git checkout main
git fetch upstream
git pull upstream main
git push origin main
```

## Solving a Challenge

1. Go to the `challenges/` folder
2. Pick any challenge (e.g. `challenge_001/`)
3. Read the problem in `task.md`
4. Try solving it yourself in a new file or refer to the code file for hints
5. Run and test your code locally

You're encouraged to try yourself before peeking ath the solution.
Treat the solution as a hint, not the first step

## Contributing

Want to add your own challenge? Follow the structure below:

1. Create a new folder under `challenges/`

```bash
challenges/challenge_xyz/
```

2. Inside the folder add:
   - `task.md` -- with the problem description, examples and any notes
   - `solution.xxx` -- a working solution in your language of choice
3. Recommended metadata in `task.md`
   - Difficulty (Easy/Medium/Hard)
   - Tags: `#math`, `#recursion`, etc.
   - example Input/Output
4. Commit your changes:

```bash
git add challenges/challenge-XYZ/
git commit -m "Add challenge XYZ: <title>"
```

5. Push and open a Pull Request to contribute back.

## Contact / Questions

Found a mistake? Have suggestions or want to collaborate?
Open an issue or start a discussion in the repo — feedback is welcome!
