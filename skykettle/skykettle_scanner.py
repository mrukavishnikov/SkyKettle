"""Scan for SkyKettle devices"""

# use only lower case names here
VALID_DEVICE_NAMES = ['rk-g201s']

DEVICE_PREFIX = 'E4:98:AF:'


def scan(backend, timeout=10):
    """Scan for skykettle devices.

    Note: this must be run as root!
    """
    result = []
    for (mac, name) in backend.scan_for_devices(timeout):
        if (name is not None and name.lower() in VALID_DEVICE_NAMES) or \
                mac is not None and mac.upper().startswith(DEVICE_PREFIX):
            result.append(mac.upper())
    return result
