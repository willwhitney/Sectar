import os
HOME = os.path.expanduser("~")

CODE_DIRS_TO_MOUNT = [
    HOME + '/code/rllab',
    HOME + '/code/Sectar/traj2vec',
    HOME + '/code/baselines'
]
DIR_AND_MOUNT_POINT_MAPPINGS = [
    dict(
        local_dir=HOME + '/.mujoco/',
        mount_point='/root/.mujoco',
    ),
]
LOCAL_LOG_DIR = HOME + '/code/Sectar/traj2vec/data/local/'
RUN_DOODAD_EXPERIMENT_SCRIPT_PATH = (
    HOME + '/code/Sectar/scripts/run_experiment_from_doodad.py'
)
DOODAD_DOCKER_IMAGE = 'jcoreyes/traj2vecv3:latest'

# This really shouldn't matter and in theory could be whatever
OUTPUT_DIR_FOR_DOODAD_TARGET = '/tmp/doodad-output/'
# OUTPUT_DIR_FOR_DOODAD_TARGET = '/tmp/dir/from/railrl-config/'
