import os

from settings import GridPlotTypes, WAVESHARE_ETHERNET
from store.gridAngleModel import GridAngleModel
from store.yigFreqModel import YigFrequencyModel


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
    BLOCK_DEMAG_THREAD = False
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
    VNA_PORT = 5025
    VNA_SPARAM = "S11"
    VNA_SPARAMS = ["S11", "S22", "S12", "S21"]
    VNA_CHANNEL_FORMAT = "COMP"
    VNA_POWER = -30
    VNA_POINTS = 300
    VNA_FREQ_START = 2
    VNA_FREQ_STOP = 12
    VNA_SAMPLES_COUNT = 1

    VNA_STORE_DATA = True

    # VNA constants
    VNA_POWER_MIN = -100
    VNA_POWER_MAX = 0
    VNA_POINTS_MAX = 5000
    VNA_TEST_MAP = dict(
        (
            ("0", "Ok"),
            ("1", "Error"),
        )
    )

    # NRX variables
    NRX_APER_TIME = 50  # ms
    NRX_FILTER_TIME = 0.01
    NRX_IP = "169.254.2.20"
    NRX_STREAM_THREAD = False
    NRX_STREAM_PLOT_GRAPH = False
    NRX_STREAM_GRAPH_TIME = 60
    NRX_STREAM_STORE_DATA = False
    NRX_UNITS = {"DBM": "dBm", "W": "W", "DBUV": "dBμV"}
    NRX_UNITS_REVERSE = {v: k for k, v in NRX_UNITS.items()}
    NRX_UNIT = "DBM"

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
    AGILENT_SIGNAL_GENERATOR_OUTPUT = False

    # Prologix
    PROLOGIX_IP = "169.254.156.103"

    # Arduino step motor
    GRID_ADDRESS = "169.254.0.52"

    GRID_BLOCK_BIAS_POWER_MEASURE_THREAD = False
    GRID_CURRENT_ANGLE_THREAD = False
    GRID_ANGLE = GridAngleModel()
    GRID_ANGLE_ROTATE = 0
    GRID_ANGLE_START = 0
    GRID_ANGLE_STOP = 0
    GRID_ANGLE_STEP = 10
    GRID_SPEED = 180  # degree per second
    GRID_PLOT_TYPE = GridPlotTypes.IV_CURVE

    # Spectrum
    SPECTRUM_STEP_DELAY = 0.5
    SPECTRUM_GPIB_ADDRESS = 20

    # WaveShare
    WAVESHARE_HOST = "169.254.54.24"
    WAVESHARE_PORT = 1111

    # Chopper
    CHOPPER_HOST = WAVESHARE_HOST
    CHOPPER_PORT = WAVESHARE_PORT
    CHOPPER_ADAPTER = WAVESHARE_ETHERNET
    CHOPPER_DEFAULT_SERIAL_PORT = "COM16"
    CHOPPER_FREQ = 1
    CHOPPER_SWITCH = True
    CHOPPER_MONITOR = False

    # National Instruments
    NI_PREFIX = "http://"
    NI_IP = "169.254.0.86"

    NI_FREQ_TO = 13
    NI_FREQ_FROM = 3
    NI_FREQ_POINTS = 300
    NI_STABILITY_MEAS = False
    DIGITAL_YIG_FREQ_1 = YigFrequencyModel()
    DIGITAL_YIG_FREQ_2 = YigFrequencyModel()
    DIGITAL_YIG_MAP = {
        "yig_1": DIGITAL_YIG_FREQ_1,
        "yig_2": DIGITAL_YIG_FREQ_2,
    }

    NRX_POINTS = 20

    CALIBRATION_CURR_2_FREQ = [3.49015508e10, 1.14176903e08]
    CALIBRATION_FREQ_2_CURR = [2.86513427e-11, -3.26694024e-03]
    CALIBRATION_FILE = os.path.join(os.getcwd(), "calibration.csv")
    CALIBRATION_STEP_DELAY = 0.1

    CALIBRATION_DIGITAL_POINT_2_FREQ = [2478826.8559771227, 2937630021.5301304]
    CALIBRATION_DIGITAL_FREQ_2_POINT = [4.03405867562004e-07, -1185.002515827086]


state = State()
