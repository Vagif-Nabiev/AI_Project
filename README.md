# Vacuum Cleaner AI Simulation

This project is a Python-based simulation designed to evaluate and compare the performance of different Artificial Intelligence agent architectures in a grid-based vacuum cleaner environment. 

## 🤖 Agents

The simulation compares two types of AI agents:

1. **Simple Reflex Agent**: 
   - Has no memory or internal state.
   - Only considers the current percept (whether the current square is dirty or clean).
   - If dirty, it sucks. If clean, it moves randomly in one of the four directions.
   
2. **Model-Based Agent**:
   - Maintains an internal model of the world (keeps track of unvisited squares).
   - If the current square is dirty, it sucks.
   - If clean, it computes the Manhattan distance to the closest unvisited square and moves towards it.
   - Stops efficiently when the entire grid has been visited, giving it a 100% success rate under the step limit.

## 📁 Project Structure

- `vacuum_project/environment.py`: Defines the `VacuumEnvironment` class, which handles grid initialization, randomized dirt distribution, and percept generation.
- `vacuum_project/agents.py`: Contains the logic for the `SimpleReflexAgent` and `ModelBasedAgent`.
- `vacuum_project/main.py`: The simulation driver. Runs trials, scores the agents, prints the results, and generates a comparative bar chart.

## 📊 Scoring System

Agents are evaluated over a set number of trials (default: 100) based on the following rules:
- **+10 points** for successfully cleaning a dirty square.
- **-1 point** for each movement (Up, Down, Left, Right).
- **-5 points** penalty for attempting to clean a square that is already clean.

## 🚀 Installation & Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Vagif-Nabiev/AI_Project.git
   cd AI_Project
   ```

2. **Install dependencies**:
   The project requires `numpy` and `matplotlib`. Install them via pip:
   ```bash
   pip install numpy matplotlib
   ```

3. **Run the simulation**:
   ```bash
   python vacuum_project/main.py
   ```

## 📈 Output

Running `main.py` will print the average scores, step counts, and success rates for both agents directly to the console. It will also generate a bar chart named `performance_comparison.png` in the root directory visually comparing the average scores.
