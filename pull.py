# This simple pattern does what nbgitpuller does on
# https://jupyterhub.cs.tufts.edu for someone who is
# running their own server.

from nbgitpuller import GitPuller

# enter your repository location as a path on your hard disk.
# an absolute path is recommended. The example path is in Windows.

MY_REPO = '/c/Users/acouch/Documents/GitHub/comp205'
gp = GitPuller("https://github.com/prof-couch/comp205", "master", MY_REPO)

try:
    for line in gp.pull():
        print(line)  # print log output from actions taken
except Exception as e:
    print(e)
