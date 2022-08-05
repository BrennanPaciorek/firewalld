import sys
import unittest
import firewall
from firewall.client import FirewallClient, \
                            FirewallClientZoneSettings, \
                            FirewallClientServiceSettings, \
                            FirewallClientIcmpTypeSettings
from firewall.core.base import DEFAULT_ZONE_TARGET
from firewall.core.fw import Firewall

class TestFirewallDReset(unittest.TestCase):
    pass