"""
Objects in 2D space have a Position & Velocity 
Object.state can be represented as np.array([px, py, vx, vy])
"""
import numpy as np
import matplotlib.pyplot as plt

"""Propagate an object in 2D space by multiplying its x,y by (dt * velocity(x/y))"""
def propagate(state: np.ndarray, dt:float) -> np.ndarray:
    px, py, vx, vy = state
    return np.array([px + vx * dt, py + vy * dt, vx, vy])

"""Simulate the Trajectory Path of both, Interceptor and Target, and plot the results using MatPlotLib"""
def simulate_trajectory_path(interceptor_state: np.ndarray, target_state: np.ndarray, dt: float, duration: float) -> tuple[np.ndarray,np.ndarray]:
    n_steps = int(duration / dt) + 1
    interceptor_trajectory = np.zeros((n_steps, 2))
    target_trajectory = np.zeros((n_steps,2))

    i_state = interceptor_state.copy()
    t_state = target_state.copy()
    for i in range(n_steps):
        interceptor_trajectory[i] = i_state[:2]
        target_trajectory[i] = t_state[:2]
        i_state = propagate(i_state, dt)
        t_state = propagate(t_state, dt)

    return interceptor_trajectory, target_trajectory

def plot_paths(interceptor_path: np.ndarray, target_path: np.ndarray) -> None:
    title = "Straight-Line Interception"
    fig, ax = plt.subplots(figsize=(6,6))
    ax.plot(interceptor_path[:,0], interceptor_path[:, 1], "b-", label="Interceptor")
    ax.plot(target_path[:,0], target_path[:, 1], "r-", label="Target")
    ax.scatter(*interceptor_path[0], c="blue", marker="o", s=80, zorder=5)
    ax.scatter(*target_path[0], c="red", marker="o", s=80, zorder=5)
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.set_title(title)
    ax.legend()
    ax.set_aspect("equal")
    ax.grid(True)
    plt.tight_layout()
    plt.savefig("interceptor_path_week1.png", dpi=150)
    plt.show()
if __name__ == "__main__":
    interceptor = np.array([0.0, 0.0, 10.0, 0.0]) #starting point(0,0) Ground, moving East at 10.0 m/s
    target = np.array([50.0, 0.0, 0.0, 8.0]) #starting point(50,0) Air, moving North at 8.0 m/s
    i_traj, t_traj = simulate_trajectory_path(interceptor, target, dt=0.1, duration=10.0)
    plot_paths(i_traj, t_traj)