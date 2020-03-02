from unittest import TestCase
import json

import cv2

from src import assets
import os

from src.domain.vision.PuckFinder import PuckFinder
from src.domain.vision.TableCropper import TableCropper


class TestPuckFinder(TestCase):

    def load_mappings(self):
        self.puck_mapping = {}
        self.table_mapping = {}
        with open(os.path.dirname(assets.__file__) + "/Mapping/puck_mapping.json") as mapping_json_file:
            self.puck_mapping = json.loads(mapping_json_file.read())
        with open(os.path.dirname(assets.__file__) + "/Mapping/table_mapping.json") as mapping_json_file:
            self.table_mapping = json.loads(mapping_json_file.read())

    def table_id_generator(self):
        for table_id in sorted(self.table_mapping):
            if len(self.table_mapping[table_id]) and table_id in self.puck_mapping:
                yield table_id

    def image_id_generator(self, table_id):
        for image_id in sorted([*self.puck_mapping[table_id]], key=lambda s: int(s[6:])):
            yield image_id

    @staticmethod
    def get_image(table_id, image_id):
        return cv2.imread(os.path.dirname(assets.__file__) + f"/Mapping/{table_id}/{image_id}.jpg")

    def mapped_color_generator(self, table_id, image_id):
        for color in self.puck_mapping[table_id][image_id]:
            yield color

    def __test_puck_found(self, table_id, image_id, puck_found, delta=10):
        for color in self.mapped_color_generator(table_id, image_id):
            with self.subTest(table=table_id, image=image_id, color=color):
                self.assertIn(color, puck_found)
                for axis in ['x', 'y']:
                    axis_found = puck_found[color][axis]
                    axis_target = self.puck_mapping[table_id][image_id][color][axis]
                    self.assertAlmostEqual(axis_found, axis_target, delta=delta, msg=f"{axis}")

    def test_find_pucks(self):
        self.load_mappings()
        puck_finder = PuckFinder()
        for table_id in self.table_id_generator():
            for image_id in self.image_id_generator(table_id):
                image = self.get_image(table_id, image_id)
                table_cropper = TableCropper(self.table_mapping[table_id])
                image_cropped = table_cropper.crop(image)
                puck_found = puck_finder.find_pucks(image_cropped, debug=False)
                self.__test_puck_found(table_id, image_id, puck_found)
