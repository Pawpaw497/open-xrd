class BaselineMethod:
    SNIP = "snip"
    ALS = "als"
    POLY = "poly"
    ROLLING_BALL = "rolling_ball"
    MOD_POLY = "modpoly"
    ANCHOR = "anchor"


class BaselineParams:
    method: str = BaselineMethod.SNIP
