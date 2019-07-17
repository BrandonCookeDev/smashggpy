import re
import sys

from os.path import abspath
from pathlib import Path
from subprocess import call

ROOT_FOLDER = abspath(Path(__file__, '..', '..'))
DEVOPS_FOLDER = abspath(Path(__file__, '..'))
SETUP_PATH = abspath(Path(__file__, '..', '..', 'setup.py'))
DEPLOY_SCRIPT_PATH = abspath(Path(__file__, '..', 'deploy.sh'))
VERSION_REGEX = re.compile("(version=\"([0-9]+.[0-9]+.[0-9]+)\")")
MAJOR_MINOR_PATCH_REGEX = re.compile("([0-9]+).([0-9]+).([0-9]+)")
GIT_STATUS_COMMAND = 'cd {} && git status'.format(ROOT_FOLDER)
GIT_COMMIT_COMMAND = 'cd ' + ROOT_FOLDER + ' && git add . && git commit -m "{0}" && git push'


def read_setup_py() -> str:
    lines = []
    content = ""
    with open(SETUP_PATH) as f:
        lines = f.readlines()
    return content.join(lines)


def get_version_from_setup():
    content = read_setup_py()
    version_match = VERSION_REGEX.search(content)
    if version_match:
        groups = version_match.groups()
        if len(groups) > 1:
            return groups[1]
        else:
            raise Exception('no version matching regular expression')
    else:
        raise Exception('no version property in setup.py')


def add_to_version(input, major=0, minor=0, patch=1):
    version_match = MAJOR_MINOR_PATCH_REGEX.search(input)
    if version_match:
        groups = version_match.groups()
        if len(groups) is 3:
            cur_major = int(groups[0])
            cur_minor = int(groups[1])
            cur_patch = int(groups[2])

            new_major = cur_major + int(major)
            new_minor = cur_minor + int(minor)
            new_patch = cur_patch + int(patch)

            return "{0}.{1}.{2}".format(new_major, new_minor, new_patch)

    raise Exception('no major-minor-patch matching regular expression')


def write_version_to_setup_py(version: str):
    content = read_setup_py()
    replaced = VERSION_REGEX.sub('version="{}"'.format(version), content)
    lines = replaced.split('\n')
    lines = [line + '\n' for line in lines]
    with open(SETUP_PATH, "w") as f:
        f.writelines(lines)


def process_with_deployment():
    response = input('Input [y] to continue with this deployment...')
    if response != 'y':
        print('Deployment canceled. Input was: {}'.format(response))
        sys.exit(1)

    write_version_to_setup_py(new_version)
    call(DEPLOY_SCRIPT_PATH, shell=True)
    print('deployment complete! Version: {}'.format(new_version))


def do_git_commit():
    call(GIT_STATUS_COMMAND, shell=True)
    do_commit_response = input('Would you like to commit to the git repository? (all the above will be included) [y] ')
    if do_commit_response != 'y':
        print('Not committing. Input was: {}'.format(do_commit_response))
        sys.exit(0)

    commit_message = input('Please type your commit message: ')
    git_command = GIT_COMMIT_COMMAND.format(commit_message)
    print(git_command)
    call(git_command, shell=True)


if __name__ == "__main__":
    print('beginning deployment')
    print(GIT_COMMIT_COMMAND)

    major = sys.argv[1] if len(sys.argv) > 1 else 0
    minor = sys.argv[2] if len(sys.argv) > 2 else 0
    patch = sys.argv[3] if len(sys.argv) > 3 else 1
    print(major, minor, patch)

    version = get_version_from_setup()
    new_version = add_to_version(version, major, minor, patch)
    print('current version: {}'.format(version))
    print('new version after update: {}'.format(new_version))

    process_with_deployment()
    do_git_commit()

    print('Completed!')
