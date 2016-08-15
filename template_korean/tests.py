#-*- coding: utf-8 -*-
from django.test import TestCase

# Create your tests here.
class TemplateKoreanTestCase(TestCase):
	def setUp(self):
		pass
	def test_test(self):
		self.assertEqual(1, 1)
	def test_korean_proofread(self):
		import korean
		res = korean.l10n.proofread(u"황윤구(은)는 지금 졸리다.")
		self.assertEqual(res, u"황윤구는 지금 졸리다.")
	def test_korean_proofread_fail(self):
		import korean
		res = korean.l10n.proofread(u"황윤구(은)는 지금 졸리다.")
		self.assertNotEqual(res, u"황윤구은 지금 졸리다.")