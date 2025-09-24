# Line Follower Drone (Simulation)

This project simulates a **line-following drone**:
1. Uses webcam/IP cam to detect a line on the floor.
2. Calculates the line centroid.
3. Simulates drone commands (`LEFT`, `RIGHT`, `FORWARD`, `HOLD`) based on position.
4. Sends commands to a REST API server for logging.

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
