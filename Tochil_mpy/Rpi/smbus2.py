# *  ----------------------------------------------:
# * import block# :
#  ----------------------------------------------:
from ctypes import c_uint32, c_uint8, c_uint16, c_char, POINTER, Structure, Array, Union, create_string_buffer, string_at
from typing import cast, List


#  ----------------------------------------------:
# * Vars block :
#  ----------------------------------------------:
I2CBUS =1
LAST_ADR =0
LAST_CMD =0
LAST_DATA =0
RETURN_DATA = [i for i in range(11)[::-1]]
# print (RETURN_DATA)


#  ----------------------------------------------:
# * class SMBus: 
class SMBus(object):
# ** def __init__(self, bus=None, force=False, port=I2CBUS): : 
    def __init__(self, bus=None, force=False, port=I2CBUS):
        """
        Initialize and (optionally) open an i2c bus connection.
        :param bus: i2c bus number (e.g. 0 or 1)
            or an absolute file path (e.g. `/dev/i2c-42`).
            If not given, a subsequent  call to ``open()`` is required.
        :type bus: int or str
        :param force: force using the slave address even when driver is
            already using it.
        :type force: boolean
        """
        self.i2c_read_byte =10
        self.i2c_write_byte = []

     
# ** def __enter__(self): : 
    def __enter__(self):
        """Enter handler."""
        return self
