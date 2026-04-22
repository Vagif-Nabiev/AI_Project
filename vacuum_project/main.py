import matplotlib.pyplot as plt
from environment import VacuumEnvironment
from agents import SimpleReflexAgent, ModelBasedAgent

def run_simulation(agent_class, trials=100, max_steps=100):
    total_score = 0
    total_steps = 0
    success_count = 0 # times it cleaned the whole grid
    
    for _ in range(trials):
        env = VacuumEnvironment(width=4, height=4, dirt_probability=0.3)
        
        # set up the agent. model-based one needs grid size for its map.
        if agent_class == ModelBasedAgent:
            agent = agent_class(width=4, height=4)
        else:
            agent = agent_class()
            
        agent_x, agent_y = 0, 0
        score = 0
        steps = 0
        
        for step in range(max_steps):
            if env.is_goal_reached():
                success_count += 1
                break
                
            percept = env.get_percept(agent_x, agent_y)
            action = agent.act(percept)
            
            if action == 'Suck':
                if env.is_dirty(agent_x, agent_y):
                    env.clean_square(agent_x, agent_y)
                    score += 10
                else:
                    score -= 5 # lose points for sucking a clean square
            elif action in ['Up', 'Down', 'Left', 'Right']:
                score -= 1 # movement penalty
                steps += 1
                
                # update location and make sure we don't go out of bounds
                if action == 'Up' and agent_y > 0: agent_y -= 1
                elif action == 'Down' and agent_y < env.height - 1: agent_y += 1
                elif action == 'Left' and agent_x > 0: agent_x -= 1
                elif action == 'Right' and agent_x < env.width - 1: agent_x += 1
            elif action == 'NoOp':
                break # agent thinks it's done
                
        total_score += score
        total_steps += steps

    return {
        "avg_score": total_score / trials,
        "avg_steps": total_steps / trials,
        "success_rate": (success_count / trials) * 100
    }

if __name__ == "__main__":
    print("Running simulations...")
    results_simple = run_simulation(SimpleReflexAgent)
    results_model = run_simulation(ModelBasedAgent)
    
    print("\n--- Simple Reflex Agent ---")
    print(f"Average Score: {results_simple['avg_score']}")
    print(f"Average Steps: {results_simple['avg_steps']}")
    print(f"Success Rate:  {results_simple['success_rate']}%")
    
    print("\n--- Model-Based Reflex Agent ---")
    print(f"Average Score: {results_model['avg_score']}")
    print(f"Average Steps: {results_model['avg_steps']}")
    print(f"Success Rate:  {results_model['success_rate']}%")

    # make a chart for the results
    labels = ['Simple Reflex', 'Model-Based']
    scores = [results_simple['avg_score'], results_model['avg_score']]
    
    plt.figure(figsize=(8, 5))
    plt.bar(labels, scores, color=['#e74c3c', '#2ecc71'])
    plt.title('Average Performance Score Comparison (100 Trials)')
    plt.ylabel('Average Score (+10 Clean, -1 Move, -5 Bad Suck)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig('performance_comparison.png')
    print("\nChart saved as 'performance_comparison.png'")