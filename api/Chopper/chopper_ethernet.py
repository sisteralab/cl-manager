import logging
import time
from typing import Tuple, Union

from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusIOException

from api.Chopper.chopper_sync import Chopper


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ChopperEthernet(Chopper):
    def __init__(
        self,
        host: str = "169.254.54.24",
        port: int = 1111,
        baudrate: int = 9600,
        slave_address: int = 1,
    ):
        super().__init__(host, port, baudrate, slave_address)

    def init_client(self):
        self.port = int(self.port)
        if self.client is not None:
            if self.client.connected:
                self.client.close()
        self.client = ModbusTcpClient(
            method="rtu",
            host=self.host,
            port=self.port,
            baudrate=self.baudrate,
            stopbits=1,
            bytesize=8,
            parity="N",
        )

    def read_di23(self) -> Union[None, Tuple[bool, bool]]:
        """
        DI2 - left
        DI3 - right

        True - hot state
        False - cold state
        """
        response = self.client.read_holding_registers(
            int(0x0179), count=1, slave=self.slave_address
        )
        if isinstance(response, ModbusIOException):
            logger.error(f"{response}")
            return None
        num = next((result for result in response.registers), None)
        bits_str = "{0:08b}".format(num)
        return bits_str[-2] == "1", bits_str[-3] == "1"

    def align_to_hot(self):
        steps = 100
        step = 1
        di2, di3 = self.read_di23()
        if di2 is False and di3 is False:
            self.path0(90)
            time.sleep(1)

        while not (di2 is True and di3 is True):
            logger.info(f"[STEP {step}/{steps}] Start new step")
            if step >= steps:
                logger.info(f"Break align to hot, {step} steps exceeded")
                break
            if di2 is True and di3 is False:
                logger.info(
                    f"[STEP {step}/{steps}] Left D is Hot, Right D is Cold. \n Rotate 2 degree CW"
                )
                self.motor_direction(1)
                self.path0(10, align=False)
                time.sleep(0.1)
                di2, di3 = self.read_di23()
            elif di2 is False and di3 is True:
                logger.info(
                    f"[STEP {step}/{steps}] Left D is Cold, Right D is Hot. \n Rotate 2 degree CCW"
                )
                self.motor_direction(0)
                self.path0(10, align=False)
                time.sleep(0.1)
                di2, di3 = self.read_di23()
            step += 1
        self.path0(5, align=False)
        self.motor_direction(0)
        self.set_origin()
        self.go_to_pos(0)


if __name__ == "__main__":
    chopper = ChopperEthernet()
    chopper.connect()
    try:
        # while 1:
        #     print(f"[{datetime.now()}]{chopper.read_di23()}")
        #     time.sleep(0.1)
        #     chopper.path0()
        #     time.sleep(0.3)
        chopper.path0(45)
        time.sleep(5)
        chopper.align_to_hot()
        time.sleep(2)
        chopper.path0(125)
        time.sleep(2)
        chopper.align_to_hot()
    except KeyboardInterrupt:
        chopper.client.close()