# ** def __exit__(self, exc_type, exc_val, exc_tb): : 
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit handler."""
        self.close()
# ** def open(self, bus): : 
    def open(self, bus):
        """
        Open a given i2c bus.
        :param bus: i2c bus number (e.g. 0 or 1)
            or an absolute file path (e.g. '/dev/i2c-42').
        :type bus: int or str
        :raise TypeError: if type(bus) is not in (int, str)
        """
        pass

     
# ** def close(self): : 
    def close(self):
        """
        Close the i2c connection.
        """
        pass

     
# ** def _get_pec(self): : 
    def _get_pec(self):
        return self._pec
# ** def enable_pec(self, enable=True): : 
    def enable_pec(self, enable=True):
        """
        Enable/Disable PEC (Packet Error Checking) - SMBus 1.1 and later
        :param enable:
        :type enable: Boolean
        """
        pass

     
# ** pec = property(_get_pec, enable_pec)  # Drop-in replacement for smbus member "pec" : 
    pec = property(_get_pec, enable_pec)  # Drop-in replacement for smbus member "pec"
    """Get and set SMBus PEC. 0 = disabled (default), 1 = enabled."""
# ** def _set_address(self, address, force=None): : 
    def _set_address(self, address, force=None):
        """
        Set i2c slave address to use for subsequent calls.
        :param address:
        :type address: int
        :param force:
        :type force: Boolean
        """
        pass

     
# ** def _get_funcs(self): : 
    def _get_funcs(self):
        """
        Returns a 32-bit value stating supported I2C functions.
        :rtype: int
        """
        pass

     
# ** def write_quick(self, i2c_addr, force=None): : 
    def write_quick(self, i2c_addr, force=None):
        """
        Perform quick transaction. Throws IOError if unsuccessful.
        :param i2c_addr: i2c address
        :type i2c_addr: int
        :param force:
        :type force: Boolean
        """
        pass

     
# ** def read_byte(self, i2c_addr, force=None): : 
    def read_byte(self, i2c_addr, force=None):
        """
        Read a single byte from a device.
        :rtype: int
        :param i2c_addr: i2c address
        :type i2c_addr: int
        :param force:
        :type force: Boolean
        :return: Read byte value
        """
        self.i2c_read_byte += 1
        return self.i2c_read_byte 

     
# ** def write_byte(self, i2c_addr, value, force=None): : 
    def write_byte(self, i2c_addr, value, force=None):
        """
        Write a single byte to a device.
        :param i2c_addr: i2c address
        :type i2c_addr: int
        :param value: value to write
        :type value: int
        :param force:
        :type force: boolean
        """
        self.i2c_write_byte.append( value)
        return self.i2c_write_byte 

     
# ** def read_byte_data(self, i2c_addr, register, force=None): : 
    def read_byte_data(self, i2c_addr, register, force=None):
        """
        Read a single byte from a designated register.
        :param i2c_addr: i2c address
        :type i2c_addr: int
        :param register: Register to read
        :type register: int
        :param force:
        :type force: Boolean
        :return: Read byte value
        :rtype: int
        """
        return  RETURN_DATA[0]

# ** def write_byte_data(self, i2c_addr, register, value, force=None): : 
    def write_byte_data(self, i2c_addr, register, value, force=None):
        """
        Write a byte to a given register.
        :param i2c_addr: i2c address
        :type i2c_addr: int
        :param register: Register to write to
        :type register: int
        :param value: Byte value to transmit
        :type value: int
        :param force:
        :type force: Boolean
        :rtype: None
        """
        pass

     
# ** def read_word_data(self, i2c_addr, register, force=None): : 
    def read_word_data(self, i2c_addr, register, force=None):
        """
        Read a single word (2 bytes) from a given register.
        :param i2c_addr: i2c address
        :type i2c_addr: int
        :param register: Register to read
        :type register: int
        :param force:
        :type force: Boolean
        :return: 2-byte word
        :rtype: int
        """
        pass

     
# ** def write_word_data(self, i2c_addr, register, value, force=None): : 
    def write_word_data(self, i2c_addr, register, value, force=None):
        """
        Write a single word (2 bytes) to a given register.
        :param i2c_addr: i2c address
        :type i2c_addr: int
        :param register: Register to write to
        :type register: int
        :param value: Word value to transmit
        :type value: int
        :param force:
        :type force: Boolean
        :rtype: None
        """
        pass

     
# ** def process_call(self, i2c_addr, register, value, force=None): : 
    def process_call(self, i2c_addr, register, value, force=None):
        """
        Executes a SMBus Process Call, sending a 16-bit value and receiving a 16-bit response
        :param i2c_addr: i2c address
        :type i2c_addr: int
        :param register: Register to read/write to
        :type register: int
        :param value: Word value to transmit
        :type value: int
        :param force:
        :type force: Boolean
        :rtype: int
        """
        pass

     
# ** def read_block_data(self, i2c_addr, register, force=None): : 
    def read_block_data(self, i2c_addr, register, force=None):
        """
        Read a block of up to 32-bytes from a given register.
        :param i2c_addr: i2c address
        :type i2c_addr: int
        :param register: Start register
        :type register: int
        :param force:
        :type force: Boolean
        :return: List of bytes
        :rtype: list
        """
        return register

     
# ** def write_block_data(self, i2c_addr, register, data, force=None): : 
    def write_block_data(self, i2c_addr, register, data, force=None):
        """
        Write a block of byte data to a given register.
        :param i2c_addr: i2c address
        :type i2c_addr: int
        :param register: Start register
        :type register: int
        :param data: List of bytes
        :type data: list
        :param force:
        :type force: Boolean
        :rtype: None
        """
        pass

     
# ** def block_process_call(self, i2c_addr, register, data, force=None): : 
    def block_process_call(self, i2c_addr, register, data, force=None):
        """
        Executes a SMBus Block Process Call, sending a variable-size data
        block and receiving another variable-size response
        :param i2c_addr: i2c address
        :type i2c_addr: int
        :param register: Register to read/write to
        :type register: int
        :param data: List of bytes
        :type data: list
        :param force:
        :type force: Boolean
        :return: List of bytes
        :rtype: list
        """
        pass

     
# ** def read_i2c_block_data(self, i2c_addr, register, length, force=None): : 
    def read_i2c_block_data(self, i2c_addr, register, length, force=None):
        """
        Read a block of byte data from a given register.
        :param i2c_addr: i2c address
        :type i2c_addr: int
        :param register: Start register
        :type register: int
        :param length: Desired block length
        :type length: int
        :param force:
        :type force: Boolean
        :return: List of bytes
        :rtype: list
        """
        pass

     
# ** def write_i2c_block_data(self, i2c_addr, register, data, force=None): : 
    def write_i2c_block_data(self, i2c_addr, register, data, force=None):
        """
        Write a block of byte data to a given register.
        :param i2c_addr: i2c address
        :type i2c_addr: int
        :param register: Start register
        :type register: int
        :param data: List of bytes
        :type data: list
        :param force:
        :type force: Boolean
        :rtype: None
        """
        LAST_ADR = i2c_addr
        LAST_DATA = data
        print("adr = {}; data =".format(i2c_addr), data )


     
# ** def i2c_rdwr(self, *i2c_msgs): : 
    def i2c_rdwr(self, *i2c_msgs):
        """
        Combine a series of i2c read and write operations in a single
        transaction (with repeated start bits but no stop bits in between).
        This method takes i2c_msg instances as input, which must be created
        first with :py:meth:`i2c_msg.read` or :py:meth:`i2c_msg.write`.
        :param i2c_msgs: One or more i2c_msg class instances.
        :type i2c_msgs: i2c_msg
        :rtype: None
        """
        # print (i2c_msgs[1])
        # print (i2c_msgs[0].len)
        # print (i2c_msgs[0].len)
        # i2c_msgs[0].buf = [LAST_DATA[0]]
        # i2c_msgs[0].buf = POINTER(c_char(10))
        # i2c_msgs[0].buf = c_char(b'1') 
        last_adr = i2c_msgs[0].addr
        last_data = list(i2c_msgs[0])
        # print(last_data)
        print("adr = {}; data =".format(last_adr), last_data )
        i2c_msgs[1].buf[0] = (10).to_bytes(1, "big")

     
#  ----------------------------------------------:
# * class i2c_msg(Structure): : 
#  ----------------------------------------------:
class i2c_msg(Structure):
    """
    As defined in ``i2c.h``.
    """
    _fields_ = [
        ('addr', c_uint16),
        ('flags', c_uint16),
        ('len', c_uint16),
        ('buf', POINTER(c_char))]

    def __iter__(self):
        """ Iterator / Generator
        :return: iterates over :py:attr:`buf`
        :rtype: :py:class:`generator` which returns int values
        """
        idx = 0
        while idx < self.len:
            yield ord(self.buf[idx])
            idx += 1

    def __len__(self):
        return self.len

    def __bytes__(self):
        return string_at(self.buf, self.len)

    def __repr__(self):
        return 'i2c_msg(%d,%d,%r)' % (self.addr, self.flags, self.__bytes__())

    def __str__(self):
        s = self.__bytes__()
        # Throw away non-decodable bytes
        s = s.decode(errors="ignore")
        return s

    @staticmethod
    def read(address, length):
        """
        Prepares an i2c read transaction.
        :param address: Slave address.
        :type: address: int
        :param length: Number of bytes to read.
        :type: length: int
        :return: New :py:class:`i2c_msg` instance for read operation.
        :rtype: :py:class:`i2c_msg`
        """
        arr = create_string_buffer(length)
        return i2c_msg(
            addr=address, flags=1, len=length,
            buf=arr)

    @staticmethod
    def write(address, buf):
        """
        Prepares an i2c write transaction.
        :param address: Slave address.
        :type address: int
        :param buf: Bytes to write. Either list of values or str.
        :type buf: list
        :return: New :py:class:`i2c_msg` instance for write operation.
        :rtype: :py:class:`i2c_msg`
        """
        buf = bytes(buf)
        arr = create_string_buffer(buf, len(buf))
        return i2c_msg(
            addr=address, flags=0, len=len(arr),
            buf=arr)


# *  ----------------------------------------------:
