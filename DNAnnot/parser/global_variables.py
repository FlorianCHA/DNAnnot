import sys
from pathlib import Path

DOCS="https://DNANNOT-pipeline.readthedocs.io/en/latest/"
# Hack for build docs with unspecified path install
args = str(sys.argv)
if "sphinx" in args:
    DNANNOT_PATH = Path("/Path/to/DNANNOT_install/")
else:
    DNANNOT_PATH = Path(__file__).resolve().parent.parent

DNANNOT_SNAKEFILE = DNANNOT_PATH.joinpath("Snakefile")
DNANNOT_MODE = DNANNOT_PATH.joinpath(".mode.txt")
DNANNOT_SCRIPTS = DNANNOT_PATH.joinpath("scripts")
DNANNOT_PROFILE = DNANNOT_PATH.joinpath("default_profile")
DNANNOT_CONFIG_PATH = DNANNOT_PATH.joinpath("install_files", "config.yaml")

DNANNOT_TOOLS_PATH = DNANNOT_PATH.joinpath("install_files", "tools_path.yaml")
DNANNOT_USER_TOOLS_PATH = Path("~/.config/DNANNOT/tools_path.yaml").expanduser()
DNANNOT_ARGS_TOOLS_PATH = Path("~/.config/DNANNOT/tools_path_args.yaml").expanduser()

DNANNOT_CLUSTER_CONFIG = DNANNOT_PROFILE.joinpath("cluster_config.yaml")
DNANNOT_USER_CLUSTER_CONFIG = Path("~/.config/DNANNOT/cluster_config.yaml").expanduser()
DNANNOT_ARGS_CLUSTER_CONFIG = Path("~/.config/DNANNOT/cluster_config_args.yaml").expanduser()

SINGULARITY_URL_FILES = 'shub://FlorianCHA/singularity_containers:braker'
