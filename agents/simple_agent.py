import logging
from datetime import datetime

# Configure logging (Observability layer)
logging.basicConfig(
    filename="logs/agent.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

class SimpleAgent:
    def __init__(self, goal):
        self.goal = goal

    def think(self):
        decision = f"Deciding how to achieve goal: {self.goal}"
        logging.info(f"THINK → {decision}")
        return decision

    def act(self):
        action = "Simulated action (no real tool yet)"
        logging.info(f"ACT → {action}")
        return action

    def run(self):
        logging.info("AGENT STARTED")
        self.think()
        self.act()
        logging.info("AGENT FINISHED")

if __name__ == "__main__":
    agent = SimpleAgent(goal="Understand enterprise AI observability")
    agent.run()