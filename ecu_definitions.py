from enum import Enum 

ECU_IDENTIFICATION_TABLE = [
	{
		'offset': 0x82014, # RSW zone
		'expected': [b'\x36\x36\x32\x31'], #6621
		'ecu': {
			'name': 'SIMK43 8mbit',
			'eeprom_size_bytes': 1048576, # (1024 KiB)
			'bin_offset': 0,
			'calibration_section_address': 0x90000,
			'calibration_size_bytes': 0x10000, # 65536 bytes (64 KiB)
			'program_section_address': 0xA0000,
			'program_section_size': 0x60000
		}
	},
	{
		'offset': 0x90040,
		'expected': [b'\x63\x61\x36\x36'], #CA66
		'ecu': {
			'name': 'SIMK43 2.0 4mbit',
			'eeprom_size_bytes': 524288, # (512 KiB)
			'bin_offset': -0x80000,
			'calibration_section_address': 0x90000,
			'calibration_size_bytes': 0x10000, # 65536 bytes (64 KiB)
			'program_section_address': 0xA0000,
			'program_section_size': 0x60000
		},
	},
	{
		'offset': 0x88040,
		'expected': [b'\x63\x61\x36\x35\x34\x30\x31'], #CA65401 (5WY17)
		'ecu': {
			'name': 'SIMK43 V6 4mbit (5WY17)',
			'eeprom_size_bytes': 524288, # (512 KiB)
			'bin_offset': -0x80000,
			'calibration_section_address': 0x88000,
			'calibration_size_bytes': 0x8000, # 32,768 bytes (32 KiB)
			'program_section_address': 0x90000,
			'program_section_size': 0x70000
		}
	},
		{
		'offset': 0x88040,
		'expected': [b'\x63\x61\x36\x35\x34', b'\x63\x61\x36\x35\x35'], #CA654, CA655 (5WY18+)
		'ecu': {
			'name': 'SIMK43 V6 4mbit (5WY18+)',
			'eeprom_size_bytes': 524288, # (512 KiB)
			'bin_offset': -0x80000,
			'calibration_section_address': 0x88000,
			#'calibration_size_bytes': 0x8000, # 32,768 bytes (32 KiB)
			'calibration_size_bytes': 0x6EFF, # experiment
			'program_section_address': 0x90000,
			'program_section_size': 0x70000
		}
	},
	{
		'offset': 0x48040,
		'expected': [b'\x63\x61\x36\x36\x30', b'\x63\x61\x36\x35\x32', b'\x63\x61\x36\x35\x30'], #CA660, CA652, CA650
		'ecu': {
			'name': 'SIMK41 / V6 2mbit',
			'eeprom_size_bytes': 262144, # (256 KiB)
			'bin_offset': -0x40000,
			'calibration_section_address': 0x48000,
			'calibration_size_bytes': 0x8000, # 32,768 bytes (32 KiB)
			'program_section_address': 0x50000, 
			'program_section_size': 0x30000
		}
	},
	{
		'offset': 0x88040,
		'expected': [b'\x63\x61\x36\x36\x31'], #CA661 (Sonata)
		'ecu': {
			'name': 'SIMK43 2.0 4mbit (Sonata)',
			'eeprom_size_bytes': 524288, # (512 KiB)
			'bin_offset': -0x80000,
			'calibration_section_address': 0x88000,
			'calibration_size_bytes': 0x8000, # 32,768 bytes (32 KiB)
			'program_section_address': 0x90000,
			'program_section_size': 0x70000
		}
	},	
]

BAUDRATES = {
	0x01: 10400,
	0x02: 20000,
	0x03: 40000,
	0x04: 60000,
	0x05: 120000
}

class Routine (Enum):
	ERASE_PROGRAM = 0x00
	ERASE_CALIBRATION = 0x01
	VERIFY_BLOCKS = 0x02

	QUERY_IMMO_INFO = 0x12
	BEFORE_LIMP_HOME = 0x16 # what does this actually do?
	ACTIVATE_LIMP_HOME = 0x18 # user 4 pin code password as parameters
	BEFORE_LIMP_HOME_TEACHING = 0x13
	LIMP_HOME_INPUT_NEW_PASSWORD = 0x17
	LIMP_HOME_CONFIRM_NEW_PASSWORD = 0x19

	BEFORE_IMMO_RESET = 0x15 # what does this actually do?
	IMMO_INPUT_PASSWORD = 0x1A # 6 digit pin code as parameter
	IMMO_RESET_CONFIRM = 0x20

	BEFORE_IMMO_KEY_TEACHING = 0x14 # what does this actually do?
	# these enums below are not actually used, just serve as documentation
	IMMO_TEACH_KEY_1 = 0x1B
	IMMO_TEACH_KEY_2 = 0x1C
	IMMO_TEACH_KEY_3 = 0x1D
	IMMO_TEACH_KEY_4 = 0x1E

	BEFORE_SMARTRA_NEUTRALIZE = 0x25
	SMARTRA_NEUTRALIZE = 0x26

class IOIdentifier (Enum):
	CHECK_ENGINE_LIGHT = 0x10
	COOLING_FAN_RELAY_HIGH = 0x1A
	COOLING_FAN_RELAY_LOW = 0x1B
	IDLE_SPEED_ACTUATOR = 0x23
	CVVT_VALVE = 0x24
	ADAPTIVE_VALUES = 0x50
