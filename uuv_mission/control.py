"""PD feedback controller for the UUV depth loop."""


class PDController:
    """Discrete-time proportional-derivative controller.

    u[t] = kp * e[t] + kd * (e[t] - e[t-1]),  with e[t] = r[t] - y[t]
    and e[-1] = 0.
    """

    def __init__(self, kp: float = 0.15, kd: float = 0.6) -> None:
        self.kp = kp
        self.kd = kd
        self.prev_error = 0.0  # e[-1] = 0

    def reset(self) -> None:
        """Clear memory so the controller can be reused for a new simulation."""
        self.prev_error = 0.0

    def compute(self, reference: float, output: float) -> float:
        """Return the control action u[t] for one time step."""
        error = reference - output
        action = self.kp * error + self.kd * (error - self.prev_error)
        self.prev_error = error
        return action