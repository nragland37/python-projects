import importlib.util
import pathlib

# Dynamically load the grapevines module
module_path = pathlib.Path(__file__).resolve().parents[1] / \
    'src/01-grapevineFarmingCalculator/grapevines.py'
spec = importlib.util.spec_from_file_location('grapevines', module_path)
grapevines = importlib.util.module_from_spec(spec)
spec.loader.exec_module(grapevines)


def test_get_vines_example():
    assert grapevines.get_vines(300, 1.5, 2.2) == 135.0
