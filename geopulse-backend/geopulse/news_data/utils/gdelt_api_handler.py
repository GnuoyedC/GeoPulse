import apps.common.utils.json_handler as jsh
class GDELTAPI:
    @classmethod
    def test(cls):
        print("Test")
GDELTAPI.test()

if __name__ == '__main__':
    import sys
    from pathlib import Path

    # Add the project root directory to the Python path
    sys.path.append(str(Path(__file__).resolve().parents[4]))

    # Now import the setup script from the deep directory
    from backend.apps.common.utils.setup_django import setup
    setup()
    
