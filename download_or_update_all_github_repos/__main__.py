from download_or_update_all_github_repos.fn import getGivenUser
from download_or_update_all_github_repos.ReposContent import ReposContent

def main():

    givenUser = getGivenUser()
    reposContent = ReposContent(givenUser)

    if reposContent.canGetRepos():
        print("There's an issue in fetch the content: " + reposContent.getCoundNotGetMessage())
        exit()

    while reposContent.haveContent():
        reposContent.nextPge()
