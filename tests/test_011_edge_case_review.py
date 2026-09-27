import unittest

from denial_pattern_auditor.models import Record
from denial_pattern_auditor.scoring import score_record


class DepthCheck11(unittest.TestCase):
    def test_011_edge_case_review(self):
        record = Record(id="denial-011", exposure=89608, signal=0.834, urgency=6)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
