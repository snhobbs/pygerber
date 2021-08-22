from types import SimpleNamespace
from unittest import TestCase, main

from pygerber.meta.aperture_manager import ApertureManager

from .test_aperture import ApertureSetTest, CircleApertureCollector


class ApertureManagerTest(TestCase):
    def get_dummy_bound_aperture_manager(self):
        am = ApertureManager(ApertureSetTest.get_dummy_apertureSet())
        return am

    def test_define_aperture(self):
        am = self.get_dummy_bound_aperture_manager()
        args = SimpleNamespace(
            DIAMETER=0.2,
            HOLE_DIAMETER=0,
        )
        am.define_aperture("C", None, 10, args)
        self.assertEqual(type(am.apertures[10]), CircleApertureCollector)
        self.assertEqual(am.apertures[10].DIAMETER, args.DIAMETER)
        self.assertEqual(am.apertures[10].HOLE_DIAMETER, args.HOLE_DIAMETER)

    def test_get_aperture(self):
        am = self.get_dummy_bound_aperture_manager()
        args = SimpleNamespace(
            DIAMETER=0.2,
            HOLE_DIAMETER=0,
        )
        am.define_aperture("C", None, 10, args)
        self.assertEqual(am.apertures[10], am.get_aperture(10))


if __name__ == "__main__":
    main()