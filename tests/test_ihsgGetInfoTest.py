from click.testing import CliRunner

import unittest
from ihsginfocli import cli

class Test_IhsgGetInfoTest(unittest.TestCase):
  def test_increment(self):
    self.assertEqual(4, 4)
  def test_get_stock_info_lower(self):
    runner = CliRunner()
    result = runner.invoke(cli, ['get', 'info', 'bbca'])
    self.assertEqual(result.exit_code, 0)
  def test_get_stock_info_upper(self):
    runner = CliRunner()
    result = runner.invoke(cli, ['get', 'info', 'BBCA'])
    self.assertEqual(result.exit_code, 0)

if __name__ == '__main__':
  unittest.main()

