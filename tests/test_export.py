import os
import unittest
import sys

current_dir = os.path.dirname(__file__)
src_dir = os.path.join(current_dir, "..")

src_dir = os.path.normpath(src_dir)
sys.path.append(os.path.normpath(src_dir))

from src.modules.utils.export import export_info

class TestExportInfo(unittest.TestCase):
    def test_export_info(self):
        file_path = os.path.normpath(
            os.path.join(current_dir, "data", "mock-output.txt")
        )
        
        data = {
            "ip": "192.168.1.1",
            "ipv": "IPv4",
            "isp": "ExampleISP",
            "continentCode": "NA",
            "continentName": "North America",
            "country": "USA",
            "phoneCode": "+1",
            "city": "New York",
            "countryCode": "US",
            "latitude": 40.7128,
            "longitude": -74.0060,
            "locationLink": "http://example.com",
            "currencyName": "USD",
            "currencySymbol": "$",
            "localTime": "2025-03-10 14:00:00",
            "countryCapital": "Washington, D.C.",
        }

        export_info(file_path, data) 
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.readlines()

        content = [line.strip() for line in content]    

        self.assertTrue("ip: 192.168.1.1" in content)
        self.assertTrue("isp: ExampleISP" in content)
        self.assertTrue("continentCode: NA" in content)
        self.assertTrue("city: New York" in content)
        self.assertTrue("latitude: 40.7128" in content)
        self.assertTrue("longitude: -74.0060" in content)
        self.assertTrue("currencyName: USD" in content)
        self.assertTrue("countryCapital: Washington, D.C." in content)

    def tearDown(self):
        file_path = os.path.normpath(os.path.join(current_dir, "data", "mock-output.txt"))
        if os.path.exists(file_path):
            os.remove(file_path)

if __name__ == "__main__":
    unittest.main()