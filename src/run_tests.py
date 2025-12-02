#!/usr/bin/env python3
import sys
#               Copyright © DuckieCorp. All Rights Reserved.
#
#  Everyone is permitted to copy and distribute verbatim copies of this
#      license document, but changing or removing it isn't allowed.
#
#                       __     TERMS AND CONDITIONS
#                     /` ,\__
#                    |    ).-' 0. "Copyright" applies to other kinds of
#                   / .--'        works, such as coin-op arcade machines,
#                  / /            novelty T-shirts (both offensive and
#    ,      _.==''`  \            inoffensive), macrame, and warm (but
#  .'(  _.='         |            not frozen) desserts.
# {   ``  _.='       |         1. "The Program" refers to any copyrightable
#  {    \`     ;    /             work, recipe, or social media post
#   `.   `'=..'  .='              licensed under this License.
#     `=._    .='              2. "Licensees" and "recipients" may be
#  jgs  '-`\\`__                  individuals, organizations, or both;
#           `-._(                 further, they may be artificially or
#                                 naturally sentient (or close enough).


import unittest
from tests import test_phoenix, test_mandelbrot, test_image, test_lambda, test_parser, test_septagon, test_oceanlava, test_moth, test_joker, test_toxic

suite = unittest.TestSuite()

for test in [test_parser.TestParser, test_phoenix.TestPhoenix, test_mandelbrot.TestMandelbrot, test_lambda.TestLambda, test_septagon.TestSeptagon, test_image.TestImagePainter, test_oceanlava.TestOceanLava, test_moth.TestMoth, test_joker.TestJoker, test_toxic.TestToxic]:
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(test))
unittest.TextTestRunner(verbosity=2).run(suite)

