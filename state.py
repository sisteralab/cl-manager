class State:
    # Block variables
    BLOCK_ADDRESS = "169.254.190.83"
    BLOCK_PORT = 9876
    BLOCK_BIAS_DEV = "DEV4"
    BLOCK_CTRL_DEV = "DEV3"
    BLOCK_BIAS_VOLT = 0
    BLOCK_BIAS_VOLT_FROM = 0
    BLOCK_BIAS_VOLT_TO = 7
    BLOCK_BIAS_VOLT_POINTS = 300
    BLOCK_CTRL_CURR = 0
    BLOCK_CTRL_CURR_FROM = 0
    BLOCK_CTRL_CURR_TO = 30
    BLOCK_CTRL_POINTS = 300
    BLOCK_BIAS_SCAN_THREAD = False
    BLOCK_CTRL_SCAN_THREAD = False
    BLOCK_CTRL_STEP_DELAY = 0.01
    BLOCK_STREAM_THREAD = False
    BLOCK_BIAS_POWER_MEASURE_THREAD = False
    BLOCK_BIAS_STEP_DELAY = 0.1
    BLOCK_BIAS_SHORT_STATUS = "1"
    BLOCK_CTRL_SHORT_STATUS = "1"

    # Block constants
    BLOCK_BIAS_VOLT_MIN_VALUE = -30
    BLOCK_BIAS_VOLT_MAX_VALUE = 30
    BLOCK_BIAS_VOLT_POINTS_MAX = 10001
    BLOCK_CTRL_POINTS_MAX = 10001
    BLOCK_CTRL_CURR_MIN_VALUE = -100
    BLOCK_CTRL_CURR_MAX_VALUE = 100
    BLOCK_SHORT_STATUS_MAP = {
        "0": "Open",
        "1": "Short",
    }

    # VNA variables
    VNA_ADDRESS = "169.254.106.189"
    VNA_SPARAM = "S21"
    VNA_CHANNEL_FORMAT = "COMP"
    VNA_POWER = -30
    VNA_POINTS = 300
    VNA_FREQ_FROM = 2
    VNA_FREQ_TO = 12

    # VNA constants
    VNA_POWER_MIN = -60
    VNA_POWER_MAX = 0
    VNA_POINTS_MAX = 2000
    VNA_TEST_MAP = dict(
        (
            ("0", "Ok"),
            ("1", "Error"),
        )
    )

    # NRX variables
    NRX_APER_TIME = 0.05
    NRX_FILTER_TIME = 0.01
    NRX_IP = "169.254.2.20"
    NRX_STREAM_THREAD = False
    NRX_STREAM_PLOT_GRAPH = False
    NRX_STREAM_GRAPH_POINTS = 150

    # NRX constants
    NRX_TEST_MAP = dict(
        (
            ("0", "Ok"),
            ("1", "Error"),
        )
    )

    # Bias reflection variables
    BIAS_REFL_SCAN_THREAD = False
    BIAS_REFL_VOLT_FROM = 0
    BIAS_REFL_VOLT_TO = 0
    BIAS_REFL_VOLT_POINTS = 300
    BIAS_REFL_DELAY = 0.8

    # Agilent signal generator
    AGILENT_SIGNAL_GENERATOR_IP = "169.254.190.9"
    AGILENT_SIGNAL_GENERATOR_GPIB = 19

    AGILENT_SIGNAL_GENERATOR_FREQUENCY = 14  # GHz
    AGILENT_SIGNAL_GENERATOR_AMPLITUDE = -20  # dBm

    # Prologix
    PROLOGIX_IP = "169.254.156.103"

    # Arduino step motor
    STEP_MOTOR_ADDRESS = "169.254.0.52"

    GRID_BLOCK_BIAS_POWER_MEASURE_THREAD = False
    STEP_MOTOR_ANGLE = 90
    STEP_MOTOR_ANGLE_FROM = 0
    STEP_MOTOR_ANGLE_TO = 0
    STEP_MOTOR_ANGLE_STEP = 10
    STEP_MOTOR_SPEED = 180  # degree per second


state = State()
