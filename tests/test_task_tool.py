import json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from check_revisions import analyze
class TaskToolTests(unittest.TestCase):
 def sample(self):return json.loads((ROOT/'examples/tool-input.json').read_text(encoding='utf-8'))
 def test_chinese_original_positions(self):self.assertEqual(analyze(self.sample())['text'],'小李告诉小王小李提交了申请。')
 def test_stale_original_stops(self):
  p=self.sample();p['changes'][0]['old']='她'
  with self.assertRaises(ValueError):analyze(p)
 def test_overlapping_edits_stop(self):
  p=self.sample();p['changes']*=2
  with self.assertRaises(ValueError):analyze(p)
 def test_out_of_bounds_stops(self):
  p=self.sample();p['changes'][0]['end']=100
  with self.assertRaises(ValueError):analyze(p)
 def test_missing_reason_stops(self):
  p=self.sample();p['changes'][0]['reason']=' '
  with self.assertRaises(ValueError):analyze(p)

if __name__=='__main__':unittest.main()