# test_dict = {
#     'centerx': 0.5,
#     'centery': 0.3,
#     'axislength': 0.1,
#     'preal': -0.5,
#     'pimag': 0.0,
#     'creal': 0.5667,
#     'cimag': 0.0,
#     'pixels': 500,
#     'iterations': 100,
#     'name':'mandelbrot'
# }
#
# class TestHelperMethods(unittest.TestCase):
#     def setUp(self):
#         self.here = os.path.dirname(__file__)
#
#     def test_min_max(self):
#         test_min, test_size = image.min_max(test_dict)
#         self.assertEqual(test_min[0], 0.45)
#         self.assertEqual(test_min[1], 0.25)
#         self.assertEqual(test_size, 0.00019531250000000007)
#
#     def test_phoenix_count(self):
#         less_than_two = phoenix.count(complex(2, 2), test_dict['iterations'], complex(0.55, 0.35), complex(test_dict['preal'], test_dict['pimag']))
#         exceeds_two = phoenix.count(complex(0, 0), test_dict['iterations'], complex(0.55, 0.35), complex(test_dict['preal'], test_dict['pimag']))
#         self.assertTrue(exceeds_two > 2)
#         self.assertTrue(less_than_two < 2)
#         self.assertEqual((0.45 + 1 * 0.1), 0.55)
#         self.assertEqual((0.25 + 1 * 0.1), 0.35)
#
#     def test_mbrot_count(self):
#         exceeds_two = mandelbrot.count(complex(0.55, 0.35), test_dict['iterations'])
#         less_than_two = mandelbrot.count(complex(2, 2), test_dict['iterations'])
#         self.assertTrue(exceeds_two > 2)
#         self.assertTrue(less_than_two < 2)
#         self.assertEqual((0.45 + 1 * 0.1), 0.55)
#         self.assertEqual((0.25 + 1 * 0.1), 0.35)
#
#     def test_phoenix_dict(self):
#         phoenix_dict = parser.dictionary(f"{self.here}/tests/p/phoenix.frac", 'phoenix')
#         self.assertEqual(phoenix_dict['type'], 'phoenix')
#         self.assertRaises(RuntimeError, parser.dictionary, f"{self.here}/tests/p/no-property-name.frac", 'phoenix')
#         self.assertRaises(RuntimeError, parser.dictionary, f"{self.here}/tests/p/commented-out-property.frac", 'phoenix')
#         self.assertRaises(ValueError, parser.dictionary, f"{self.here}/tests/p/negative-axislen.frac", 'phoenix')
#         self.assertRaises(ValueError, parser.dictionary, f"{self.here}/tests/p/zero-axislen.frac", 'phoenix')
#
#     def test_mbrot_dict(self):
#         mbrot_dict = parser.dictionary(f"{self.here}/tests/m/mandelbrot.frac", 'mandelbrot')
#         self.assertEqual(mbrot_dict['type'], 'mandelbrot')
#         self.assertRaises(RuntimeError, parser.dictionary, f"{self.here}/tests/m/commented-out-property.frac", 'mandelbrot')
#         self.assertRaises(RuntimeError, parser.dictionary, f"{self.here}/tests/m/no-property-name.frac", 'mandelbrot')
#         self.assertRaises(ValueError, parser.dictionary, f"{self.here}/tests/m/negative-axislen.frac", 'mandelbrot')
#         self.assertRaises(ValueError, parser.dictionary, f"{self.here}/tests/m/zero-axislen.frac", 'mandelbrot')
#
#     def test_dict_creator(self):
#         self.assertRaises(ValueError, parser.dictionary, f"{self.here}/tests/m/bad-float-value.frac", 'mandelbrot')
#         self.assertRaises(RuntimeError, parser.dictionary, f"{self.here}/tests/m/no-colons.frac", 'mandelbrot')
#         self.assertRaises(ValueError, parser.dictionary, f"{self.here}/tests/m/bad-int-value.frac", 'mandelbrot')
#         self.assertRaises(RuntimeError, parser.dictionary, f"{self.here}/tests/m/too-many-colons.frac", 'mandelbrot')
#         self.assertRaises(ValueError, parser.dictionary, f"{self.here}/tests/m/missing-value.frac", 'mandelbrot')
#         self.assertRaises(ValueError, parser.dictionary, f"{self.here}/tests/p/bad-float-value.frac", 'phoenix')
#         self.assertRaises(ValueError, parser.dictionary, f"{self.here}/tests/p/bad-int-value.frac", 'phoenix')
#         self.assertRaises(ValueError, parser.dictionary, f"{self.here}/tests/p/missing-value.frac", 'phoenix')
#         self.assertRaises(RuntimeError, parser.dictionary, f"{self.here}/tests/p/too-many-colons.frac", 'phoenix')
#         self.assertRaises(RuntimeError, parser.dictionary, f"{self.here}/tests/p/no-colons.frac", 'phoenix')
#
#     def test_phoenix_color(self):
#         self.assertEqual('#f4ff86', palettes.get_phoenix_color(15))
#         self.assertEqual('#15ff41', palettes.get_phoenix_color(51))
#         self.assertEqual('#002277', palettes.get_phoenix_color(200))
#
#     def test_mbrot_color(self):
#         self.assertEqual('#D8DE97', palettes.get_mbrot_color(6))
#         self.assertEqual('#6DCB8C', palettes.get_mbrot_color(39))
#         self.assertEqual('#7D387D', palettes.get_mbrot_color(110))
#
#     def test_tkinter_window(self):
#         window, img, start = image.create_window()
#         self.assertIsNotNone(window)
#         self.assertIsNotNone(img)
#         self.assertEqual(512, img.width())
#         self.assertIsNotNone(start)
#
#     def test_status_bar(self):
#         self.assertEqual('[100% =================================]', image.status_bar(1))
#         self.assertEqual('[ 75% =========================        ]', image.status_bar(128))
#         self.assertEqual('[ 50% =================                ]', image.status_bar(256))
#         self.assertEqual('[ 25% ========                         ]', image.status_bar(384))
#         self.assertEqual('[  0%                                  ]', image.status_bar(512))
        
