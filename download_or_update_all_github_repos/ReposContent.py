import requests
import os
import subprocess

class ReposContent:

    def __init__(self, giverUser: str):
        self.giverUser = giverUser
        self.currentPage = 0
        self.failingMessage = ""

    def haveContent(self) -> bool:
        iterationContent = self.__get_api_content()
        if len(iterationContent) > 0:
            self.downloadOrUpdateGroupOfRepos(iterationContent)
            return True
        else:
            return False

    def nextPge(self):
        self.currentPage += 1

    def canGetRepos(self) -> bool:
        iterationContent = self.__get_api_content()
        if "message" in iterationContent:
            self.failingMessage = iterationContent["message"]
            return True
        return False

    def getCoundNotGetMessage(self) -> str:
        return self.failingMessage

    def downloadOrUpdateGroupOfRepos(self, repos):
        for repo in repos:

            repo_address = repo["html_url"]
            repo_folder = self.__get_repo_folder(repo_address)

            if os.path.isdir(repo_folder):
                print("Updading repository: " + repo_address)
                os.chdir(repo_folder)
                subprocess.call(["git", "pull"])
                os.chdir("..")
            else:
                print("Cloning repository: " + repo_address)
                subprocess.call(["git", "clone", repo_address])

    def __get_api_content(self):
        address = "https://api.github.com/users/" + self.giverUser + "/repos?page=" + str(self.currentPage)
        r = requests.get(address)
        return r.json()

    def __get_repo_folder(self, repo_address) -> str:
        broken_words_from_repos = repo_address.split("/")
        return broken_words_from_repos[4]

