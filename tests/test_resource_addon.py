import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


ADDON_ROOT = Path(__file__).resolve().parents[1]


class ArcticFuseResourceAddonTests(unittest.TestCase):
    def test_manifest_registers_image_resources_and_license(self):
        addon = ET.parse(ADDON_ROOT / "addon.xml").getroot()
        self.assertEqual(addon.get("id"), "resource.images.arctic.fuse.3")
        self.assertEqual(
            addon.find("./extension[@point='kodi.resource.images']").get("compile"),
            "true",
        )
        self.assertEqual(
            addon.find("./extension[@point='kodi.resource.images']").get("type"),
            "arctic.fuse.3",
        )
        self.assertIn(
            "kodi.resource",
            {node.get("addon") for node in addon.findall("./requires/import")},
        )
        self.assertIn("Creative Commons", (ADDON_ROOT / "LICENSE.txt").read_text())

    def test_browse_directories_and_metadata_assets_exist(self):
        extras = ADDON_ROOT / "resources" / "extras"
        for directory in (
            "backgrounds",
            "icons",
            "screenshots",
            "viewtypes",
        ):
            with self.subTest(directory=directory):
                self.assertTrue((extras / directory).is_dir())
        extensions = {path.suffix.lower() for path in extras.rglob("*") if path.is_file()}
        self.assertEqual(extensions, {".jpg", ".png"})

        for icon in (
            "play.png",
            "play3.png",
            "circle-check-regular.png",
            "circle-check.png",
            "circle-xmark-regular.png",
            "circle-xmark.png",
        ):
            with self.subTest(icon=icon):
                self.assertTrue((extras / "icons" / icon).is_file())

        addon = ET.parse(ADDON_ROOT / "addon.xml").getroot()
        metadata = addon.find("./extension[@point='xbmc.addon.metadata']")
        for name in ("icon", "fanart", "screenshot"):
            for entry in metadata.findall(f"./assets/{name}"):
                with self.subTest(asset=entry.text):
                    self.assertTrue((ADDON_ROOT / entry.text).is_file())


if __name__ == "__main__":
    unittest.main()
